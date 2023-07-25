x = input("Enter a number: ")
x = x.split()
print(x)

numbers = []
sum_num = sum(numbers)
len_num = len(numbers)

for x in numbers:
    numbers.append(x)
print(numbers)


def average():
    # x = input("Enter several numbers separated by a comma to be averaged: ")
    average = sum_num / len_num
    print(f"The average of the numbers is: {average}")


average()
