grade = int(input("What is your grade percent? "))
print()
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
print()
sign = ""
last_digit = grade % 10
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
print()
if grade >= 93:
    sign = ""
if letter == "F":
    sign = ""
print(f"Your letter grade is: {letter}{sign}")
print()
if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")
print()