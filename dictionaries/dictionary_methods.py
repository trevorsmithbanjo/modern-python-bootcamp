# clear empties dictionary of all data
d = {
    "a": 1,
    "b": 2,
}

print(d)
d.clear()
print(d)

# copy makes a copy of a dictionary. they look the same but aren't the same in memory
d2 = {
    "a": 1,
    "b": 2,
    "c": 3,
}

c = d2.copy()
print(c)
c == d # true
c is d # false

# fromkeys usually used to generate default values
new_user = {}.fromkeys(["name", "score", "email", "profile bio"], "unkown")
print(new_user)
