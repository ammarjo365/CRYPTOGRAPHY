def caesar_cipher(text, shift, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()  # Check if it's uppercase
            char = char.lower()  # Convert to lowercase for easier manipulation
            char_code = ord(char)  # Get the ASCII code of the character
            if decrypt:
                char_code = ((char_code - ord('a') - shift) % 26) + ord('a')  # Decrypt
            else:
                char_code = ((char_code - ord('a') + shift) % 26) + ord('a')  # Encrypt
            if is_upper:  # If it was originally uppercase, convert it back
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            result += char_code
        else:
            result += char  # Keep non-alphabetical characters unchanged
    return result

# Input from the user
choice = input("Enter 'E' for encryption or 'D' for decryption: ").strip().upper()

if choice == 'E':
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (an integer): "))
    result = caesar_cipher(plaintext, shift)
    print("Encrypted Text:", result)
elif choice == 'D':
    ciphertext = input("Enter the text to decrypt: ")
    shift = int(input("Enter the shift value (an integer): "))
    result = caesar_cipher(ciphertext, shift, decrypt=True)
    print("Decrypted Text:", result)
else:
    print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
