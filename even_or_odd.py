def even_or_odd():
    n = float(
        input(f"Enter an interger so the program can determine if it is even or odd:  ")
    )

    if (n % 2) == 1:
        print(f"{n} is odd.")
    else:
        print(f"{n} is even.")


even_or_odd()
