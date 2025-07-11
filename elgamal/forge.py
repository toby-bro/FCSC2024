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
