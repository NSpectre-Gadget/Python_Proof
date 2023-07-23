n = int(input("Enter the no of entries you want to enter : "))
dict = {}
for i in range(n):
    key = int(input("Enter the key : "))
    value = input("Enter the value : ")
    dict[key] = value
print(dict)
