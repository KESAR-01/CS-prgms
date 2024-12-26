import base64

# Take input from the user
sample_string = input("Enter your text: ")

# Convert the string to bytes
sample_string_bytes = sample_string.encode("ascii")

# Encode the bytes using Base64
base64_bytes = base64.b64encode(sample_string_bytes)

# Convert the Base64 bytes back to a string
base64_string = base64_bytes.decode("ascii")

# Print the encoded Base64 string
print(f"Encoded string: {base64_string}")

# Now, decode the Base64 string back to the original text

# Convert the Base64 string to bytes
base64_bytes = base64_string.encode("ascii")

# Decode the Base64 bytes
sample_string_bytes = base64.b64decode(base64_bytes)

# Convert the bytes back to the original string
sample_string = sample_string_bytes.decode("ascii")

# Print the decoded string
print(f"Decoded string: {sample_string}")
