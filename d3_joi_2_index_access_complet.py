lst = ["ala", "bala", "porto", "cala"]

# acces după index negativ:
lst[-1]

# slicing
lst[1:3]
# de la început până la un index
lst[:3]
# de la un index până la sfârșit
lst[3:]

# ultimele două elemente
lst[-2:]
# toate în afată de ultimele două


# introducem step:
range(1, 10, 2)
range(10, 0, -1)

# step în cazul slice-ului:
lst[1:10:2]
lst[10:1:-1]
# toată lista, inversată:
lst[::-1]

# dată fiind lista
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

# creați o listă nouă cu primele 5 distanțe
# în ordine crescătoare (sortate).

# algoritm:
# 1. creăm o listă nouă cu distanțele.
distances = []

for city in cities:
    dist = city[1]
    distances.append(dist)

# 2. sortăm lista de distanțe
distances.sort()

# 3. slice pe listă
print(distances[:5])


# Exercițiu:
# vrem primele 5 orașe în ordinea crescătoare
# a distanței
def myfunc(elem):
    return elem[1]

cities.sort(key=myfunc)
print(cities[:5])

# orașe sortate după ultima literă a numelui
def strange_sorter(elem):
    # elem = ('Ploiești', 60)
    return elem[0][-1]

cities.sort(key=strange_sorter)

# dar sortate după ultima literă și nr. km?
def stranger_sorter(elem):
    # elem = ('Ploiești', 60)
    return (elem[0][-1], elem[1])

cities.sort(key=stranger_sorter)

