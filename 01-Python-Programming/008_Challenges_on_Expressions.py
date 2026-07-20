## AREA OF RECTANGLE
Length = float(input("Enter the Length of the Rectangle: "))
Breadth = float(input("Enter the Breadth of the Rectangle: "))
Area = Length * Breadth
print("The Total area of the Rectangle is ", Area)
#Sample Input: 
"""
Enter the Length of the Rectangle: 10
Enter the Breadth of the Rectangle: 5
"""
#OUTPUT: The Total area of the Rectangle is  50.0

## AREA OF THE TRIANGLE
Base = float(input("Enter the Base of the Triangle: "))
Heigth = float(input("Enter the Heigth of the triangle: "))
Area = (Base * Heigth)/2
print("The Total area of the triangle is ", Area)
#Sample Input: 
"""
Enter the Base of the Triangle: 9
Enter the Heigth of the triangle: 5
"""
#OUTPUT: The Total area of the triangle is  22.5

## AREA OF THE TRAPEZIUM 
Side1 = float(input("Enter the Side 1 of the Trapezium: "))
Side2 = float(input("Enter the Side 2 of the Trapezium: "))
Heigth = float(input("Enter the Heigth of the Trapzium: "))
Area = ((Side1 + Side2)*Heigth)/2
print("The Total Area of the Trapezium is ", Area)
#Sample Input: 
"""
Enter the Side 1 of the Trapezium: 7
Enter the Side 2 of the Trapezium: 5
Enter the Heigth of the Trapzium: 3
"""
#OUTPUT: The Total Area of the Trapezium is  18.0

## AREA OF THE CIRCLE
import math
Radius = float(input("Enter the radius of the circle: "))
Area = math.pi * Radius ** 2
print("The Toal area of the circle is ", Area)
#Sample Input: Enter the radius of the circle: 25
#OUTPUT: The Toal area of the circle is  1963.4954084936207

## CONVERSION OF DISTANCE FROM KM TO MILES 
kiloM = float(input("Enter the distance in the KiloMeters: "))
Miles = 0.6213 * kiloM
print("The Miles is Equal to ", Miles)
#Sample Input: Enter the distance in the KiloMeters: 10
#OUTPUT: The Miles is Equal to  6.212999999999999

## dISPLACEMENT CALCULATION 
InitVel = float(input("Enter the Initial Velocity: "))
FinalVel = float(input("Enter the Final Velocity: "))
Accelrn = float(input("Enter the Acceleration: "))
Disp = (FinalVel ** 2 - InitVel ** 2)/(2 * Accelrn)
print("The Displacement is ", Disp)
#Sample Input: 
"""
Enter the Initial Velocity: 8
Enter the Final Velocity: 15
Enter the Acceleration: 5
"""
#OUTPUT: The Displacement is  16.1

## TOTAL AREA OF THE CUBOIDAL
Length = float(input("Enter the Length of the Cuboidal: "))
Breadth = float(input("Enter the Braedth of the Cuboidal: "))
Heigth = float(input("Enter the Heigth of the Cuboidal: "))
TotalArea = 2 *(Length * Breadth + Length * Heigth + Breadth * Heigth)
print("The total area of the Cuboidal is ", TotalArea)
#Sample Input: 
"""
Enter the Length of the Cuboidal: 18
Enter the Braedth of the Cuboidal: 8
Enter the Heigth of the Cuboidal: 10
"""
#OUTPUT: The total area of the Cuboidal is  808.0

## QUADRATIC EQUATION
import math
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))
d = y ** 2 - 4 * x * z
root1 = (-y + math.sqrt(d))/(2 * x)
root2 = (-y - math.sqrt(d))/(2 * x)
print("The roots of this Quadratic Equation are: ",root1 ," And ", root2)
#Sample Input: 
"""
Enter the value of x: 1
Enter the value of y: -5
Enter the value of z: 6
"""
#OUTPUT: The roots of this Quadratic Equation are:  3.0  And  2.0