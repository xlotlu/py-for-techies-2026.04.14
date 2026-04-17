# dat fiind fișierul "books.csv"
# grupați cărțile după "Genre"
# și scrieți fiecare dintre aceste colecții
# în fișiere separate.
#
# exemplu: "economics.csv", "data_science.csv"
# etc.

import csv

with open("data/books.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    dfinal = {}

    for book in reader:
        genre = book['Genre']
        # dacă nu există genre în dfinal..
        if genre not in dfinal:
            dfinal[genre] = [] # instanțiez obiectul în care acumulez
        dfinal[genre].append(book)

    # am finalizat agregarea

    # acum creăm fișiere separate
    for genre, books in dfinal.items():
        filename = genre + ".csv"
        books # listă de dicționare

        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, reader.fieldnames)
            writer.writeheader()
            writer.writerows(books)



# rezolvare cu pandas!

import pandas as pd

df = pd.read_csv("data/books.csv")
for genre, g_books in df.groupby("Genre"):
    g_books.to_csv(f"pd_{genre}.csv")

# quick intro în pandas:

# acces după coloană:
for pub in df["Publisher"]:
    print(pub)

# slice de row-uri:
df[:3]
df[-3:]
# slice de coloană
df["Publisher"][:3]
