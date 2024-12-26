import re

def is_valid_password(password):
    # Check the length condition
    if len(password) < 8:
        return False
    
    # Check if it contains at least one uppercase letter, one lowercase letter,
    # one digit, and one of the specified special characters
    if not (re.search(r'[A-Z]', password) and 
            re.search(r'[a-z]', password) and 
            re.search(r'\d', password) and 
            re.search(r'[!@#$%&]', password)):
        return False
    
    return True

# Example usage:
password = input("Enter a password: ")

if is_valid_password(password):
    print("Valid Password.")
else:
    print("Password does not meet requirements.")
