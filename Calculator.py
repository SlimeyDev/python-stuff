#i am inporting time module so i can use the code in line 11 if i dont import this them it will not work
import time

#setting the answer variable to 0 so it does not have a value before and messing up our calculation
answer = 0


#defines a function so i dont have to type this every time i want to do an operation
def print_answer():
    print("The",operation,"of",firstno," and ",seceondno," is")
    print("calculating.....")
    #if ur wondering wut this does, it just waits for 1 second and then moves on
    time.sleep(1)
    print (answer)

print("Welcome to Nesar's python calculator")

print("The avalible oparations are as follows - addition, subtraction, multiplication, division")

#takes in first number
firstno = int(input("please type the first number: "))
#takes in second number
seceondno = int(input("please type the seceond number: "))
#taks in the operation i want to do
operation = input ("What oparation do you want to perform? (Please enter in words)")

#checks if the operation is addition and does addition
if(operation == "addition"):
    answer = firstno + seceondno
    print_answer()

#checks if the operation is subtraction and does subtraction
elif(operation == "subtraction"):

    #if u know math then u know u cant subtract a big number from a small number unless u want minus values
    if(firstno < seceondno):
        answer = seceondno - firstno

    #same thing just checking stuff in the numbers        
    elif(seceondno < firstno):
        answer = firstno - seceondno
    print_answer()
    
#checks if the operation is multiplication and does multiplication
elif(operation == "multiplication"):
    answer = firstno * seceondno
    print_answer()

#checks if operation is division and does division
elif(operation == "division"):
    #same thing done for subtraction is done here
    if(firstno < seceondno):
        answer = seceondno/firstno

    elif(firstno > seceondno):
        answer = firstno/seceondno
    print_answer()
    
#if the operation input is not anyof these things above then it will say its invalid
else:
    print("'",operation,"'"+"is not a valid oeration, please check the spelling")


