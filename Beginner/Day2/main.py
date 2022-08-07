#Data types

#String
print("Hello"[0])

print("123" + "345")

#Integer

123 

345

123_321_345

#float

3.231345 
3.21234

#Boolean

True
False

#type error

num_char = len(input("what is your name?"))

print(type(num_char)) #this will tell you what type a varible is

new_num_char = str(num_char)

print("your name has " + new_num_char + " characters.")


#int to a string
a = str(123)
print(type(a))

#int to a float
print(70 + float("100.5"))

#int to string
print(str(100) + str(70))

#Mathamatical operators
3+5 #plus
7-3 #minus
2*2 #multiplication
4/2 #division
2 ** 3 #to the power off


#rounding

print(8/3)
print(round(8/3, 2)) #the added two is rounding the 2 decimal places
print(8//3) #prints an int

result = 4 / 2
result /= 2
print(result)

##score
score = 0

score += 1 #can be done with * / + -


#f-string
score = 0
height = 1.8
isWinning = True

print(f"your score is {score} and your height is {height} and did you win? {isWinning}")