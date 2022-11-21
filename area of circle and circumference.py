#Desigh a function to calculate the area of a circle

from math import pi

def getArea(radius):
    area = pi*(radius**2)
    return area

def circumference(radius):
    circum=(2*pi*radius)
    return circum

r = float(input("Enter Radius: "))
area = getArea(r)
circum = circumference(r)
print("Area of the circle is: ",area)
print("Circumference of circle is", circum)