import math


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("please enter a rectangle or a circle")


def rectangle_area():
    length = float(input("enter the length : "))
    width = float(input("enter the width : "))
    area = length * width
    print("The area of the rectangle is: ", area)


def circle_area():
    radius = float(input("enter the radius : "))
    area = math.pi * (math.pow(radius, 2))
    print("The area of the circle is: {:.2f}".format(area))


def main():
    shape_type = input("Get area for what shape : ")
    get_area(shape_type)


main()
