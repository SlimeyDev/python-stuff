x = int(input("enter an integer: "))

while not x == 1:
    if x%2 == 0:
        x = x/2
        print(x)
    else:
        x = (x*3)+1
        print(x)