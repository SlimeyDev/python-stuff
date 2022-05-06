import time

number = int(input("please enter the number to which you want to count to:\t"))
number = number+1

i = 0
while i<number:
    print(i)
    i = i+1
    time.sleep(.2)
