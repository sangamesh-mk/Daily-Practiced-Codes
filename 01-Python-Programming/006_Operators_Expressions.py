### OPERATORS
##1. Arithmetic Operators: +,-,*,/,//,%.**
A = 10
B = 20
Add = A + B
Sub = A - B
Mult = A * B
Div = A / B
FloorD = A // B
Mod = A % B
Expon = A ** B

print("Addition : ", Add) #OUTPUT: Addition :  30
print("Subtraction : ", Sub) #OUTPUT: Subtraction :  -10
print("Multiplication : ", Mult) #OUTPUT: Multiplication :  200
print("Division : ", Div) #OUTPUT: Division :  0.5
print("Floor Division : " ,FloorD) #OUTPUT: Floor Division :  0
print("Modulus : ", Mod) #OUTPUT: Modulus :  10
print("Exponent : ", Expon) #OUTPUT: Exponent :  100000000000000000000

## STRING CONCATENATION(Joining(+)of Two strings) And STRING REPETATION(Repeating(*)strings n times)

# STRING CONCATENATION(+)
First_String = "Sangamesh"
Second_String = "M Kuri"
Joined_String = First_String + " " + Second_String
print(Joined_String) #OUTPUT: Sangamesh M Kuri

FirstString = "1VW25CompSci"
SecondString = "090"
FinalString = FirstString + SecondString
print(FinalString) #OUTPUT: 1VW25CompSci090

FirstString = "1VW25CompSci"
SecondString = str(90)
FinalString = FirstString + SecondString
print(FinalString) #OUTPUT: 1VW25CompSci90

Name = input("Enter Your Name: ")
TotalMarks = int(input("Enter the Total Marks: "))
ObtainedMarks = int(input("Enter your Marks: "))
print(Name + " Scored " , ObtainedMarks , " Out of ", TotalMarks) 
#Sample INPUT: 
"""
Enter Your Name: Sangamesh M Kuri
Enter the Total Marks: 600
Enter your Marks: 550
"""
#OUTPUT: Sangamesh M Kuri Scored  550  Out of  600

# STRING REPETATION(*)

String1 = "Sangamesh\n"
RepString = String1 * 5
print(RepString)
#OUTPUT: 
"""
Sangamesh
Sangamesh
Sangamesh
Sangamesh
Sangamesh
"""
String1 = "Sangamesh\t"
RepString = String1 * 5
print(RepString)
#OUTPUT: Sangamesh       Sangamesh       Sangamesh       Sangamesh       Sangamesh


### EXPRESSIONS 
Expr = 2 + 88 * 100 - 9 / 2
print("The Result is : ", Expr) #OUTPUT: The Result is :  8797.5

Expr1 = (5 + 98) * 20 / 55 
print("The Total Result : ", Expr1) #OUTPUT: The Total Result :  37.45454545454545
print(round(Expr1)) #OUTPUT:37

import math
print(math.sqrt(Expr1)) #OUTPUT: 6.120011883529758


##2. Relational Operators: <,>,<=,>=,==,!=
a = 10
b = 22
c = 8
d = a < b
print(d) #OUTPUT: True
e = b <= a
print(e) #OUTPUT: False
f = a > c
print(f) #OUTPUT: True
g = b >= c
print(g) #OUTPUT: True
h = a == b
print(h)  #OUTPUT: False
i = a != b
print(i) #OUTPUT: True

#String Comparision(Relational Operators)
#Lexicographic Order
StrComp1 = "Apple" < "Apply"
print(StrComp1) #OUTPUT: True

StrComp2 = "Attachment" > "Attach"
print(StrComp2) #OUTPUT: True

StrComp3 = "Ram" > "Ravana"
print(StrComp3) #OUTPUT: False

StrComp4 = "Dhuryodhana" > "Bheema"
print(StrComp4) #OUTPUT: True

StrComp5 = "90Sons" < "OneDaughter"
print(StrComp5) #OUTPUT: True

print("#Python" < "Python") #OUTPUT: True

