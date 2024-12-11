def add_redundant_bit(message):
    # Dictionary to map symbols to their binary codes
    symbol_to_code = {
        "A1": "00",
        "A2": "01",
        "A3": "10",
        "A4": "11",
        "A5": "100",
        "A6": "101"
    }

    # Convert the message into its binary representations
    binary_message = [symbol_to_code[symbol] for symbol in message]

    # Add the redundant bit to each symbol
    redundant_message = []
    for i, symbol in enumerate(binary_message):
        # Calculate the redundant bit as modulo 2 sum of all bits in the symbol
        redundant_bit = sum(int(bit) for bit in symbol) % 2
        # Append the redundant bit to the original binary representation
        new_symbol = symbol + str(redundant_bit)
        redundant_message.append(new_symbol)

    return redundant_message

message = ["A1", "A2", "A3", "A4", "A5", "A6"]

redundant_result = add_redundant_bit(message)
print("Redundant message M: ", redundant_result)