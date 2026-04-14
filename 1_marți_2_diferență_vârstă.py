# Exercițiu:
# Cereți utilizatorului:
# - vârsta voastră
# - vârsta unui prieten
# și apoi faceți print cu diferența astfel:
# "Diferența voastră de vârstă este <diff>"

# strategie:
# declarăm 2 variabile cu valoarea input()-ului
v1 = input("vârsta ta? ")
v2 = input("vârsta prietenului? ")

# trebuie să le transformăm în int
# le scădem
diff = int(v2) - int(v1)

# facem print
print("Diferența este " + str(diff))
