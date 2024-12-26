def encrypt(text, shift):
    result = ""  # Initialize the result as an empty string
    
    for char in text:
        if char.isalpha():
            # Determine the case of the character (uppercase or lowercase)
            if char.isupper():
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            # If the character is not a letter, keep it unchanged
            result += char
    
    return result

def decrypt(ciphertext, shift):
    # Decryption is the same as encryption with a negative shift
    return encrypt(ciphertext, -shift)

def main():
    # Get input from the user
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))

    # Encrypt the input text
    ciphertext = encrypt(plaintext, shift)
    print("Encrypted text:", ciphertext)

    # Decrypt the encrypted text
    decrypted_text = decrypt(ciphertext, shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
