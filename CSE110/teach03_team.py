side = float(input("What is the length of a side of the square? "))
area = side ** 2
print(f"The area of the square is: {area}")


length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
area = length * width
print(f"The area of the rectangle is: {area}")


radius = float(input("What is the radius of the circle? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area}")


import math
radius = float(input("What is the radius of the circle? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area}")


value = float(input("What is the value to be used? "))


area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)


print(f"Area of a square: {area_square}")
print(f"Area of a circle: {area_circle}")
print(f"Volume of a cube: {volume_cube}")
print(f"Volume of a sphere: {volume_sphere}")


side = float(input("What is the length of a side of the square (in cm)? "))
area = side ** 2 

print(f"The area of the square is: {area} cm^2")

print(f"The area of the square is: {area / 10000} m^2")


length = float(input("What is the lengh of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")


radius = float(input("What is the radius of the cirlce (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")

print()
