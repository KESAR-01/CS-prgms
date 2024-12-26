import requests
import hashlib
import csv

def check_password_breach(password):
    # Hash the password using SHA-1
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix, suffix = hashed_password[:5], hashed_password[5:]

    # Make a request to the "Have I Been Pwned" API
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)

    # Check if the suffix of the hash is present in the response
    return suffix in response.text

def main():
    # Read usernames and passwords from a file
    file_path = 'usernames_and_passwords.txt'  # Replace with your actual file path

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            username, password = row[0], row[1]

            # Check if the password has been breached
            if check_password_breach(password):
                print(f'Password for {username} has been breached!')
            else:
                print(f'Password for {username} is secure.')

if __name__ == "__main__":
    main()
