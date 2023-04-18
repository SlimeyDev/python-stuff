from cryptography.fernet import Fernet
import time

encryptedstr = input("Enter the encrypted byte string: ")
encryptedstr = bytes(encryptedstr, "utf-8")
key = input("enter the key: ")
key = bytes(key, "utf-8")

fernet = Fernet(key)

decstr = fernet.decrypt(encryptedstr)

#purely for the looks
print("Decrypting string [#      ]")
time.sleep(0.1)
print("Decrypting string [##     ]")
time.sleep(0.1)
print("Decrypting string [###    ]")
time.sleep(0.1)
print("Decrypting string [####   ]")
time.sleep(0.1)
print("Decrypting string [#####  ]")
time.sleep(0.1)
print("Decrypting string [#######]")
time.sleep(0.1)
print("Done")

print("Decrypted string: ", decstr)

input("Close application?(Type anything then press enter when you are ready): ")
print("closing...")
time.sleep(3)