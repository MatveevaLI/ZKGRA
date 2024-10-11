polybius_square = [
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P', 'Q', 'R'],
    ['S', 'T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', '0', '1', '2', '3'],
    ['4', '5', '6', '7', '8', '9']
]


def get_char_from_polybius(letter):
    for row in range(len(polybius_square)):
        for col in range(len(polybius_square[row])):
            if polybius_square[row][col] == letter:
                return row + 1, col + 1
    return None


user_input = input("Please enter message: ")
user_input = user_input.upper()
words = user_input.split()

encoded_words = []
encoded_message = []

for word in words:
    encoded_word = []
    for letter in word:
        encoded_value = get_char_from_polybius(letter)
        if encoded_value:
            encoded_word.append(f"{encoded_value[0]}{encoded_value[1]}")
    encoded_words.append(" ".join(encoded_word))

for encoded_word in encoded_words:
    print(encoded_word)
