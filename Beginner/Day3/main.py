print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

#If and Else statments in Python
if height >= 120:
    print("You can ride this rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay £5")
    elif age <= 18:
         bill = 7
         print("Please pay £7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You can  go in for FREE")
    else:
        bill = 12
        print("Please pay £12")

    photos = input("Do you want photos, Y or N ? ")

    if photos == "Y":
        #Adds £3 to bill
        bill += 3
        print(f"the bill is: {bill}")
    else:
        print(f"The total bill is: {bill}")
else:
    print("You can not ride the rollercoaster")

#Comparoson operators

1 > 2 #Greater Than
2 < 1 #Less than
1 >= 3 #Greater than or equal to
2 <= 1 #Less than or equal too
1 == 2 #equal too
1 != 2 #not equal too