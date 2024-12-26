import rsa

def rsa_algo(password):
    (publickey, privatekey) = rsa.newkeys(256)
    print("Public Key:", publickey)
    print("Private Key:", privatekey)
    message = password.encode('utf8')
    ciphertext = rsa.encrypt(message, publickey)
    print("Ciphertext (Encrypted message):", ciphertext)
    decrypted_message = rsa.decrypt(ciphertext, privatekey)
    print("Decrypted message:", decrypted_message.decode('utf8'))
password = input("Input Your Text: ")
rsa_algo(password)
