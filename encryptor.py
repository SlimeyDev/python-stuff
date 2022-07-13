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
    file.write("Message: ")
    file.write(message)
    file.write("\nencrypted message: ")
    file.write(str(encMessage))
    file.close()
    print("Saved to data.txt")
    print("closing...")
    time.sleep(2)
elif yn == "n":
    print("closing...")
    time.sleep(2)
else:
    print("Invalid response!")
    print("closing...")
    time.sleep(2)