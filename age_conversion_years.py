def age_conversion_years():
    x = float(input("Enter age of dog in human years: "))

    if x <= 0:
        print(f"Number is a negative. Please choose another.")
    elif x <= 2:
        y = x * 10.5
        print(f"The age of the dog is: {y: 2f}")
    if x > 2:
        z = (2 * 10.5) + ((x - 2) * 4)
        print(f"The dog is {z: 2f} years.")


age_conversion_years()
