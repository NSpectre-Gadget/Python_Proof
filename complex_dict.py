import random
import string

keys = ["id", "username", "password"]
users = ["mariyasha888", "KnotABot"]

data = [
    {
        key: (
            i
            if key == "id"
            else users[i]
            if key == "username"
            else "".join(random.choices(string.printable, k=8))
        )
        for key in keys
    }
    for i in range(len(users))
]
print(data)
