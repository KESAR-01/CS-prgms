import re

def is_valid_password(password):
    # Check the length condition
    if len(password) < 8:
        return False
    
    # Check if it contains at least one uppercase letter, one lowercase letter,
    # one digit, and one of the specified special characters
    if (re.search('[A-Z]', password) and 
        re.search('[a-z]', password) and 
        re.search(r'\d', password) and 
        re.search('[!@#$%&]', password)):
        return True
    
    return False

# Read passwords from a file
file_path = 'password.txt'  # Assuming the file extension is .txt

valid_passwords = []
invalid_passwords = []

try:
    with open(file_path, 'r') as file:
        for line in file:
            password = line.strip()  # Removes leading/trailing whitespaces
            if is_valid_password(password):
                valid_passwords.append(password)
            else:
                invalid_passwords.append(password)
except FileNotFoundError:
    print("File not found.")

# Print valid passwords
if valid_passwords:
    print("Valid Passwords:")
    for password in valid_passwords:
        print(password)
else:
    print("No valid passwords found.")

# Print invalid passwords
if invalid_passwords:
    print("\nInvalid Passwords:")
    for password in invalid_passwords:
        print(password)
