x = int(input("Enter no. of purchases to average: ").strip())
num = []

for i in range(x):
    y = int(input("Enter the age of attendees:"))
    num.append(y)
print(num)

cost = 23.00

if y <= 2:
    print(f"There is an infant in your group.")
elif 3 <= y <= 12:
    # u = cost * 0.6083
    print(f"You have to pay for kids in under 12 group")
elif 65 <= y:
    # v = cost * 0.7824
    print(f"You have to pay for senior citizens")
elif 13 <= y <= 64:
    # w = cost * 1.00
    print(f"You have to pay for a regular price ticket.")
