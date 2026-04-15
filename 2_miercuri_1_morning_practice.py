#1. obțineți partea întreagă a împărțirii lui 17 la 4.
17 // 4

#2. obțineți restul împărțirii lui 17 la 4.
17 % 4

#3. ridicați 8 la puterea a 3a.
8 ** 3

#5. scrieți o funcție `cube(x)` ce returnează x la puterea a 3a.
def cube(x):
    return x ** 3

#6. cereți input de la utilizator un număr întreg.
#   printați textul "Cubul numărului <număr> este <cub>."
num = input("Introdu un număr întreg: ")
result = cube(int(num))
output = "Cubul numărului " + str(num) + " este " + str(result) + "."
print(output)

#7. concatenați string-ul "tra la la " cu sine de 7 ori.
"tra la la " * 7

#8. scrieți o funcție `get_user_name()` ce promptează utilizatorul
#   pentru numele său și îl returnează.

def get_user_name():
    name = input("Care este numele tău? ")
    return name

#9. folosiți următorul cod pentru a obține ora curentă:

from datetime import datetime

def get_current_hour():
    now = datetime.now()
    return now.hour

#10. folosind funcțiile
#    - get_user_name()
#    - get_current_hour()
#    - și get_greeting(hour) definită ieri
#    cereți numele utilizatorului și salutați-l
#    cu salutul potrivit pentru momentul zilei.
#    Exemplu de rezultat: "Bună dimineața Gigel".
def get_greeting(hour):
    # am acces la hour
    if hour >= 5 and hour < 10:
        return "Bună dimineața"
    elif hour >= 10 and hour < 19:
        return "Bună ziua"
    elif hour>=19 and hour<22:
        return "Bună seara"
    else:
        return "Noapte bună"

name = get_user_name()
hour = get_current_hour()
greeting = get_greeting(hour)
print(greeting + " " + name)

#11. Scrieți o funcție
def is_expected_age(age):
    pass
#   ce returnează True dacă argumentul `age` are valoare
#   cuprinsă între 18 și 60 inclusiv, și False în celelalte cazuri.

def is_expected_age(age):
    if age >= 18 and age <= 60:
        return True
    else:
        return False

def is_expected_age(age):
    return age >= 18 and age <= 60

def is_expected_age(age):
    return 18 <= age <= 60


#12. Scrieți o funcție `get_user_age()` ce promptează utilizatorul
#    pentru vârsta sa și o returnează drept număr întreg.
#    Combinați `get_user_age()` cu `is_expected_age()`
#    și dacă rezultatul este True printați mesajul "Acceptat", altfel
#    "Ne pare rău, nu ai vârsta potrivită".
#
#    Găndiți-vă cum ați putea să vă asigurați că utilizatorul tastează un număr întreg.

def get_user_age():
    age = input("Vârsta ta? ")
    return int(age)

user_age = get_user_age()
if is_expected_age(user_age):
    print("Acceptat")
else:
    print("Ne pare rău, nu ai vârsta potrivită")



# Găndiți-vă cum ați putea să vă asigurați
# că utilizatorul tastează un număr întreg.
#
# 1) avem nevoie să detectăm dacă input-ul este ok
# 2) vrem să îl forțăm să tasteze din nou dacă nu a fost ok.
