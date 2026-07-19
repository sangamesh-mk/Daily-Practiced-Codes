### Base Conversions 
"""
1.bin()
2.oct()
3.hex()
"""

##1.bin() : Converts the any other base types to the Binary data type(Base 2)
#FOR INTEGERS
B1 = 8
B2 = bin(B1)
print(B2) #OUTPUT: 0b1000 (Zero b 1000)
print(type(B2)) #OUTPUT: <class 'str'>

B3 = 99
print(bin(B3)) #OUTPUT: 0b1100011

#FOR BOOLEAN 
Bool1 = True
Bool2 = False
print(bin(Bool1)) #OUTPUT: 0b1
print(bin(Bool2)) #OUTPUT: 0b0


##2.oct() : Converts the any other base types to the octal data type(Base 8)
#FOR INTEGERS
O1 = 8
O2 = oct(O1)
print(O2) #OUTUT: 0o10 (Zero o 1 0)
print(type(O2)) #OUTPUT: <class 'str'>

O3 = 99
O4 = oct(O3)
print(O4) #OUTPUT: 0o143
print(type(O4)) #OUTPUT: <class 'str'>

#FOR BOOLEAN 
Bool11 = True
Bool22 = False
print(oct(Bool11)) #OUTPUT: 0o1
print(oct(Bool22)) #OUTPUT: 0o0


##3.hex() : Converts the any other base types to the Hexadecimal data type(Base 16)
#FOR INTEGERS
H1 = 8
H2 = hex(H1)
print(H2) #OUTPUT: 0x8 (Zero x 8)
print(type(H2)) #OUTPUT: <class 'str'>

H3 = 99
H4 = hex(H3)
print(H4) #OUTPUT: 0x63
print(type(H4)) #OUTPUT: <class 'str'>

#FOR BOOLEAN 
Bool111 = True
Bool222 = False
print(hex(Bool111)) #OUTPUT: 0x1
print(hex(Bool222)) #OUTPUT: 0x0

"""
For FLOATS :-
F1 = 12.5
B4 = bin(F1)
O5 = oct(F1)
H5 = hex(F1)

print(B4) #OUTPUT:  TypeError: 'float' object cannot be interpreted as an integer
print(O5) #OUTPUT:  TypeError: 'float' object cannot be interpreted as an integer
print(H5) #OUTPUT:  TypeError: 'float' object cannot be interpreted as an integer
"""

### TYPE CONVERSIONS 
"""
1.int()
2.float()
3.bool()
4.complex()
5.str()
"""

##1. int() 
#Converts any other data types into INTEGER DATA TYPE
F1 = 12.95
Int1 = int(F1)
print(Int1) #OUTPUT: 12
print(type(F1)) #OUTPUT: <class 'float'>
print(type(Int1)) #OUTPUT: <class 'int'>

B1 = True 
Int2 = int(B1)
print(Int2) #OUTPUT: 1
print(type(B1)) #OUTPUT: <class 'bool'>
print(type(Int2)) #OUTPUT: <class 'int'>

S1 = "090"
Int3 = int(S1)
print(Int3) #OUTPUT: 90
print(type(S1)) #OUTPUT: <class 'str'>
print(type(Int3)) #OUTPUT: <class 'int'>

Binary_String = "0b1010"
Int4 = int(Binary_String,2)
#WE NEED TO MENTION THE BASE VALUE AFTER THE VARIABLE NAME 
#THAT STORES THE BASE FORM DATA TYPE LIKE (Base=2,Hexa=16 and Oct=8)
print(Int4) #OUTPUT: 10
print(type(Binary_String)) #OUTPUT: <class 'str'>
print(type(Int4)) #OUTPUT: <class 'int'>


##2.float()
#Converts any other data types into FLOAT DATA TYPES 
I1 = 80
Float1 = float(I1)
print(Float1) #OUTPUT: 80.0
print(type(I1)) #OUTPUT: <class 'int'>
print(type(Float1)) #OUTPUT: <class 'float'>

B1 = True
Float2 = float(B1)
print(Float2) #OUTPUT: 1.0
print(type(B1)) #OUTPUT: <class 'bool'>
print(type(Float2)) #OUTPUT: <class 'float'>

S1 = "99.9"
Float3 = float(S1)
print(Float3) #OUTPUT: 99.9
print(type(S1)) #OUTPUT: <class 'str'>
print(type(Float3)) #OUTPUT: <class 'float'>


##3.bool()
#Converts any other data types into the BOOLEAN DATA TYPE
I1 = 99
Bool1 = bool(I1)
print(Bool1) #OUTPUT: True
print(type(I1)) #OUTPUT: <class 'int'>
print(type(Bool1)) #OUTPUT: <class 'bool'>

#The bool() Function always gives TRUE , Except these THREE Cases:

Case1 = False
Bool2 = bool(Case1)
print(Bool2) #OUTPUT: False
print(type(Case1)) #OUTPUT: <class 'bool'>
print(type(Bool2)) #OUTPUT: <class 'bool'>

Case2 = 0
Bool3 = bool(Case2)
print(Bool3) #OUTPUT: False
print(type(Case2)) #OUTPUT: <class 'int'>
print(type(Bool3)) #OUTPUT: <class 'bool'>

Case3 = ""
Bool4 = bool(Case3)
print(Bool4) #OUTPUT: False
print(type(Case3)) #OUTPUT: <class 'str'>
print(type(Bool4)) #OUTPUT: <class 'bool'>


##4.complex()
#Converts any other data types into COMPLEX DATA TYPE
I1 = 100
Complex1=  complex(I1)
print(Complex1) #OUTPUT: (100+0j)
print(type(I1)) #OUTPUT: <class 'int'>
print(type(Complex1)) #OUTPUT: <class 'complex'>

F1 = 90.50
Complex2 = complex(F1)
print(Complex2) #OUTPUT: (90.5+0j)
print(type(F1)) #OUTPUT: <class 'float'>
print(type(Complex2)) #OUTPUT: <class 'complex'>

B1 = True
Complex3 = complex(B1)
print(Complex3) #OUTPUT: (1+0j)
print(type(B1)) #OUTPUT: <class 'bool'>
print(type(Complex3)) #OUTPUT: <class 'complex'>

S1 = "55"
Complex4 = complex(S1)
print(Complex4) #OUTPUT: (55+0j)
print(type(S1)) #OUTPUT: <class 'str'>
print(type(Complex4)) #OUTPUT: <class 'complex'>


##5.str()
#Converts any other other data types into STRINGS DATA TYPE just by adding quotes
I1 = 909
Str1 = str(I1) 
print(Str1) #OUTPUT: 909
print(type(I1)) #OUTPUT: <class 'int'>
print(type(Str1)) #OUTPUT: <class 'str'>

F1 = 78.8
Str2 = str(F1)
print(Str2) #OUTPUT: 78.8
print(type(F1)) #OUTPUT: <class 'float'>
print(type(Str2)) #OUTPUT: <class 'str'>

B1 = True
Str3 = str(B1)
print(Str3) #OUTPUT: True
print(type(B1)) #OUTPUT: <class 'bool'>
print(type(Str3)) #OUTPUT: <class 'str'>

C1 = 4+9j
Str4 = str(C1)
print(Str4) #OUTPUT: (4+9j)
print(type(C1)) #OUTPUT: <class 'complex'>
print(type(Str4)) #OUTPUT: <class 'str'>