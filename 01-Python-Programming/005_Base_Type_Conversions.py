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