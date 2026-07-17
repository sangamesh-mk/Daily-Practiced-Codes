#declaration and initialization of variables

Name = "Sangamesh M Kuri"
print(Name) #output: Sangamesh M Kuri
 #Here, The variable Name is declared and initialized with the value "Sangamesh M Kuri" and then printed to the console.
 
Age = 20
print(Age) #output: 20
#Here, The variable Age is declared and initialized with the value 20 and then printed to the console.

#We can declare multple variables in a single line as shown below.
a,b,c = 10,20,30
print(a) #output: 10
print(b) #output: 20
print(c) #output: 30
print(a,b,c) #output: 10 20 30

Name,Price,Qty = "Books",20.50,5
print(Name) #output: Books
print(Price) #output: 20.5
print(Qty) #output: 5
print(Name,Price,Qty) # output: Books 20.5 5

#To know the data type of a variable we can use the type() function as shown below.
print(type(Name)) #output: <class 'str'>
print(type(Price)) #output: <class 'float'>
print(type(Qty)) #output: <class 'int'>

#We can also declare multiple variables with the same value in a single line as shown below.
X,Y,Z = 10,10,10
print(X) #output: 10
print(Y) #output: 10
print(Z) #output: 10
print(X,Y,Z) #output: 10 10 10

#OR

A=B=C = 10
print(A) #output: 10
print(B) #output: 10
print(C) #output: 10
print(A,B,C) #output: 10 10 10

# ALSO WE KNOW THAT : IF THE MULTIPLE VARIABLES HAS SAME DATA(VALUE) , THE COMPUTER ALLOCATES THE SAME SINGLE MEMORY SPACE.HOW???
print(A) #output: 10
print(B) #output: 10
print(C) #output: 10

print(id(A)) #output: 140711234567456
print(id(B)) #output: 140711234567456
print(id(C)) #output: 140711234567456
# As we can see the memory address of A,B,C is same because they are pointing to the same value 10.

# Also we can UPDATE the value of the Variables by Reassigning the value to the variable as shown below.
A = 100
print(A) #output: 100
print(id(A)) #output: 140711234567456

A = 1500
print(A) #output: 1500
print(id(A)) #output: 2141385241072

# SWAPPING 
Name1 = "Sangamesh"
Name2 = "M Kuri"
print("Before Swapping :" , Name1, Name2) #output: Before Swapping : Sangamesh M Kuri

Name1, Name2 = "M Kuri", "Sangamesh"
print("After Swapping : ", Name1, Name2) #output: After Swapping :  M Kuri Sangamesh