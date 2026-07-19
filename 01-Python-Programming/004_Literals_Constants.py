### THERE ARE MAINLY FIVE TYPES OF LITERALS IN PYTHON
"""
1.Integer Literals
2.Float Literals
3.Boolean Literals
4.Complex Literals
5.String Literals 

"""
##1.Integer Literals
#Direct integer valus like "200"
I1 = 12345678910 #Without underscore
I2 = 123_45_67_8910 #With underscores to enhance the readability
print(I1) #output: 12345678910
print(I2) #output: 12345678910
print(type(I1), type(I2)) #output: <class 'int'> <class 'int'>

"""
#Invalid integer literals
I3 = _1234
print(I3) #output: SyntaxError: invalid token

I4 = 12345_
print(I4) #output: SyntaxError: invalid token

"""

##2.Float Literals
#Direct float values like "3.14"
F1 = 3.14 #Without underscore
F2 = 3.1_4 #With underscores to enhance the readability
print(F1)
print(F2)
print(type(F1),type(F2))

"""
#Invalid Float Literals 
F3 = 54_._8
F4 = 3_6._8
print(F3) #output: invalid decimal literal
print(F4) #output: invalid decimal literal
"""

##3.Boolean Literals
#Direct True or False 
B1 = True
B2 = False
print(B1) #output 
print(B2)
print(type(B1),type(B2))

##4.Complex Literals
#Direct Complex Data types assigned to the variables
C1 = 4+9j
C2 = 8_5 + 10_3j
print(C1) #output: (4+9j)
print(C2) #output: (85+103j)
print(type(C1),type(C2)) #outout: <class 'complex'> <class 'complex'>

##5.String Literals
"""
It can be enclosed by :
Single Quotes ='  '
Double Quotes ="  "
Triple Quotes ="'  "'
"""
Name = 'Sangamesh'
Name1 = "Sangamesh MK"
Name2 = '"Sanagmesh M Kuri"'
print(Name) #output: Sangamesh
print(Name1) #output: Sangamesh MK
print(Name2) #output: "Sanagmesh M Kuri" #Here the python considered the inner double quotes as the part of the string and prints tghe output with the the double quotes.
print(type(Name)) #output: <class 'str'>