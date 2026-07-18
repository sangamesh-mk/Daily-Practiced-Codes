# NUMERIC DATA TYPES 
# 01: INTEGER DATA TYPE 
# 02: FLOAT DATA TYPE 
# 03: BOOLEAN DATA TYPE 
# 04: COMPLEX DATA TYPE 

## 01: INTEGER DATA TYPE
# Integer data type is used to represent whole numbers without any decimal point.
#In Python, integers can be positive, negative, or zero. They are represented by the 'int' class.
# Example of integer data type: 
I1 = 10
I2 = -22
I3 = 0
print(I1,I2,I3) #OUTPUT: 10 -22 0
print(type(I1)) #OUTPUT: <class 'int'>
print(type(I2)) #OUTPUT: <class 'int'>
print(type(I3)) #OUTPUT: <class 'int'>

#WE CAN CHECK THE SIZE OF INTEGER DATA TYPE USING sys.getsizeof() FUNCTION
import sys
print(sys.getsizeof(I1)) #OUTPUT: 28
print(sys.getsizeof(I2)) #OUTPUT: 28
print(sys.getsizeof(I3)) #OUTPUT: 28

#WE CAN ALSO CHECK THE MEMORY ADDRESS OF INTEGER DATA TYPE USING id() FUNCTION
print(id(I1)) #OUTPUT:140733349283224)  
print(id(I2)) #OUTPUT:140733349283160)
print(id(I3)) #OUTPUT:140733349283096)  

## 02: FLOAT DATA TYPE
# Float data type is used to represent decimal numbers. In Python, floats are represented by the 'float' class.
F1 = 10.50 
F2 = -22.85
F3 = 0

#We can also represent float numbers in scientific notation using 'e' or 'E' to indicate the power of 10.
F4 = 2.3E2 # 2.3 * 10^2
F5 = -3.14e-22 # -3.14 * 10^-22
F6 = 22.99E-8 # 22.99 * 10^-8
F7 = -33.87e4 # -33.87 * 10^4
print(F1,F2,F3,F4,F5,F6,F7) #OUTPUT: 10.5 -22.85 0 230.0 -3.14e-22 2.299e-07 -3387000.0
print(type(F1),type(F2),type(F3),type(F4),type(F5),type(F6),type(F7))
#OUTPUT: <class 'float'> <class 'float'> <class 'float'> <class 'float'> <class 'float'> <class 'float'> <class 'float'>

## 03: BOOLEAN DATA TYPE
# Boolean data type is used to represent truth values. In Python, booleans are represented by the 'bool' class.
x = True
y = False
print(x,y) #OUTPUT: True False

print(int(x)) #OUTPUT: 1
print(int(y)) #OUTPUT: 0

#WE CAN USE THE BOOLEAN DATA TYPE IN CONDITIONAL STATEMENTS
a = 10
b = 99
c = (a>b)
print(c) #OUTPUT: False
d = (a<b)
print(d) #OUTPUT: True


## 04: COMPLEX DATA TYPE
# Complex data type is used to represent complex numbers. In Python, complex numbers are represented by the 'complex' class.
C1 = 2 + 3j
C2 = -2 + 5j
C3 = 8 - 9j
C4 = 2.1 + 8j
C5 = 9 - 9.0j  

#We can also create complex numbers using the complex() function, which takes two arguments: the real part and the imaginary part.
C6 = complex(2,5) # Creates a complex number with real part 2 and imaginary part 5
C7 = complex(99) # Creates a complex number with real part 99 and imaginary part 0
C8 = complex(22.5, 33.7)  # Creates a complex number with real part 22.5 and imaginary part 33.7
C9 = complex(-22.5, -33.7)  # Creates a complex number with real part -22.5 and imaginary part -33.7

print(C1,C2,C3,C4,C5,C6,C7,C8,C9) #OUTPUT: (2+3j) (-2+5j) (8-9j) (2.1+8j) (9-9j) (2+5j) (99+0j) (22.5+33.7j) (-22.5-33.7j)
print(type(C1)) #OUTPUT: <class 'complex'>
print(type(C2)) #OUTPUT: <class 'complex'>
print(type(C3)) #OUTPUT: <class 'complex'>
print(type(C4)) #OUTPUT: <class 'complex'>
print(type(C5)) #OUTPUT: <class 'complex'>
print(type(C6)) #OUTPUT: <class 'complex'>
print(type(C7)) #OUTPUT: <class 'complex'>
print(type(C8)) #OUTPUT: <class 'complex'>
print(type(C9)) #OUTPUT: <class 'complex'>

