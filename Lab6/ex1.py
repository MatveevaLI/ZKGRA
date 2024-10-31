# Initial permutation table
permutation_table = [
    16, 19, 5, 1, 13,
    14, 4, 21, 10, 8,
    24, 11, 3, 12, 22,
    17, 9, 20, 7, 18,
    23, 2, 6, 15, 25
]

# initial permutation based on initial permutation table
def permute_bits(bit_string, table):
    return ''.join(bit_string[idx - 1] for idx in table)

# DES round with XOR
def des_round(left_part, right_part, round_key):
    # XOR operation between right_part and round_key
    transformed_right = format(int(right_part, 2) ^ int(round_key, 2), '0' + str(len(right_part)) + 'b')
    return transformed_right, left_part  # Swap left and right parts

# simplified DES encryption
def des_encrypt(input_message, encryption_key, perm_table):
    # Convert message to an 8-bit binary format
    binary_data = ''.join(format(ord(character), '08b') for character in input_message)

    permuted_data = permute_bits(binary_data, perm_table)

    # Split permuted data to left and right parts
    left_side, right_side = permuted_data[:len(permuted_data) // 2], permuted_data[len(permuted_data) // 2:]

    # Round 1 and 2
    right_side, left_side = des_round(left_side, right_side, encryption_key)
    right_side, left_side = des_round(left_side, right_side, encryption_key)

    # Combine the left and right parts
    encrypted_output = left_side + right_side

    return encrypted_output


print("Enter message for encryption:")
input_message = input()
encryption_key = "10101010"

encrypted_result = des_encrypt(input_message, encryption_key, permutation_table)
print(f"Encrypted output: {encrypted_result}")
