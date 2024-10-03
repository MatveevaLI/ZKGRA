import time


# find a key in a dictionary based on a given value
def find_key_by_value(dictionary, search_value):
    for key, value in dictionary.items():
        if value == search_value:
            return key
    return None


# Initializes dictionaries for direct, reverse, divided orders and shifted of encoding message
def initialize(K):
    direct_order = {}
    reverse_order = {}
    divide_order = {}
    shifted_order = {}

    for i in range(26):
        letter = chr(ord('a') + i)
        direct_order[letter] = i + 1
        reverse_order[letter] = 27 - (i + 1)
        if i < 13:
            divide_order[letter] = 13 - i
        else:
            divide_order[letter] = 39 - i

        shifted_value = (i + 1 + K) % 26
        if shifted_value == 0:
            shifted_value = 26
        shifted_order[letter] = shifted_value

    return direct_order, reverse_order, divide_order, shifted_order


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
letter_numbers_direct, letter_numbers_reverse, letter_numbers_divide, letter_numbers_shifted = initialize(K)

print("Example:\n\t decoded message: matveeva\n\t encoded message: 13,1,20,22,5,5,22,1\n\t Caesar cipher:   15,3,22,24,7,7,24,3")
user_input = input("Please enter surname: ")
divider = ","

direct_encoding_message = []
reverse_encoding_message = []
divide_encoding_message = []
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

    exec_with_time(user_input, encoding, letter_numbers_direct, "Direct ")
    exec_with_time(user_input, encoding, letter_numbers_reverse, "Reverse")
    exec_with_time(user_input, encoding, letter_numbers_divide, "Divided")
    exec_with_time(user_input, encoding, letter_numbers_shifted, "Shifted")

elif divider in user_input:
    user_input_array = [int(num) for num in user_input.split(',')]

    exec_with_time(user_input_array, decoding, letter_numbers_direct, "Direct ")
    exec_with_time(user_input_array, decoding, letter_numbers_reverse, "Reverse")
    exec_with_time(user_input_array, decoding, letter_numbers_divide, "Divided")
    exec_with_time(user_input_array, decoding, letter_numbers_shifted, "Shifted")
else:
    print("String doesn't support")
