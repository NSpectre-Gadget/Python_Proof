G = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0,
}

F = []

c = int(input("Enter no. of classes to average: ").strip())
num = []

points = float(input("Enter the interest rate percentage of the investment: "))
credits = float(input("Enter the interest rate percentage of the investment: "))

for i in range(c):
    y = int(input(f"Enter the grade given {(G[c])}."))
    num.append(y)
print(num)

TPE = sum(points)
TCA = sum(credits)

print(TPE)
print(TCA)

for n in G:
    GPA = TPE / TCA
    F.append(GPA)
for n in num:
    for i in F:
        print(n, i)
print(F)
