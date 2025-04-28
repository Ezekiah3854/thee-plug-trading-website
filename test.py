import bcrypt

password = "granton"
password = password.encode()
print(password)
encrypted_password = bcrypt.hashpw(password, bcrypt.gensalt(12))

print(encrypted_password)

new_password = "granton".encode()

print(bcrypt.checkpw(new_password, encrypted_password))