##3. Logic Operators: and,or,not
u = 1
v = 0
w = 20
x = 5
y = 9
z = 20

A = x!=y and w == z
print(A) #OUTPUT: True
B = v < u or v >= z
print(B) #OUTPUT: True
C = not z
print(C) #OUTPUT: False

#Non-Boolean Conditions in Logical Operations
#For AND Operator,
"""
Returns the SECOND operand ,if the first operand is TRUE(operand is not 0 or any false values)
Returns the FIRST operand, if the first operand is FALSE(operand is 0 or any false values)
"""

print(w and x) #OUTPUT: 5
print(20 and 5) #OUTPUT: 5
print(5 and 20)  #OUTPUT: 20

#For OR Operator,
"""
Returns the FIRST operand ,if the first operand is TRUE(operand is not 0 or any false values)
Returns the SECOND operand, if the first operand is FALSE(operand is 0 or any false values)
"""

print(w or x) #OUTPUT: 20
print(20 or x) #OUTPUT: 20
print(x or y) #OUTPUT: 5
print(y or x) #OUTPUT: 9

#For NOT Operator,TRUE will be the Output for 0 and FALSE for all the other VALUES.
print(not w) #OUTPUT: False
print(not x) #OUTPUT: False
print(not z) #OUTPUT: False
print(not u) #OUTPUT: False
print(not v) #OUTPUT: True
print(not 1) #OUTPUT: False

##4. Assignment Operators: =,+=,-=,*=,/=,%=,**=,//=
X = 15 # 15 is ASSIGNING to X
Y = 90
Z = 4

X += X
print(X) #OUTPUT: 30
X += Y
print(X)  #OUTPUT: 120 (X=30 and Y=90 X+Y=120)
Z -= 1
print(Z) #OUTPUT: 3
X *= Y
print(X) #OUTPUT: 10800


##5. Identity Operators: is,is not
A = 25
B = 25
print(A == B) #OUTPUT: True
print(A is B) #OUTPUT: True
print(A is not B) #OUTPUT: False

a = [1,2,3]
b = [1,2,3]
print(a == b) #OUTPUT: True
print(a is b) #OUTPUT: False
print(a is not b) #OUTPUT: True

x = 100
y = 1000
print(x is b) #OUTPUT: False
print(x is not y) #OUTPUT: True


##6. Bitwise Operators: &,|,^,~,<<,>>
#AND(&) OPERATOR
a = 10 #1010
b = 15 #1111
print(a & b) #OUTPUT: 10 (1010)
print(format(a ,"b")) #OUTPUT: 1010 (without prefix 0b)
print(bin(a)) #OUTPUT: 0b1010 (with prefix)
print(a.bit_length()) #OUTPUT: 4 (Length of the Bit)

#OR(|) OPERATOR
A = 5
B = 8
print(A | B) #OUTPUT: 13
print(format(A, "b")) #OUTPUT: 101
print(bin(A)) #OUTPUT: 0b101
print(A.bit_length()) #OUTPUT: 3

#XOR(^) OPERATOR
x = 10
y = 8
print(x ^ y) #OUTPUT: 2
print(format(x, "b")) #OUTPUT: 1010
print(bin(x)) #OUTPUT: 0b1010
print(bin(y)) #OUTPUT: 0b1000
print(x.bit_length()) #OUTPUT: 4


#Complement(~) OPERATOR
X = 6
Y = 30
print(~X) #OUTPUT: -7
print(~Y) #OUTPUT: -31

#Left Shift(<<)
p = 9
q = 4
print(p << 1) #OUTPUT: 18 (p * 2 ** 1 = 9 * 2**1)
print(q << 3) #OUTPUT: 32 (q * 2 ** 3 = 4 * 2 ** 3)
print(format(p , "b")) #OUTPUT: 1001

#Right Shift(>>)
P = 4
Q = 8
print(P >> 1) #OUTPUT: 2 (P // 2 ** 1 = 4 // 2 ** 1)
print(Q >> 3) #OUTPUT: 1 (Q // 2 ** 3 = 8 // 2 ** 3)