def gcd(a, b):
    # Calculate the Greatest Common Divisor of a and b
    while b != 0:
        a, b = b, a % b
    return a


def extended_euclidean(a, b):
    # Find x and y such that ax + by = gcd(a, b)
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modular_inverse(e, phi):
    # Find modular inverse of e mod phi
    gcd, x, _ = extended_euclidean(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi


def rsa_sign(h_m, d, n):
    # Sign the hash value using the private key (d, n)
    signature = pow(h_m, d, n)
    print(f"Signing step: h(M)^d mod n = {h_m}^{d} mod {n} = {signature}")
    return signature


def rsa_verify(signature, e, n):
    # Verify the signature using the public key (e, n)
    verified_hash = pow(signature, e, n)
    print(f"Verification step: s^e mod n = {signature}^{e} mod {n} = {verified_hash}")
    return verified_hash


p = 17
q = 11
n = p * q
phi = (p - 1) * (q - 1)
e = 7

print(f"Calculate n = p * q = {p} * {q} = {n}")
print(f"Calculate φ(n) = (p - 1) * (q - 1) = {p - 1} * {q - 1} = {phi}")

if gcd(e, phi) != 1:
    raise ValueError("e is not coprime with φ(n)")
print(f"Verify gcd(e, φ(n)) = gcd({e}, {phi}) = 1")

d = modular_inverse(e, phi)
print(f"Calculate d = e^(-1) mod φ(n) = {d}")

h_m = 88
print(f"Hash value of the message: h(M) = {h_m}")

signature = rsa_sign(h_m, d, n)

verified_hash = rsa_verify(signature, e, n)

if verified_hash == h_m:
    print("The signature is genuine.")
else:
    print("The signature is not genuine.")
