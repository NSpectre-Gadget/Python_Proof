def fuel_conversion_1():
    mpg = float(input("Enter number of mpg consumption: "))

    L_per_100_km = 235.21 / mpg

    print(f"The {mpg} mpg equals to {L_per_100_km: .2f} L per 100/km.")


fuel_conversion_1()
