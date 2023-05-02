def Collatz_Conjecture(x):
    list = []

    while not x == 1:
        if x%2 == 0:
            x = x/2
            list.append(x)
        else:
            x = (x*3)+1
            list.append(x)
        
    return list

num = int(input("Till what number do you want to brute force?\n"))

for n in range(1,num+1):
    value = Collatz_Conjecture(n)
    print(str(n)+":\t"+str(value)+"\n")
    n=+1