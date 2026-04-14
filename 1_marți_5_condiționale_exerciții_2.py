# Exercițiu:
# salutăm utilizatorul cu salutul potrivit pentru ora curentă

hour = int(input("Care este ora? "))

# dacă ora este între 5 și 10:
#  "Bună dimineața"
# între 10 și 19:
#  "Bună ziua"
# între 19 și 22:
#  "Bună seara"
# între 22 și 5:
#  "Noapte bună"

if hour >= 5 and hour < 10:
    print("Bună dimineața")
elif hour >= 10 and hour < 19:
    print("Bună ziua")
elif hour>=19 and hour<22:
    print("Bună seara")
else:
    print("Noapte bună")