def area_of_the_field():
    acre = 43560

    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))

    area_of_the_field = length * width
    area_of_the_field_in_acreage = area_of_the_field / acre

    print(f"The area of your room is: {area_of_the_field_in_acreage} arcres")


area_of_the_field()
