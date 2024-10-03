print("**** CAESAR CIPHER PROGRAM ***")
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around the alphabet
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += char
    return encrypted_text

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        action = input("Would you like to (e)ncrypt or (d)ecrypt a message? (or 'q' to quit): ").lower()
        if action == 'q':
            print("Goodbye!")
            break
        elif action not in ('e', 'd'):
            print("Invalid option. Please choose 'e' for encrypt or 'd' for decrypt.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (positive for encrypt, negative for decrypt): "))

        if action == 'e':
            result = caesar_cipher(message, shift)
            print(f"Encrypted message: {result}")
        elif action == 'd':
            result = caesar_cipher(message, -shift)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
