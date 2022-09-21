"""
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid
then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
"""
base = float(input("What is the base of your triangle in in?"))
b2 = float(input("what is the second base of the trapezoid in in?"))
height = float(input("What is the height of your triangle in in?"))
area = (((base+b2)/2)*height)
print("The area of the trapezoid is", area, "in^2")
