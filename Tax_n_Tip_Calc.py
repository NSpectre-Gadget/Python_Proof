def tax_n_tip():
    meal_cost = float(input("The amount of your meal is: "))
    local_tax_rate = 0.06
    tip_rate = 0.18

    tax = meal_cost * local_tax_rate
    tip = meal_cost * tip_rate

    grand_total = meal_cost + tax + tip

    print(
        f"Your meal has tax of {tax} tip amount of {tip} and grand total of $: {grand_total: .2f}"
    )


tax_n_tip()
