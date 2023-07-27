n = int(input("Enter no. of variables to average: ").strip())
num = []

for i in range(n):
    y = int(input("Number: "))
    num.append(y)
print(num)

sum_num = sum(num)
len_num = len(num)

print(sum_num)
print(len_num)


def average_num():
    average = sum_num / len_num
    print(f"The average of the number is: {average}")


average_num()
