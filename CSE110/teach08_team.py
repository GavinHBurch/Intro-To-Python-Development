import math
user_choice = int(input("How many columns and rows do you want in your multiplication table? "))
max_number = user_choice * user_choice
digits = int(math.log10(max_number)) + 1
range_size = user_choice + 1
for row_number in range(1, range_size):
    for col_number in range(1, range_size):
        number = row_number * col_number
        print(f"{number:{digits}}", end=" ")
    print()
