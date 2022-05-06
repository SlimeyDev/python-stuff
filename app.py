rollNumber = int(input("Roll number:\t"))
name = str(input("Name:\t"))

# for i in range(5):
#     marks = input(f"Marks for subject {i+1}:\t")

#     global totalMarks
#     totalMarks = marks

marks1 = float(input("Marks for subject 1 out of 100:\t"))
marks2 = float(input("Marks for subject 2 out of 100:\t"))
marks3 = float(input("Marks for subject 3 out of 100:\t"))
marks4 = float(input("Marks for subject 4 out of 100:\t"))
marks5 = float(input("Marks for subject 5 out of 100:\t"))

totalMarks = marks1 + marks2 + marks3 + marks4 + marks5
percentOfMarks = round(totalMarks/500*100, 2)

print("="*50)
print(f"Name: {name}")
print(f"Roll number: {rollNumber}")
print("-"*50)
print(f"Marks in subject 1: {marks1}")
print(f"Marks in subject 2: {marks2}")
print(f"Marks in subject 3: {marks3}")
print(f"Marks in subject 4: {marks4}")
print(f"Marks in subject 5: {marks5}")
print("-"*50)
print(f"total marks: {totalMarks}")
print(f"percentage of total marks: {percentOfMarks}")
print("="*50)