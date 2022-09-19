# Sign your name:Rachel
# In all the short programs below, do a good job communicating with your end user!
import math  # always put import at the top of the page
# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = input("Hello, what is your name?")
print("Hello", name + ", How are you doing today?")
print()
print("---------")
print()
# 2. Write a program where a user enters a base and height, and you print the area of a triangle.
base = float(input("What is the base of your triangle in cm?"))
height = float(input("What is the height of your triangle in cm?"))
area = ((base*height)/2)
print("The area of the triangle was", area, "cm^2")
print()
print("---------")
print()
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
R = float(input("What is the radius of a circle in meters?"))
C = ((R*math.pi)*2)
print("The circumference of a circle was", C, "meters")
print()
print("---------")
print()
# 4. Ask a user for an integer and then print the square root.
Int = int(input("What is the radius of a circle?"))
squareRoot = (math.sqrt(Int))  # square root in numbers = x^0.5
print("The square root of", Int, "is", squareRoot)
print()
print("---------")
print()
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = float(input("What is the mass in kg?"))
accel = float(input("What is the acceleration in m/s/s?"))
force = (mass*accel)
print("May the", force, "N, be with you")
print("Get it?")
# print()
# print("2+3")
# print(2+3)
# print("Hello World")
# print("your new score is", 1030+10)
# print("I want to print a double quote \"right here")  # \ is an escape code
# print("Hello \nWorld")  # causes a new line
# print()
# print("Hello \rWorld")
# print()
# print("Hello", end=" Here is the end character")  # this # is above the three on the keyboard
# print("World")
# print()
# # tab makes adds an indent and shift tab undoes an indent
# int()
# miles_Driven = float(input("enter the miles driven:"))
# gallons_used = float(input("enter the gallons used:"))
# mpg = miles_Driven/gallons_used
# print(mpg)

'''
this is a docstring
'''