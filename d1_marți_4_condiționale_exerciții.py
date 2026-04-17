# Exercițiu:
# Cereți utilizatorului:
# - vârsta voastră
# - vârsta unui prieten
# și apoi faceți print cu diferența astfel:
# "Diferența voastră de vârstă este <diff>".
# Atenție: output-ul să fie întotdeauna
#          un număr pozitiv

# strategie:
# declarăm 2 variabile cu valoarea input()-ului
v1 = input("vârsta ta? ")
v2 = input("vârsta prietenului? ")

# trebuie să le transformăm în int
# le scădem
diff = int(v2) - int(v1)

if diff > 0:
    print("Diferența este " + str(diff))
else:
    print("Diferența este " + str(-diff))



# alternativ,
# calculăm diferența drept nr. pozitiv
# doar când avem nevoie

if diff < 0:
    # pot să re-asignez variabila
    # unei alte valori
    diff = -diff

print("Diferența este " + str(diff))


# Exercițiu:
# dacă diferența este zero,
# faceți print cu "Aveți aceeași vârstă"
if diff > 0:
    print("Diferența este " + str(diff))
elif diff < 0:
    print("Diferența este " + str(-diff))
else:
    print("Aveți aceeași vârstă")


# Rezolvare alternativă, folosind abs()

if diff == 0:
    print("Aveți aceeași vârstă")
else:
    print("Diferența este " + str(abs(diff)))
