# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0 
for score in student_scores: #loops through numbers
    if score > highest_score: #each number is scaned if higher then previous number
        highest_score = score #it is replaces as the highest score
print("The highest score in the class is: " + str(highest_score)) 