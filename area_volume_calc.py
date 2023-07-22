# This function will calculate
def area_volume_calc():
    r = float(input(f"Enter the radius: "))

    pi = 3.141565

    A = pi * (r**2)
    V = (4 / 3) * pi * (r**3)

    print(f"The area of the circle is {A: .2f} cm squared.")
    print(f"The volume of the sphere is {V: .2f} cm cubed.")


area_volume_calc()
