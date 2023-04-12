from cryptography.fernet import Fernet
import time

message = input("Message: ")

key = Fernet.generate_key()
print("key: ", key)

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("\n")
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

yn = input("Do you want to save this to a text file? (y/n): ")

if yn == "y":
    file = open("data.txt", "w")
    file.write("Message: ")
    file.write(message)
    file.write("\nencrypted message: ")
    file.write(str(encMessage))
    file.write("\n")
    file.write("key: ")
    file.write(key)
    file.close()
    print("Saved to data.txt")
    print("closing...")
    time.sleep(3)
elif yn == "n":
    print("closing...")
    time.sleep(3)
else:
    print("Invalid response!")
    time.sleep(1)
    print("closing...")
    time.sleep(3)