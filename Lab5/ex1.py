# calculate (base^exp) % mod
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Given secret keys for the transmitter and receiver
transmitter_secret_key = 6
receiver_secret_key = 3

base_1 = 2
modulus_1 = 4

base_2 = 78
modulus_2= 33

# Calculate the public keys
transmitter_public_key_1 = mod_exp(base_1, transmitter_secret_key, modulus_1)
receiver_public_key_1 = mod_exp(base_1, receiver_secret_key, modulus_1)

transmitter_public_key_2 = mod_exp(base_2, transmitter_secret_key, modulus_2)
receiver_public_key_2 = mod_exp(base_2, receiver_secret_key, modulus_2)

# Calculate the shared secret key
shared_key_transmitter_1 = mod_exp(receiver_public_key_1, transmitter_secret_key, modulus_1)
shared_key_receiver_1 = mod_exp(transmitter_public_key_1, receiver_secret_key, modulus_1)

shared_key_transmitter_2 = mod_exp(receiver_public_key_2, transmitter_secret_key, modulus_2)
shared_key_receiver_2 = mod_exp(transmitter_public_key_2, receiver_secret_key, modulus_2)

# Output results
print("2^x(mod4)")
print("Transmitter's public key:", transmitter_public_key_1)
print("Receiver's public key:", receiver_public_key_1)
print("Shared key calculated by transmitter:", shared_key_transmitter_1)
print("Shared key calculated by receiver:", shared_key_receiver_1)

print("\n78^x(mod33)")
print("Transmitter's public key:", transmitter_public_key_2)
print("Receiver's public key:", receiver_public_key_2)
print("Shared key calculated by transmitter:", shared_key_transmitter_2)
print("Shared key calculated by receiver:", shared_key_receiver_2)