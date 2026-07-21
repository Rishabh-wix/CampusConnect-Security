# ============================================
# RSA Algorithm Implementation
# Author: Rishabh Srivastava
# ============================================

from math import gcd

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa(p, q, e, m):
    print("=" * 50)
    print(f"Input Values")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"e = {e}")
    print(f"m = {m}")

    # Validation
    if p == q:
        print("Error: p and q must be different prime numbers.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(e, phi) != 1:
        print("Error: e is not coprime with φ(n).")
        return

    if not (0 <= m < n):
        print("Error: Message must satisfy 0 <= m < n.")
        return

    d = mod_inverse(e, phi)

    c = pow(m, e, n)
    decrypted = pow(c, d, n)

    print("\nCalculated Values")
    print(f"n = {n}")
    print(f"φ(n) = {phi}")
    print(f"d = {d}")

    print("\nEncryption")
    print(f"Ciphertext (c) = {c}")

    print("\nDecryption")
    print(f"Recovered Message = {decrypted}")

    if decrypted == m:
        print("\nResult : Success")
    else:
        print("\nResult : Failed")

    print("=" * 50)


# ============================================
# Test Case 1 (Given in Assignment)
# ============================================

print("\nTEST CASE 1")
rsa(3, 11, 3, 4)

# ============================================
# Test Case 2 (Custom)
# ============================================

print("\nTEST CASE 2")
rsa(13, 17, 5, 9)
