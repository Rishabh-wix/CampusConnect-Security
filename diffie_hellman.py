# ============================================
# Diffie-Hellman Key Exchange
# Author: Rishabh Srivastava
# ============================================

def diffie_hellman(p, alpha, a, b):
    print("=" * 60)
    print("Diffie-Hellman Key Exchange")
    print("=" * 60)

    print(f"Public Prime (p)      : {p}")
    print(f"Public Base (α)       : {alpha}")
    print(f"Alice Private Key (a) : {a}")
    print(f"Bob Private Key (b)   : {b}")

    # Validation
    if not (1 < a < p - 1):
        print("\nError: Alice private key must satisfy 1 < a < p-1")
        return

    if not (1 < b < p - 1):
        print("\nError: Bob private key must satisfy 1 < b < p-1")
        return

    # Public Keys
    A = pow(alpha, a, p)
    B = pow(alpha, b, p)

    # Shared Secret
    K_alice = pow(B, a, p)
    K_bob = pow(A, b, p)

    print("\nComputed Public Keys")
    print(f"A = α^a mod p = {A}")
    print(f"B = α^b mod p = {B}")

    print("\nShared Secret")
    print(f"Alice computes K = {K_alice}")
    print(f"Bob computes   K = {K_bob}")

    if K_alice == K_bob:
        print("\nResult : SUCCESS")
        print(f"Shared Secret Key = {K_alice}")
    else:
        print("\nResult : FAILED")

    print("=" * 60)


# ============================================
# TEST CASE 1 (Given in Assignment)
# p = 29, α = 2, a = 5, b = 12
# ============================================

print("\nTEST CASE 1")
diffie_hellman(29, 2, 5, 12)


# ============================================
# TEST CASE 2 (Custom)
# ============================================

print("\nTEST CASE 2")
diffie_hellman(23, 5, 6, 15)
