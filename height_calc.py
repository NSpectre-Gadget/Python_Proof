def height_calc():
    ft = float(input(f"Enter the feet height of the individual: "))
    inches = float(input(f"Enter the related inches of the individual: "))

    height_in_cm = (ft * (12) * (2.54)) + (inches * (2.54))
    print(f"This individual is {height_in_cm: .2f} cm tall.")


height_calc()
