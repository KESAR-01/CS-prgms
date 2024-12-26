from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"jss college")
print("Encrypted message:", token)
decrypted_message = f.decrypt(token)
print("Decrypted message:", decrypted_message.decode())
