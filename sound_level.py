def sound_level():
    sound_level = {
        "Jackhammer": 130,
        "Gas Lawnmower": 106,
        "Alarm Clock": 70,
        "Quiet Room": 40,
    }
    # reserse the key value location in the dictionary.
    reversed_dictionary = dict(map(reversed, sound_level.items()))

    db = float(input("Enter the number of decibels: "))
    if db <= 40:
        print(f"The leve of sound is equivalent to {reversed_dictionary[40]}")
    if 41 < db <= 70:
        print(f"The level of sound is equivalent to {reversed_dictionary[70]}")
    if 71 < db <= 106:
        print(f"The level of sound is equivalent to {reversed_dictionary[106]}")
    if 107 < db <= 130:
        print(f"The level of sound is equivalent to {reversed_dictionary[130]}")
    elif db > 130:
        print(f"The entered {db: .2f} level is immediately hearing harmful.")


sound_level()

# print(f"The level of sound is equivalent to {reversed_dictionary[db]}")

# print(f"The entered decibel reaches {sound_level[db]}")
