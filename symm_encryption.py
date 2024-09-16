import argparse
from encryption import decryption, encryption, generate_roundkey

def main():
    # CLI argument parser setup
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a given string using a custom encryption algorithm.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the input string')
    group.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the input string')
    parser.add_argument('input_string', type=str, help='The string to encrypt or decrypt')
    #parser.add_argument('--key', type=str, required=True, help='The encryption/decryption key')
    #parser.add_argument('--rounds', type=int, default=3, help='Number of rounds for encryption/decryption (default: 3)')

    args = parser.parse_args()

    input_string = args.input_string
    #key = args.key if args.key else '0111001010001001'
    #rounds = args.rounds if args.rounds else 3
    key = '0111001010001001'
    rounds=3

    if args.encrypt:
        print(f"Encrypting the input: '{input_string}'")
        encrypted_val = encryption(input_string, key, rounds)
        print("Encrypted value:")
        print( "'",encrypted_val, "'")
    elif args.decrypt:
        print(f"Decrypting the input: '{input_string}'")
        decrypted_val = decryption(input_string, key, rounds)
        print(f"Decrypted value: '{decrypted_val}'")

if __name__ == "__main__":
    main()
