#Q3
# Write a program that asks the user to enter their marks and displays 
# their grade:
# • 90-100: A
# • 80-89: B
# • 70-79: C
# • 60-69: D
# • Below 60: F

marks=int(input("Enter Your Marks:"))
if 90<= marks <=100:
    print("Grade A")
elif 80<= marks <=89:
    print("Grade B")
elif 70<= marks <=79:
    print("Grade C")
elif 60<= marks <=69:
    print("Grade D")
else:
    print("Grade F")