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

# 4 neucleobases in DNA
# A only with T; C only with G
# Adenine = A, Cytosine = C, Guanine = G, and Thymine = T

import random

bases = ["A", "T", "C", "G"]
strand1 = random.choices(bases, k=10)
print(strand1)

dna = {
    key: [
        val,
        ("T" if val == "A" else "A" if val == "T" else "C" if val == "G" else "G"),
    ]
    for (key, val) in enumerate(strand1)
}
print(dna)
