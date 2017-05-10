# This is Muhammad Azri

#desmondyeoh11@gmail.com


import math
#import PyAutoGUI #programme to control your mouse
#import tkinter #build a GUI
#import Django #build a website, similar to Ruby on Rails
#import flask #build a website, easier than Django
#import kivy #build apps

#Python is usually used to automate small and simple task

#firstname = input("Your first name?: ")
#lastname = input("Your last name?: ")
#print ("\nHello, " + firstname + " " + lastname)

#num1 = int(input("Enter first number: ")) #for numbers, put int before input
#num2 = int(input("Enter second number: "))
#print (num1 + num2) - as integers

#print("Sum: " + str(num1 + num2)) # as string

#data types in Python
#print (3 + 2) #Output 5 - as integers
#print('3' + '2') #Output 32 - as string (with '')
#print("3" + "2") #Output 32 - as string (with "")

#there is no character is Python, only String

# True & False = boolean (capital letters)

#print ('2' == '2') #boolean

#math operation
# print(2/1)
# print (3**2) #3 to the power of 2
# print(math.sqrt(2)) #need to import math first
# print(math.floor(2.4)) #you go to the nearest lowest point - rounding operation
# print(math.ceil(2.4)) #you go the nearest highest point - rounding operation
# print(round(2.5, 0)) #will go to 2, kinda surprising
# print(round(2.6, 0)) #will go to 3

#it treats every variables and inputs as string, so to use it as integer and float, conver it first

#displacement = float(input("Displacement: "))
#time = float(input("Time: "))
#print("Velocity: ", displacement/time, sep='XX', end = " ENDDDDD")
#sep - separator to add something between printed and variables
#end - ending a printed with something, by default, it's a new line if it's empty

#print ('Name', end = ' ')
#print('Azri')

# height = float(input("Your height in metres: "))
# weight = int(input("Your weight in kg: "))

#BMI = (weight)/(height**2)

#print("Your BMI is: ", BMI)

# print((weight)/(height**2))

# def method(abc=2,ddd=3):
# 	print(abc,ddd)

#method()
#method(ddd=5)

# def BMIcalc():
# 	height = float(input("Your height in metres: "))
# 	weight = int(input("Your weight in kg: "))
# 	print((weight)/(height**2))

# BMIcalc()

# print(3 == 3)
# print(3 == 4)
# print(not (3 == 4))
# print(5 > 3)
# print(not (5 > 3))
# print(3 > 3)
# print (3 >= 3)
# print(3 < 3)
# print (3 <= 3)

#age = int(input("Your age: "))

# if age < 18:
# 	print("Underage")
# else:
# 	print("Overage")

# age = int(input("Your age: "))

# if 0 <= age <= 12:
# 	print("Children")
# elif 13 <= age <= 18:
# 	print("Teenager")
# elif age >= 19:
# 	print("Adult")
# else:
# 	print("Invalid Age")

# for i in range(10): #from 0 to 9
# 	print("Hello")

# for a in range(10):
# 	print(a)

# for b in range(10, 20):
# 	print(b)

# for c in range(10):
# 	name = input("Your name?: ")
# 	print(name)

# password = input("Enter your password: ")

# while password != 'azri':
# 	password = input("Enter your password: ")

# print("Success Login!")

# scores = [10, 23, 30, 50, 8] #can put string, integer and float together

# print(scores[0]) # 10
# print(scores[-2]) #from behind, from the last position - 50
# print(len(scores))

# jumbles = [10, 'Dzaqwan', 30, 'Adhwa', 8]

# print(jumbles[0])
# print(jumbles[-1])
# print(len(jumbles))

# for i in scores:
# 	print(i) #print the content one by one

# for i in scores:
# 	print(scores) #print the whole content, n times of quantity of that list

# def velocity(displacement, time): #inside bracket, what is needed to execute the function
# 	return displacement / time

# def announcement():
# 	return "Get out of here!"

# print(velocity(2,1))
# print(announcement())

bioList = ['Azri', 'WER150018', '26 Nov 1994']

# bioDict = {
# 	"name": "Azri",
# 	"matrik": "WER150018",
# 	"bday": "26 Nov 1994",
# }

bioDict = {
	"name": bioList[0],
	"matrik": "WER150018",
	"bday": "26 Nov 1994",
}

print(bioDict) #print the whole dictionary
print(bioDict['name']) #print certain part of dictionary

#to run python files, use "py <filename>.py"