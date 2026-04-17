# concepte:

Python este whitespace-sensitive.
(spațiul are înțeles semantic)

virgula: este întotdeauna separator

În Python totul este un obiect!

OOP = object-oriented programming

"Python is self-documenting"

În Python totul este o referință!


despre Python se spune că vine cu "batteries included"
   (și dacă nu există deja în stdlib, probabil cineva a rezolvat deja problema)


# essential debugging tools

print()
type() # returnează data-type-ul
help()


# data types:
int
float
str
bool # True / False
tuple
list # mutable
dict

notă: str, list & tuple sunt "sequences"
sequences:
 - sunt iterabile
 - toate suportă funcția len()
 - suportă metodele .count() și .index()
 - toate suportă acces după index
   (inclusiv index negativ)
 - toate suportă slicing
 - toate suportă operatorul `in`


# operatori:
- au prioritate
- dacă vrem să schimbăm prioritatea punem paranteze
- în Python pot fi cuvinte

## aritmetici

noi întâlniți

 //
 %
 **

## boolean (condiționali)

 ==
 !=
 and
 or
 not
 in
 not in
 is
 is not


# excepția

(o eroare)
SyntaxError / IndentationError
NameError   # când acest simbol nu este definit
UnboundLocalError # la fel ca NameError
                  # (doar că va fi declarată variabila mai târziu)
TypeError   # apare când data type-ul nu este potrivit
ValueError  # apare când valoare nu poate fi procesată
IndexError  # când nu există indexul
KeyError    # când nu există cheia


# funcția:

- blocuri de logică reutilizabile
- primește argumente (opțional)
- mai multe argumente sunt separate cu virgulă
- execută ceva
- returnează ceva (dar nu neapărat)
- poate avea side-effects


# instalare de library-uri

(în shell de sistem...)

pip install pandas
pip install ipython


# lucrul cu VSCode:

Ctrl + /    comment selection
Ctrl + F5   execută fișierul
Shift+Enter execută selecția într-un terminal de Python


# essential wisdom

DRY = don't repeat yourself

There are two very difficult problems in computing:
 - naming things
 - cache invalidation
 - off-by-one errors
