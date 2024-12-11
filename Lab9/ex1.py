import random
import pandas as pd

# IP table
IP_table = [
    [58, 50, 42, 34, 26, 18, 10, 2],
    [60, 52, 44, 36, 28, 20, 12, 4],
    [62, 54, 46, 38, 30, 22, 14, 6],
    [64, 56, 48, 40, 32, 24, 16, 8],
    [57, 49, 41, 33, 25, 17, 9, 1],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [61, 53, 45, 37, 29, 21, 13, 5],
    [63, 55, 47, 39, 31, 23, 15, 7]
]

# IP^-1 table
IP_inverse_table = [
    [40, 8, 48, 16, 56, 24, 64, 32],
    [39, 7, 47, 15, 55, 23, 63, 31],
    [38, 6, 46, 14, 54, 22, 62, 30],
    [37, 5, 45, 13, 53, 21, 61, 29],
    [36, 4, 44, 12, 52, 20, 60, 28],
    [35, 3, 43, 11, 51, 19, 59, 27],
    [34, 2, 42, 10, 50, 18, 58, 26],
    [33, 1, 41, 9, 49, 17, 57, 25]
]

# Function to flatten a table into a single list
def flatten_table(table):
    return [item for sublist in table for item in sublist]

# Extract n_values_even, n_values_odd from IP_table
flattened_IP = flatten_table(IP_table)
n_values_even = [n for n in flattened_IP if n % 2 == 0]
n_values_odd = [n for n in flattened_IP if n % 2 != 0]

# Extract m_values_odd, m_values_even from IP_inverse_table
flattened_IP_inverse = flatten_table(IP_inverse_table)
m_values_even = [m for m in flattened_IP_inverse if m % 2 == 0]
m_values_odd = [m for m in flattened_IP_inverse if m % 2 != 0]

# Randomly sample values for n and m
random_n_values_even = random.sample(n_values_even, 5)
random_n_values_odd = random.sample(n_values_odd, 5)
random_m_values_odd = random.sample(m_values_odd, 5)
random_m_values_even = random.sample(m_values_even, 5)

print("N values even ", random_n_values_even)
print("N values odd ", random_n_values_odd)
print("M values odd ", random_m_values_odd)
print("M values even ", random_m_values_even)

# Function to calculate h(n) = n mod m
def hash_function_1(n, m):
    return n % m

# Function to calculate h_combined = (h(n1) + h(n2) + ... + h(n6)) mod m
def hash_function_2(numbers, m):
    h_values = [hash_function_1(n, m) for n in numbers]
    return sum(h_values) % m

# Prepare results for the table
results = []

# Case A: Even n and odd m
for n, m in zip(random_n_values_even, random_m_values_odd):
    h1 = hash_function_1(n, m)
    random_n_list = random.sample(random_n_values_even * 2, 6)
    h2 = hash_function_2(random_n_list, m)
    results.append({"n": n, "m": m, "h(n)": h1, "h2(n)": h2, "h2(n) inputs": random_n_list,  "Case": "Even n, Odd m"})


# Case C: Odd n and even m
for n, m in zip(random_n_values_odd, random_m_values_even):
    h1 = hash_function_1(n, m)
    random_n_list = random.sample(random_n_values_odd * 2, 6)
    h2 = hash_function_2(random_n_list, m)
    results.append({"n": n, "m": m, "h(n)": h1, "h2(n)": h2, "h2(n) inputs": random_n_list, "Case": "Odd n, Even m"})

# Convert results to DataFrame
df_results = pd.DataFrame(results)

print("Hash Function Results")
print(df_results)

