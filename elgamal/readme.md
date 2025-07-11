# El Gamal

## 1
In this first challenge we must input a message and a valid signature. After reading this [website](https://ctf-wiki.org/crypto/signature/elgamal/) translated of course. I saw that if we could create the message, then we could also forge it's signature.

The code to create a message and it's signature is 
```python
def forge_signature(p, g, y):
    # Choose integers i and j where gcd(j, p-1) = 1
    i = 2
    j = 3

    # Calculate signature components
    r = pow(g, i, p) * pow(y, j, p) % p
    #print(r)
    s = -r * mod_inverse(j, p-1) % (p-1)
    # Calculate the message
    m = s * i % (p-1)

    return m, r, s
```

I had a little bit of trouble trying to automatise my interactions with the remote server (especially as my school started blocking randomly requests issuing to challenges.france-cybersecurity-challenge.fr on ports 2151 and 2152) 

The final code to validate the challenge is attack-1.py 
```python
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

```
It did not work each time, but it worked regularly enough to get the flag.

## 2
Cracking this second challenge proved much more complicated, as I went into guessing that maybe these random numbers could be factorized using baby step giant step algorithm. I implemented this algorithm in python. But as this was too slow I implemented it in C. But the numbers in input are much too big to fit in an int so I went to the gmp library, but that was too slow so I went for the NTL library. Once I did all this I thought maybe this was not an interesting method, as the solidity of El Gamal signature was supposed to rely on the complexity of the discrete logarithm.

So I went into chasing obscure properties of numbers such that $ p \equiv 1 \pmod 4 $

After having read much litterature on groups and generators and ... I finally found this [paper](https://crypto.ethz.ch/publications/files/Bleich96.pdf). And I thank Mr Bleichenbacher for having explained so clearly how he could attack such a fake signature. It took me some time to understand all his proof, but step by step with my basic knowledge of groups (and with a few questions to friends on what such groups were and what was a generator, obscure conjectures on 2 as a universal generator..., that I did not understand). I put together a forge.py 
```python
from sympy import mod_inverse
"""
Merci à https://crypto.ethz.ch/publications/files/Bleich96.pdf
"""

def get_z(alpha, w, b, y, p):
    alpha_w = pow(alpha, w, p)
    yaw = pow(y, w, p)
    for i in range(b):
        if pow(alpha_w, i, p) == yaw:
            return i
    return None

def get_f():
    return 1

def get_s(alpha, h, p, y):
    b = 4
    k = (p-3) // 2
    w = (p-1) // b
    c = get_c(alpha, w, k, p)
    f = get_f()
    z = get_z(alpha, w, b, y, p)
    num = h - c * w * z
    den = f
    mod_inv = mod_inverse(k // f, (p - 1) // f)
    return (num // den * mod_inv) % ((p-1)//f)

def get_r(alpha, p, k):
    return pow(alpha, k, p)

def get_c(alpha, w, k, p):
    return pow(alpha, k, p) // w

def forge_sign(p, alpha, y, h):
    """
    m correspond au h du papier
    g est le alpha du papier
    """
    k = (p-3)//2
    return (get_r(alpha, p, k), get_s(alpha, h, p, y))
```

That put with an attack-2.py got me this flag.
```python
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

```
