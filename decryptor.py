from cryptography.fernet import Fernet
import time

encryptedstr = input("Enter the encrypted byte string: ")
key = input("Plese enter the key: ")
fernet = Fernet(key)

print("Decrypting string [-      ]")
time.sleep(0.1)
print("Decrypting string [--     ]")
time.sleep(0.1)
print("Decrypting string [---    ]")
time.sleep(0.1)
print("Decrypting string [----   ]")
time.sleep(0.1)
print("Decrypting string [-----  ]")
time.sleep(0.1)
print("Decrypting string [-------]")
time.sleep(0.1)
print("Done")

decstr = fernet.decrypt(encryptedstr).decode()
print("Decrypted string: ", decstr)