c = int(input("Enter the Number: "))
if c % 2 ==0:
    print(c, "Is Even")
else:
    print(c, "Is Odd")
    
#Sample INPUT 01: Enter the Number: 8
#OUTPUT: 8 Is Even
#Sample INPUT 02: Enter the Number: 9
#OUTPUT: 9 Is Odd

Marks = int(input("Enter Your Marks: "))
if Marks >=90:
    print("Grade:A")
elif Marks >=80 and Marks <90:
    print("Grade:B")
elif Marks >=70 and Marks <80:
    print("Grade:C")
else:
    print("You got Failed")
#Sample INPUT 01: Enter Your Marks: 95
#OUTPUT: Grade:A
#Sample INPUT 02: Enter Your Marks: 82
#OUTPUT: Grade:B
#Sample INPUT 03: Enter Your Marks: 70
#OUTPUT: Grade:C
#Sample INPUT 04: Enter Your Marks: 55
#OUTPUT: You got Failed

FavFood = input("Enter Your Favorite Food: ")
if FavFood == "Idli" or FavFood == "Dosa":
    print("I too Like Idli and Dosa")
elif FavFood == "Chicken" or FavFood =="Fish":
    print("I Occasionally Eat Non-Veg")
else:
    print("I Hate That You Like🤦")

#Sample INPUT 01: Enter Your Favorite Food: Idli
#OUTPUT: I too Like Idli and Dosa
#Sample INPUT 02: Enter Your Favorite Food: Chicken
#OUTPUT: I Occasionally Eat Non-Veg
#Sample INPUT 03: Enter Your Favorite Food: Fish
#OUTPUT: I Occasionally Eat Non-Veg
#Sample INPUT 03: Enter Your Favorite Food: Sweets
#OUTPUT: I Hate That You Like🤦
     
