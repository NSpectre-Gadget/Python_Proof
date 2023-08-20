names = ["Mariya", "Gendalf", "Batman"]
profs = ["programmer", "wizard", "superhero"]

my_dict = {}

for key, value in zip(names, profs):
    my_dict[key] = value

print(my_dict)

my_dict = {"Spider": "photographer", "Bat": "philanthropist", "Wonder Wo": "nurse"}

my_dict = {
    (key + "man" if key != "spider" else "Superman"): (
        val if val != "photographer" else "journalist"
    )
    for (key, val) in my_dict.items()
}
print(my_dict)
