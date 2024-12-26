import hashlib

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password

password = input("Enter a password: ")
hashed_password = hash_password(password)
print("SHA-256 Hashed Password:", hashed_password)
