##Conditional Statements(if, else, elif )
a = 10
b = 5
if (a > b):
    print(a, "Is Greater Than" , b) #OUTPUT: 10 Is Greater Than 5

if a == b:
    print("Both are Equal")
else:
    print("Both are Not Equal")
#OUTPUT: Both are Not Equal

x = int(input("Enter a Number: "))
if x > 0:
    print("The Number is Positive")
elif x == 0:
    print("The Number is Zero")
else:
    print("The Number is Negative")
#Sample INPUT 01: Enter a Number: -99
#OUTPUT: The Number is Negative
#Sample INPUT 02: Enter a Number: 80
#OUTPUT: The Number is Positive
#Sample INPUT 03: Enter a Number: 0
#OUTPUT: The Number is Zero

