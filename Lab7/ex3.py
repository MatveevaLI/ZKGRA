matrix = [
    ["63", "7c", "77", "7b"],
    ["ca", "82", "c9", "7d"],
    ["b7", "fd", "93", "26"],
    ["04", "c7", "23", "c3"]
]

shifted_matrix = [
    [matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3]],  # No shift for the first row
    [matrix[1][1], matrix[1][2], matrix[1][3], matrix[1][0]],  # Left shift by 1 for the second row
    [matrix[2][2], matrix[2][3], matrix[2][0], matrix[2][1]],  # Left shift by 2 for the third row
    [matrix[3][3], matrix[3][0], matrix[3][1], matrix[3][2]]  # Left shift by 3 for the fourth row
]

print("Matrix (before ShiftRows):")
for row in matrix:
    print(" ".join(row))

print("Shifted Matrix (after ShiftRows):")
for row in shifted_matrix:
    print(" ".join(row))
