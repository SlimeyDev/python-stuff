print("Note: This is a billing system that is NOT made for commercial use.")
print("This Software is made to handle ONLY 5 PRODUCTS.")
print("Copyright (c) SlimeyDev All rights reserved")

GSTper = float(input("\nPlease type the percent of GST (type in numbers; Example: 18)\t"))

print("\n")

Product1 = str(input("Please type the name of product 1:\t"))
Quantity1 = int(input("Please type the quantity of product 1:\t"))
Price1 = float(input("Please type the price of product 1:\t"))

Total1 = Price1*Quantity1

Product2 = str(input("Please type the name of product 2:\t"))
Quantity2 = int(input("Please type the quantity of product 2:\t"))
Price2 = float(input("Please type the price of product 2:\t"))

Total2 = Price2*Quantity2

Product3 = str(input("Please type the name of product 3:\t"))
Quantity3 = int(input("Please type the quantity of product 3:\t"))
Price3 = float(input("Please type the price of product 3:\t"))

Total3 = Price3*Quantity3

Product4 = str(input("Please type the name of product 4:\t"))
Quantity4 = int(input("Please type the quantity of product 4:\t"))
Price4 = float(input("Please type the price of product 4:\t"))

Total4 = Price4*Quantity4

Product5 = str(input("Please type the name of product 5:\t"))
Quantity5 = int(input("Please type the quantity of product 5:\t"))
Price5 = float(input("Please type the price of product 5:\t"))

Total5 = Price5*Quantity5

totalBill = Total1+Total2+Total3+Total4+Total5

print(Total1, Total2, Total3, Total4, Total5)

GST = GSTper/100*totalBill
SES = 1/100*GST

totalBill = totalBill+GST+SES

print("="*50)
print("-"*20, "BILL", "-"*20)
print(Product1, "-"*15)
print("Quantity -", Quantity1, "\nPrice - ", Price1)
print("-"*50)
print(Product2, "-"*15)
print("Quantity -", Quantity2, "\nPrice - ", Price2)
print("-"*50)
print(Product3, "-"*15)
print("Quantity -", Quantity3, "\nPrice - ", Price3)
print("-"*50)
print(Product4, "-"*15)
print("Quantity -", Quantity4, "\nPrice - ", Price4)
print("-"*50)
print(Product5, "-"*15)
print("Quantity -", Quantity5, "\nPrice - ", Price5)
print("-"*50)
print("Total price with all taxes(", GSTper, "% GST and 1% SES): ", totalBill)
print("="*50)

print("\nSaving in text file Bill.txt, please wait...")

def main():
    f= open("Bill.txt","w+")

    toWrite ="="*50
    f.write(f"{toWrite}\n")
    toWrite = "-"*20+"BILL"+"-"*20
    f.write(f"{toWrite}\n")
    toWrite = Product1+"-"*15 
    f.write(f"{toWrite}\n")
    toWrite = "Quantity -"+str(Quantity1)+"\nPrice - "+str(Price1) 
    f.write(f"{toWrite}\n")
    toWrite = "-"*50
    f.write(f"{toWrite}\n")
    toWrite = Product2+"-"*15 
    f.write(f"{toWrite}\n")
    toWrite = "Quantity -"+str(Quantity2)+"\nPrice - "+str(Price2)
    f.write(f"{toWrite}\n")
    toWrite = "-"*50 
    f.write(f"{toWrite}\n")
    toWrite = Product3+"-"*15 
    f.write(f"{toWrite}\n")
    toWrite = "Quantity -"+str(Quantity3)+"\nPrice - "+str(Price3)
    f.write(f"{toWrite}\n")
    toWrite = "-"*50 
    f.write(f"{toWrite}\n")
    toWrite = Product4+"-"*15 
    f.write(f"{toWrite}\n")
    toWrite = "Quantity -"+str(Quantity4)+"\nPrice - "+str(Price4)
    f.write(f"{toWrite}\n")
    toWrite = "-"*50
    f.write(f"{toWrite}\n")
    toWrite = Product5+"-"*15 
    f.write(f"{toWrite}\n")
    toWrite = "Quantity -"+str(Quantity5)+"\nPrice - "+str(Price5)
    f.write(f"{toWrite}\n")
    toWrite = "-"*50 
    f.write(f"{toWrite}\n")
    toWrite = "Total price with all taxes("+str(GSTper)+"% GST and 1% SES): "+str(totalBill)
    f.write(f"{toWrite}\n")
    toWrite = "="*50 
    f.write(f"{toWrite}\n")

if __name__=="__main__":
    main()

print("Successfully saved bill in Bill.txt!")
print("WARNING: Any future bills will be overwriting the current content in the Bill.txt file!")

print("\nThank you for using Slimey Dev's Billing system!")