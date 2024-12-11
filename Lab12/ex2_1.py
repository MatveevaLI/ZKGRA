import math


def find_factors(n):
    sqrt_n = int(math.sqrt(n))

    for i in range(sqrt_n, 0, -1):
        if n % i == 0:
            p = i
            q = n // i
            return p, q

    return None, None


n = 851

p, q = find_factors(n)

if p and q:
    print(f"p = {p}, q = {q}")
else:
    print("No factors found.")
