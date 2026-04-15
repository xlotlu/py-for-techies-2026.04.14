# for var in iterable:
#    do_something_with(var)
#    # etc.

# tuple
t = (1, 2, 3)

for v in "string":
    print(v)

for v in t:
    print(v)

# iterabilul nu are nevoie să fie "concret"
#range(stop) # start este implicit 0
#range(start, stop)


# list
l = [1, 2, 3]



# Dată fiind lista:
people = [
    "Andrew",
    "Jane",
    "Anne",
    "Bill",
    "George",
]

# printați oamenii al căror nume începe cu litera "A"
for elem in people:
    # care este prima literă a lui elem?
    # este "A"?

# dată fiind tupla
tup = ("Constanța", 280)
# creați două variabile, `city` și `distance`
# cu datele din `tup`. și le faceți print.
city = tup[0]
distance = tup[1]

city, distance = tup
print(city, distance)


# dată fiind lista de tuple (oraș, distanță):
cities = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 400),
    ('Constanța', 225),
    ('Craiova', 230),
    ('Brașov', 180),
    ('Galați', 250),
    ('Ploiești', 60),
    ('Oradea', 600),
    ('Brăila', 200),
    ('Arad', 580),
    ('Sibiu', 275),
    ('Bacău', 300),
    ('Târgu Mureș', 330),
    ('Baia Mare', 600),
    ('Buzău', 110),
    ('Satu Mare', 640),
    ('Suceava', 450),
]
# printați toate orașele cu distanță mai mică
# decât 300

for elem in cities:
    name = elem[0]
    distance = elem[1]

    if distance <= 300:
        print(name)

# unpacking
a, b, c = "str"
print(a, b, c)

a, b, c = [1, 2, 3]
print(a, b, c)

# a, b, c = [1, 2, 3, 4] # eroare

# rescris cu unpacking
for elem in cities:
    name, distance = elem

    if distance <= 300:
        print(name)

# rescris cu unpacking direct în for
for name, distance in cities:
    if distance <= 300:
        print(name)


# Exercițiu:
# creați o listă conținând pătratele numerelor
# de la 1 la 7
#
# știm că:
# range(start, stop)
# for elem in iter
# lst.append(value)

# Pattern de acumulare

# 1. avem sursa de date 
source = range(1, 8)
# 2. instanțiem obiectul în care acumulăm
lst = []
# 3. iterăm prin sursă
for n in source:
    # 4. ne facem calculul pentru valoare dorită
    nsquare = n * n
    # 5. acumulăm
    lst.append(nsquare)
# 6. suntem gata
print(lst)


# Exercițiu:
# calculați suma pătratelor numerelor de la 1 la 7
# 1. avem sursa de date
source = range(1, 8)
# 2. instanțiem obiectul în care acumulăm
total = 0
# 3. iterăm prin sursă
for n in source:
    # 4. ne facem calculul pentru valoare dorită
    nsquare = n * n
    # 5. acumulăm
    total += nsquare
# 6. suntem gata
print(total)



# Exercițiu:
# scrieți o funcție
def count_substr(lst, s):
    pass
# ce numără totalul aparițiilor substringului `s`
# în toate elementele din iterabilul `lst`

def count_substr(lst, s):
    total = 0
    for elem in lst:
        total += elem.count(s)

    return total

print(count_substr(
    ["ala", "bala", "porto", "cala", "tralalala"],
    "ala"
))


# Exercițiu:
# dat fiind lista
lst = [
 'Cluj-Napoca',
 'Timișoara',
 'Iași',
 'Constanța',
 'Craiova',
 'Brașov',
 'Galați',
 'Ploiești',
 'Oradea',
 'Brăila',
 'Arad',
 'Sibiu',
 'Bacău',
 'Târgu Mureș',
 'Baia Mare',
 'Buzău',
 'Satu Mare',
 'Suceava',
]
# creați o listă nouă cu orașele
# care încep cu litera "B"


b_cities = []
for city in lst:
    first_letter = city[0]
    if first_letter == 'B':
        b_cities.append(city)

print(b_cities)

# cu comentarii, pattern de acumulare condițional:
# instanțiez obiectul final
b_cities = []

# iterez în sursă
for city in lst:
    # verific condiția
    first_letter = city[0]
    if first_letter == 'B':
        # acumulez
        b_cities.append(city)
# gata
print(b_cities)


# implementare alternativă, cu continue
b_cities = []
for city in lst:
    first_letter = city[0]
    
    if first_letter != 'B':
        # fac aici early exit din bucla curentă
        # pentru valorile care nu mă interesează
        continue

    # este util să facem asta atunci când aici        
    # urmează mult cod în plus
    b_cities.append(city)


# Exercițiu:
# dată fiind lista de tuple de forma (nume, vârstă)
candidates = [
    ("Andrei", 16),
    ("Gigel", 40),
    ("Andra", 21),
    ("Elena", 42),
    ("Bogdan", 84),
    ("Mara", 62),
    ("Ion", 34),
    ("Ioana", 12)
]
# creați două liste noi, `accepted` și `rejected`:
# în `accepted` persoanele cu vârsta între 18 și 60 de ani,
# restul în `rejected`.

accepted = []
rejected = []

for name, age in candidates:
    if 18 <= age <= 60:
        accepted.append(name)
    else:
        rejected.append(name)

print("» acc", accepted)
print("» rej", rejected)

# dacă voiam lista de tuple?
accepted = []
rejected = []

for person in candidates:
    age = person[1]

    if 18 <= age <= 60:
        accepted.append(person)
    else:
        rejected.append(person)

print("» acc", accepted)
print("» rej", rejected)



### Metodele listei.
# pattern FIFO:

lst = []
lst.append("primul")
lst.append("al doilea")
lst.append("al treilea")
lst.pop(0)
lst.pop(0)
lst.pop(0)

# pattern LIFO
lst = []
lst.append("primul")
lst.append("al doilea")
lst.append("al treilea")
lst.pop()
lst.pop()
lst.pop()

# variațiune de FIFO:
lst = []
lst.insert(0, "primul")
lst.insert(0, "al doilea")
lst.insert(0, "al treilea")
lst.pop()
lst.pop()
lst.pop()


# Pattern:
# dacă vrem acces și la index și la element
# în timpul iterației, folosim `enumerate()`
for idx, elem in enumerate(lst):
    print(idx, elem)

# notă: enumerate returnează un iterator virtual.
# (adică nu ocupă extra-memorie)


# Pattern:
# consumăm o listă în timp ce iterăm prin ea.
# (util pentru conservarea memoriei)

lst = [
 'Cluj-Napoca',
 'Timișoara',
 'Iași',
 'Constanța',
]
while lst:
    elem = lst.pop(0)
    print("procesez:", elem)

# dacă nu mă interesează ordinea,
# este mai eficient cu procesorul să facem .pop() de la final:
while lst:
    elem = lst.pop()
    print("procesez:", elem)


# Temă pentru acasă:
# [opțional]
# scrieți o funcție
def removeall(lst, item):
    pass
# ce șterge toate aparițiile lui `item`
# din `lst`

