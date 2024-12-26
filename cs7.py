import itertools
import string

def bruteforce_attack(password):
    # Get all printable characters
    chars = string.printable.strip()  # We use printable characters without whitespace

    attempts = 0  # Initialize attempts counter

    # Try every possible combination of characters with lengths from 1 to the password length
    for length in range(1, len(password) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)  # Join the characters to form a string
            if guess == password:
                return (attempts, guess)  # Return the number of attempts and the cracked password
    
    return (attempts, None)  # Return the number of attempts and None if password is not cracked

# User input for the password to crack
password = input("Input the password to crack: ")

# Perform the brute force attack
attempts, guess = bruteforce_attack(password)

# Output the result
if guess:
    print(f"Password cracked in {attempts} attempts. The password is '{guess}'.")
else:
    print(f"Password not cracked after {attempts} attempts.")
