d = {
    'timestamp': '07:00:00',
    'value': 19.28
}

d['timestamp'] # <-- "item access"
print(d['value'])

# modificăm o valoare pentru o cheie
d['value'] = 25

# aceeași sintaxă, adăugăm o cheie
d["wind_speed"] = 60

# ștergem o cheie
del d["wind_speed"]

# dat fiind
jane = ["Jane", 20, ["reading", "hiking", "biking"]]
# creați variabila
# `djane` un dicționar cu cheile "name", "age", "hobbies"

name, age, hobbies = jane
djane = {
    "name": name,
    "age":  age,
    "hobbies": hobbies,
}

# dat fiind lista
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# creați o listă de dicționare {"name": "...", "age": "...", "hobbies": "..."}
dfriends = []
for f in friends:
    name, age, hobbies = f
    d = {
        "name": name,
        "age":  age,
        "hobbies": hobbies,
    }
    dfriends.append(d)
print(dfriends)