# Exerciții.....

# Dată fiind structura de date
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
    # + 1 milion de row-uri
]
# formată dintr-o listă de [name, age, hobbies]

#1. Îmbătrâniți-o pe Jane cu un an
friends[0][1] += 1

jane = friends[0]

# dar dacă nu știm care este indexul?
for friend in friends:
    if friend[0] == "Jane":
        # am "row-ul" corect
        friend[1] += 1
        # am operat, nu e nevoie să mai iterez
        break

# alternativ, scriem o funcție de retrieval:
def get_friend_by_name(lst, name):
    for friend in friends:
        if friend[0] == name:
            return friend

jane = get_friend_by_name(friends, "Jane")
jane[1] += 1 # creștem age


#2. Adăugați Annei hobby-urile "reading" și "knitting"
anna = get_friend_by_name(friends, "Anna")
#anna[2].append("reading")
#anna[2].append("knitting")
anna[2].extend(["reading", "knitting"])

#3. Ștergeți-i lui Mike hobby-ul de la indexul 1
mike = get_friend_by_name(friends, "Mike")
del mike[2][1]

#4. Adăugați un prieten nou:
new = ["Georgie", 22, ["reading", "cooking", "running"]]
friends.append(new)


print(friends)


# Scrieți o funcție care să returneze o listă cu prietenii
# ce au un anumit hobby
def find_by_hobby(lst, hobby):
    # 1. instanțiez obiect final
    out = []

    # 2. iterez în sursa de date
    for person in lst:
        hobbies = person[2]
        # 3. filtrez
        if hobby in hobbies:
            # 4. construiesc
            out.append(person)

    # 5. gata
    return out

# Testați:
print(
    find_by_hobby(friends, "hiking")
)

# Scrieți o funcție care să returneze o listă cu prietenii
# cu vârsta cuprinsă între min și max
def find_by_age(lst, min_age, max_age):
    out = []

    for person in lst:
        age = person[1]
        if min_age <= age <= max_age:
            out.append(person)

    return out

# Testați:
print(
    find_by_age(friends, 20, 40)
)

# Testați ambele funcții înlănțuite:
# găsiți toți prietenii cu vârstă între 20 și 30 de ani
# pasionați de hiking.
print(
    find_by_hobby(
        find_by_age(friends, 20, 40),
        "hiking"
    )
)

# Adăugați la toți prietenii peste 30 de ani
# hobby-ul "knitting".

# modificăm semnătura funcției,
# transformând `max_age` din "positional argument"
# în "keyword argument" (kwarg).

def find_by_age(lst, min_age, max_age=None):
    out = []

    for person in lst:
        age = person[1]

        if min_age <= age and (
            max_age is None or max_age >= age
        ):
            out.append(person)

    return out
