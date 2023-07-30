def price_discounts():
    original_cost = [4.95, 9.95, 14.95, 19.95, 24.95]
    new_price = []

    for n in original_cost:
        discounted_price = n * (n * 0.60)
        new_price.append(discounted_price)

    print(f"The original price of these items was: {original_cost}")
    print(f"The discount price for these items are:  {new_price}")


price_discounts()
