from cryptography.fernet import Fernet
import time

message = input("Message: ")

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)

yn = input("Do you want to save this to a text file? (y/n): ")

if yn == "y":
    file = open("data.txt", "w")
    file.write("Message:", message, "\nencrypted message: ", encMessage)