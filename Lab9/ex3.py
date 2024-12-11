import random
import hashlib


def hash_function(value):
    return int(hashlib.sha256(value.encode()).hexdigest(), 16)


def schnorr_signature(p, q, g, x, k, M):
    # Calculate y, which is the public key
    y = pow(g, -x, p)
    print(f"Public key y: {y}")

    # Participant A chooses a random number k and calculates r = g^k (mod p)
    r = pow(g, k, p)
    print("Calculated r: ", r)

    # Participant A creates a signature (e, s)
    A = str(r) + M
    e = hash_function(A) % q
    s = (k + x * e) % q

    # Signature (e, s) and text M are sent to participant B
    signature = (e, s)

    return signature, r, y


def schnorr_verification(p, q, g, y, M, signature):
    e, s = signature

    # Participant B verifies the signature by calculating r' and e'
    r_prime = (pow(g, s, p) * pow(y, e, p)) % p
    print("Calculated r`: ", r_prime)
    A_prime = str(r_prime) + M
    e_prime = hash_function(A_prime) % q
    print("Calculated e`: ", e_prime)

    # Compare e and e'
    return e == e_prime


# Based on the Schnorr group equation -> g = h^r mod p
def get_schnorr_group(p, q):
    r = (p - 1) // q
    g_list = []
    for h in range(2, p):
        g = pow(h, r, p)
        if g != 1:
            g_list.append(g)

    g_list = list(set(g_list))
    g_list.sort()
    return g_list


if __name__ == "__main__":
    p = 48731
    q = 443
    print(f"p: {p}\nq: {q}")
    allowed_set = get_schnorr_group(p, q)
    print(f"Found {len(allowed_set)} possible generators g of a Schnorr group subroup of Z_p^x of order q")
    g = random.choice(allowed_set)
    print(f"Picked generator g: {g}")

    # Private key of the scheme, based on that x is chosen from the allowed set
    x = random.choice(allowed_set)

    print(f"Private key x: {x}")

    print("\nParticipant A ")
    M = "Hello World"
    k = random.choice(allowed_set)
    print("Randomly choose value k: ", k)
    signature, r, y = schnorr_signature(p, q, g, x, k, M)
    print(f"Signature: {signature}")
    print(f"\nMessage: {M}")

    print("\nParticipant B ")
    is_valid = schnorr_verification(p, q, g, y, M, signature)
    print("Verification result:", is_valid)
