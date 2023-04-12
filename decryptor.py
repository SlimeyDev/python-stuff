from cryptography.fernet import Fernet
import time

encryptedstr = input("Enter the encrypted byte string: ")
key = input("Plese enter the key: ")
fernet = Fernet(key)

decstr = fernet.decrypt(encryptedstr).decode()
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