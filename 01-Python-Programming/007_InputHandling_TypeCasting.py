## INPUT HANDLING :

Name = input("Enter your Name : ")
UserName = Name
print("Welcome to Matured Mind, ", UserName) 
#Sample Input : Enter your Name : SANGAMESH MK
#OUTPUT: Welcome to Matured Mind,  SANGAMESH MK
print(type(UserName)) #OUTPUT: <class 'str'>

StudentName = input("Enter the Student Name: ")
FatherName = input("Enter His/Her Father Name: ")
MotherName = input("Enter His/Her Mother Name: ")
print(StudentName + " " + "is a Student and His/Her Father Name is " + " " + FatherName + " " + "And His/Her Mother Name is " + MotherName )
#Sample Input :
"""
Enter the Student Name: Sangamesh MK
Enter His/Her Father Name: Mallappa
Enter His/Her Mother Name: Anusuya
"""
#OUTPUT: Sangamesh MK is a Student and His/Her Father Name is  Mallappa And His/Her Mother Name is Anusuya


## TYPE CASTING
#Converting the input string to our needed data type
Name1 = input("Enter your Name: ")
Age = input("Enter your Age: ")
print(Name1)
print(Age)
print(type(Name1)) #OUTPUT: <class 'str'>
print(type(Age)) #OUTPUT: <class 'str'> (Here the input always gives the string type)
#Sample Input :
"""
Enter your Name: sangamesh mk
Enter your Age: 20
"""
#OUTPUT: sangamesh mk
#OUTPUT: 20

NameOfStudent = input("Enter the student's Name: ")
AgeOfStudent = int(input("Enter the age of the student: "))
PhyScore = int(input("Enter the Score of the Physics : "))
ChemScore = int(input("Enter the Score of the Chemistry : "))
MathsScore = int(input("Enter the Score of the Mathematics: "))
BioScore = int(input("Enter the Score of the Biology: "))
TotalScore = PhyScore + ChemScore + MathsScore + BioScore
Percent = (TotalScore / 400) * 100
print(NameOfStudent ," is ", AgeOfStudent ," Years Old  and He Scored " ,TotalScore ," and His Percentage is " ,Percent ) 

#Sample Input :
"""
Enter the student's Name: Sangamesh MK
Enter the age of the student: 20
Enter the Score of the Physics : 80
Enter the Score of the Chemistry : 85
Enter the Score of the Mathematics: 90
Enter the Score of the Biology: 95
"""
#OUTPUT: Sangamesh MK  is  20  Years Old  and He Scored  350  and His Percentage is  87.5