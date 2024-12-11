def custom_hash_function(input_string):
    # Initialize a large prime number for hashing
    hash_value = 5381

    # Iterate through each character in the string
    for char in input_string:
        # Update the hash value using bitwise operations and character ASCII value
        hash_value = ((hash_value << 5) + hash_value) + ord(char)  # hash * 33 + char

    # Ensure the hash value is positive
    return hash_value & 0xFFFFFFFF


test_string = "Hello, World!"
hash_code = custom_hash_function(test_string)

print(f"Input string: {test_string}")
print(f"Hash code: {hash_code}")