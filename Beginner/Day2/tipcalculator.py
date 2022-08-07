from typing import final


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill £"))
tip = int(input("How much would you like to tip? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

tip_percent = tip / 100
total_amount = bill * tip_percent
total_bill = bill + total_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: £{final_amount}") 