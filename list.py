list = ["hello", "bye", "no", "yes"]
#index  |0       |1     |2    |3   |

print("index 0")
print(list[0]) #printing index 0 which is hello
print("index 1")
print(list[1]) #printing index 1 which is bye
print("index 2")
print(list[2]) #printing index 2 which is no
print("index 3")
print(list[3]) #printing index 3 which is yes

print("index -1")
print(list[-1]) #printing index -1 which is bye
print("index -2")
print(list[-2]) #printing index -2 which is no
print("index -3")
print(list[-3]) #printing index -3 which is yes

print("printing the entire list")
print(list)

#length of the list
print(len(list))

#adding items to the list
list.append("item")

print("printing the entire list")
print(list)

#remove items from the list
list.remove("item") # you can also remove using the item index

print("printing the entire list")
print(list)

#the pop() function can also be used to remove items from the list
list.pop(1)

print("printing the entire list")
print(list)