a = input("Please enter a: ")
b = input("Please enter b: ")
c = input("Please enter c: ")

a_int = int(a, 2)
b_int = int(b, 2)
c_int = int(c, 2)

result = a_int ^ b_int ^ c_int ^ a_int ^ b_int
result_str = format(result, f'0{len(a)}b')

print(result_str)
