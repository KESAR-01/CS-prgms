def decrypt(ciphertext, shift):
    result = ""

    for char in ciphertext:
        if char.isalpha():
            # Determine the case of the character (uppercase or lowercase)
            if char.isupper():
                result += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            # If the character is not a letter, keep it unchanged
            result += char

    return result

def brute_force_decrypt(ciphertext):
    for shift in range(1, 26):
        decrypted_text = decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

def main():
    # Get input from the user
    ciphertext = input("Enter the ciphertext to hack: ")

    # Brute-force decryption
    brute_force_decrypt(ciphertext)

if __name__ == "__main__":
    main()
