import pandas as pd
from tabulate import tabulate

# calculate y = a^x mod n
def mod_exp_table(n):
    # Create a DataFrame with index and columns ranging from 1 to n-1
    df = pd.DataFrame(index=range(1, n), columns=range(1, n))

    # Fill the table with values for y = a^x mod n
    for a in range(1, n):
        for x in range(1, n):
            df.iloc[a-1, x-1] = pow(a, x, n)

    return df

n = 8
# n = 11
table = mod_exp_table(n)

# Display the table
print(tabulate(table, headers='keys', tablefmt='grid'))