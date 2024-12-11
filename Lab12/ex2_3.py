def is_valid_split(split):
    # Check if all numbers in a split are valid (between 1 and 26) and do not start with 0
    return all(1 <= int(part) <= 26 and not part.startswith("0") for part in split)


def possible_splits(ciphertext):
    # Generate all valid splits of the ciphertext into numbers 1–26
    n = len(ciphertext)
    splits = []

    def generate(index, current_split):
        # Base case: if we've processed all digits
        if index == n:
            if is_valid_split(current_split):
                splits.append(current_split)
            return

        # Generate one-digit split
        if index < n:
            generate(index + 1, current_split + [ciphertext[index]])

        # Generate two-digit split if possible and does not start with 0
        if index + 1 < n and ciphertext[index] != "0":
            generate(index + 2, current_split + [ciphertext[index:index + 2]])

    generate(0, [])
    return splits


def decrypt(split, key):
    # Decrypt a split of ciphertext using the given key
    plaintext = ""
    for num in split:
        num = int(num)
        letter_num = (num - key) % 26  # Shift back by the key and wrap around
        if letter_num == 0:
            letter_num = 26
        plaintext += chr(letter_num + 64)  # Convert to letter (A=65 in ASCII)
    return plaintext


def brute_force(ciphertext):
    # brute force decryption for all valid splits and keys
    splits = possible_splits(ciphertext)
    for key in range(1, 27):  # Keys from 1 to 26
        print(f"\nKey {key}:")
        for split in splits:
            decrypted_text = decrypt(split, key)
            print(f"Split {split} -> {decrypted_text}")


ciphertext = "202412"

print("Brute-forcing decryption:")
brute_force(ciphertext)
