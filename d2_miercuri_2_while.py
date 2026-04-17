# while conditie: # atenție la condiție. să se și schimbe.
#    do_something()
#    # etc.

# haideți să numărăm de la 5 la 1 (inclusiv)
n = 5

while n > 0:
    # mai întâi payload
    print(n)
    # apoi modificăm variabila
    n = n - 1

# comparați cu
while n > 0:
    # modificăm variabila
    n = n - 1
    # apoi payload
    print(n)


# alternativ, inițializăm o buclă infinită
# și ieșim din ea programatic când ne întâlnim condiția

n = 5
while True:
    if n == 0:
        break
    print(n)
    n = n - 1

n = 5
while True:
    print(n)
    
    n = n - 1
    if n == 0:
        break


# Scrieți o funcție ce obține vârsta utilizatorului ca nr. întreg.
# Dacă a tastat input invalid, primește mesaj de eroare,
# și nu este lăsat în pace până nu tastează un nr. întreg corect.
def get_user_age():
    while True:
        age = input("Vârsta ta? ")

        try:
            age = int(age)
            return age
        except ValueError:
            print("Tastează un număr întreg!")
