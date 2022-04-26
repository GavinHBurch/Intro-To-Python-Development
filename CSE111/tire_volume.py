from datetime import datetime

current_date_and_time = datetime.now()

print(f"{current_date_and_time:%Y-%m-%d}")

import math

print()
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
print()

volume = width * aspect + 2540 * diameter
air = math.pi * width**2 * aspect * (volume)
tire = air / 10000000000


tire = round(tire, 2)

print(f"The approximate volume is {tire} liters")
print()
