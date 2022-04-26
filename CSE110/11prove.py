data_set = []

with open("life-expectancy.csv") as data_file:

    for line in data_file:
         #print(line.split(","))
        if line.startswith("Entity"): continue;

        row = line.split(",")
        row[2] = int(row[2])
        row[3] = float(row[3])
        data_set.append(row)       

#min max
min_exp = 1000
min_year = None
min_country = None

for i in data_set:
    if i[3] < min_exp:
        min_exp = i[3]
        min_year = i[2]
        min_country = i[0]

max_exp = 0
max_year = None
max_country = None

for i in data_set:
    if i[3] > max_exp:
        max_exp = i[3]
        max_year = i[2]
        max_country = i[0]

input_year = []
input_year = int(input("Enter the year of intrest: (1950-2019)? "))

print(f"The overall max life expectancy is: {max_exp} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_exp} from {min_country} in {min_year}")
print()


if input_year < 1950 or input_year > 2019:
    print("Year does not exist, please select a year that does. (1950-2019)")

year_list = []

for i in data_set:
    if i[2] == input_year:
        year_list.append(i)

min_exp = 150
min_year = None
min_country = None

for i in year_list:
    if i[3] < min_exp:
        min_exp = i[3]
        min_year = i[2]
        min_country = i[0]

max_exp = 0
max_year = None
max_country = None
sum = 0 

for i in year_list:
    sum += i[3]
    if i[3] > max_exp:
        max_exp = i[3]
        max_year = i[2]
        max_country = i[0]

avg = sum / len(year_list)
print()
print(f"For the year {input_year}: ")
print(f"The average life expectancy across all countries was {avg:.2f}")
print(f"The max life expectancy was in {max_country} with {max_exp}")
print(f"The min life expectancy was in {min_country} with {min_exp}")
print()