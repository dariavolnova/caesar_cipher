import argparse

def caesar_encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Encryption and Decryption")
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help="Choose action: 'encrypt' or 'decrypt'")
    parser.add_argument('message', type=str, help="The message to process")
    parser.add_argument('shift', type=int, help="The number of positions to shift in the cipher")

    args = parser.parse_args()

    if args.action == 'encrypt':
        encrypted_message = caesar_encrypt(args.message, args.shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif args.action == 'decrypt':
        decrypted_message = caesar_decrypt(args.message, args.shift)
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
