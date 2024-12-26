import random
import string

def generate_random_password(length=8):
    character_set = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

user_length = input("Enter the desired password length (or press Enter for default 8): ")

if user_length.isdigit():
    length = int(user_length)
else:
    length = 8

random_password = generate_random_password(length)
print("Generated Random Password:", random_password)
