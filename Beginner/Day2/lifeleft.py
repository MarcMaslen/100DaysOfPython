age = input("What is your current age?")

int_age = int(age)
life_left = 90 - int_age

days = life_left * 365  
weeks = life_left * 52
months = life_left * 12

print(f" You have {days} days, {weeks} weeks, and {months} months left.")

