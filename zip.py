firsts = ["Anna", "Bob", "Charles"]
middles = ["Z.", "A.", "G."]
lasts = ["Smith", "Doe", "Evans", "anotherone"]

# zip ignore length mismatch issues by ignoring extra variables, from python 10 you can add keyword "strict=True" to raise exception


# zip allow to combine two lists and make actions
for z in zip(firsts, middles, lasts):
    first, middle, last = z
    print(f"'{first} {middle} {last}'")

# zip does not create list, you have to create new list from zip output
z = zip(firsts, lasts)
print(z)
print(list(z))


# creating dicts (overwrites duplicates - pay attention!!)
d = dict(zip(firsts, lasts))
print(d)
