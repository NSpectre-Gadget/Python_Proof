def days_n_month():
    month = {
        "January": 31,
        "February": 28 or 29,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    m = str(input("Please select the month: "))

    print(f"The month selected has {(month[m])} days.")


days_n_month()
