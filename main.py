from encryption import decryption, encryption, generate_roundkey


input_string: str = "Ein zu verschlüsselnder Testsatz!"
key='0111001010001001' #keylength? 

rounds=3

print(f"input val: '{input_string}'; length: {len(input_string)}")
print(f"key: '{key}; keylength: {len(key)}'")

encrypted_val = encryption(input_string, key, rounds)
print("encrypted val:'", encrypted_val, "'")

decrypted_val = decryption(encrypted_val, key, rounds)
print(f"decrypted val: '{decrypted_val}'\n")


# print(f"Lengths - Original: {len(input_string)}, Encrypted: {len(encrypted_val)}, Decrypted: {len(decrypted_val)}")

print(f"Original input (repr): {repr(input_string)}")
print(f"Decrypted value (repr): {repr(decrypted_val)}")



assert decrypted_val == input_string