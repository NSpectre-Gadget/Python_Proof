def cash_register():
    user_list = input("Enter values $:")
    coin = user_list.split(",").strip("")
    newlist = []
    for num in coin:
        newlist.append(round(float(num), 1))
    print(newlist)


cents_per_toonie = 200

cash_register()
