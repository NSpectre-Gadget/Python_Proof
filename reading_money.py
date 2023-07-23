def money_reader():
    money_table = {
        "George Washington": 1,
        "Thomas Jefferson": 2,
        "Abraham Lincoln": 5,
        "Alexander Hamilton": 10,
        "Andrew Jackson": 20,
        "Ulysses S. Grant": 50,
        "Benjamin Franklin": 100,
    }
    # reverse the key value location in the dictionary.
    reversed_table = dict(map(reversed, money_table.items()))

    dollar_bill = float(
        input("Enter the amount appearing on the face of the banknote: ")
    )
    if dollar_bill == 1:
        print(
            f"This is a {dollar_bill} dollar bill and {reversed_table[1]} appears on the face."
        )
    elif dollar_bill == 2:
        print(
            f"This is a {dollar_bill} dollar bill and {reversed_table[2]} appears on the face."
        )
    elif dollar_bill == 5:
        print(
            f"This is a {dollar_bill} dollar bill and {reversed_table[5]} appears on the face."
        )
    elif dollar_bill == 10:
        print(
            f"This is a {dollar_bill} dollar bill and {reversed_table[10]} appears on the face."
        )
    elif dollar_bill == 20:
        print(
            f"This is a {dollar_bill} dollar bill and {reversed_table[20]} appears on the face."
        )
    elif dollar_bill == 50:
        print(
            f"This is a {dollar_bill} dollar bill and {reversed_table[50]} appears on the face."
        )
    elif dollar_bill == 100:
        print(
            f"This is a {dollar_bill} dollar bill and {reversed_table[100]} appears on the face."
        )
    else:
        print(f"The entered {dollar_bill} does not exist in U.S. circulation.")


money_reader()
