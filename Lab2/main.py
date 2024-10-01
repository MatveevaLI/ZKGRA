import time


# find a key in a dictionary based on a given value
def find_key_by_value(dictionary, search_value):
    for key, value in dictionary.items():
        if value == search_value:
            return key
    return None


# Initializes dictionaries for shifted order of encoding message
def initialize(K):
    shifted_order = {}

    for i in range(26):
        letter = chr(ord('a') + i)
        if i <= 26:
            shifted_order[letter] = i + K + 1
        elif i > 26:
            shifted_order[letter] = i + K - 26 + 1

    return shifted_order


# Encodes a given text into a list of numbers based on the provided letter mapping
def encoding(text, letters):
    message = []
    for i in text:
        direct_number = letters[i]
        message.append(direct_number)
    return message


# Decodes a list of numbers back into a string using the provided letter mapping
def decoding(text, letters):
    decoded_message = "".join(find_key_by_value(letters, num) for num in text)
    return decoded_message


K = 2
letter_numbers_shifted = initialize(K)

print("Example:\n\t decoded message: matveeva\n\t encoded message: 15,3,22,24,7,7,24,3\n")
user_input = input("Please enter surname: ")
divider = ","

shifted_encoding_message = []


def duration(start_time, end_time):
    return end_time - start_time


# Execute a given function and measure its time duration. Then print the results
def exec_with_time(input_message, function, alphabet, function_message):
    start_time = time.perf_counter()
    output = function(input_message, alphabet)
    end_time = time.perf_counter()
    print(
        "[{:.3f}ms] {} message:\t\t{} {}".format(duration(start_time, end_time) * 1000, function_message, input_message,
                                                 output))


if divider not in user_input:
    user_input = user_input.lower()

    exec_with_time(user_input, encoding, letter_numbers_shifted, "Shifted")

elif divider in user_input:
    user_input_array = [int(num) for num in user_input.split(',')]

    exec_with_time(user_input_array, decoding, letter_numbers_shifted, "Shifted")
else:
    print("String doesn't support")
