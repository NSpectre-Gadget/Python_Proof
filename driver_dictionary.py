def driver_dictionary():
    from pathlib import Path

    x = int(input("Enter no. of drivers allowed: ").strip())
    person = {}

    for i in range(x):
        # Enter driver information
        name = input("Enter your first and last name as appears on state license: ")
        imageb = input("enter the path of the image file: ")
        # imageA = Image.open(sys.argv[1])
        height = input("Enter your height in ft and inches, e.g 5ft10in: ")
        race = input("Enter your race or ethnicity: ")
        dl_number = input("Enter your driver's license number: ")
        person[name] = [imageb, height, race, dl_number]

    print(person)


driver_dictionary()
