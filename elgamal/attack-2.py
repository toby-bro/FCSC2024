import pexpect
from sympy import mod_inverse
import forge

# Open a connection to the server using nc
nc_process = pexpect.spawn("nc challenges.france-cybersecurity-challenge.fr 2152")

# Wait for the server response and extract p, g, and y values
nc_process.expect("p = (\d+)")
p = int(nc_process.match.group(1))
nc_process.expect("g = (\d+)")
g = int(nc_process.match.group(1))
nc_process.expect("y = (\d+)")
y = int(nc_process.match.group(1))
nc_process.expect("m = (\d+)")
m = int(nc_process.match.group(1))

# Print p, g, and y
print("p =", p)
print("g =", g)
print("y =", y)
print("m =", m)

# Forge a signature
reply = forge.forge_sign(p, g, y, m)
#print(reply)

# Send the forged signature to the server
for i in reply:
    nc_process.expect("\n")  # Wait for the server prompt
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

