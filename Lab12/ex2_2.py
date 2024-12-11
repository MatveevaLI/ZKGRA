def encrypt(m, e, n):
    return pow(m, e, n)


def reencrypt_with_detailed_steps(c, e, n, original_message):
    iterations = 0
    current = c
    results = []

    while True:
        next_value = encrypt(current, e, n)
        results.append((current, e, n, next_value))
        iterations += 1
        current = next_value

        # Stop when we return to the original message
        if current == original_message:
            break

    return iterations, results


p = 3
q = 11
n = p * q
e = 7
m = 2

C = encrypt(m, e, n)
print(f"Cryptogram (C): {C}\n")

public_key = (e, n)
print(f"Public key: {public_key}\n")

# Perform re-encryption and collect all detailed results
iterations, results = reencrypt_with_detailed_steps(C, e, n, m)

# Print results for all iterations
print("Re-encryption process (step-by-step):")
for i, (base, exp, mod, result) in enumerate(results):
    print(f"Iteration {i + 1}: {base}^{exp} mod {mod} = {result}")

print(f"\nNumber of iterations to return to the original message: {iterations}")
