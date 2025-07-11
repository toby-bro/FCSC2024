import pexpect
from sympy import mod_inverse

def forge_signature(p, g, y):
    # Choose integers i and j where gcd(j, p-1) = 1
    i = 3
    j = 5

    # Calculate signature components
    r = pow(g, i, p) * pow(y, j, p) % p
    s = -r * mod_inverse(j, p-1) % (p-1)
    
    # Calculate the message
    m = s * i % (p-1)

    return m, r, s

# Open a connection to the server using nc
nc_process = pexpect.spawn("nc challenges.france-cybersecurity-challenge.fr 2151")

# Wait for the server response and extract p, g, and y values
nc_process.expect("p = (\d+)")
p = int(nc_process.match.group(1))
nc_process.expect("g = (\d+)")
g = int(nc_process.match.group(1))
nc_process.expect("y = (\d+)")
y = int(nc_process.match.group(1))

# Print p, g, and y
print("p =", p)
print("g =", g)
print("y =", y)

# Forge a signature
reply = forge_signature(p, g, y)
print(reply)

# Send the forged signature to the server
for i in reply:
    nc_process.expect(">>> ")  # Wait for the server prompt
    nc_process.sendline(str(i))
    print('sent')
# Print the server output line by line
while True:
    try:
        nc_process.expect('\n')
        print(nc_process.before.strip())
    except pexpect.EOF:
        break

# Print the server output
print(nc_process.before.decode())

# Close the connection
nc_process.close()

