numbers = []

for n in numbers:
    n = float(input("Enter several numbers separated by a comma to be averaged: "))
    numbers.append(n)
    print(numbers)


def average():
    if len(numbers) != 0:
        average = sum(numbers) / len(numbers)
        print(f"The average of the numbers is: {average}")


average()
