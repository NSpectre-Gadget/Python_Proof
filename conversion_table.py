C = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
F = []

for n in C:
    F_Temp = n * (9 / 5) + 32
    F.append(F_Temp)
for n in C:
    for i in F:
        print(n, i)
print(C, F)
