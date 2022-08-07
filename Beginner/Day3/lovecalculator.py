# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lower = combined_string.lower()

t = lower.count("t") 
r = lower.count("r") 
u = lower.count("u") 
e = lower.count("e") 

true = t + r + u + e

l = lower.count("l") 
o = lower.count("o") 
v = lower.count("v") 
e = lower.count("e") 

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score  > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) or (love_score  <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")