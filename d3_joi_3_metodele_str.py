# .split() / .join()
"Numele Meu".split()

" ".join(["Numele", "Meu"])

# .replace()

# .lower() / .upper()

# .startswith() / .endswith()

# .index() / .find()
#    -- în lumea Python este preferat .index()


# .strip() / .lstrip() / .rstrip()

# .removeprefix() / .removesuffix()


# ------------

# escape sequences
# încep cu backslash
# (backslash este 'escape character')
"\n" # newline
"\t" # tab
"\r" # carriage return

# și un backslash literal:
"aha \\ ok!"

# multi-line string:
"""
text
alt text
etc....
"""

'''
sau cu apostroafe
'''

myvar = """ceva
și altceva
etc."""

myvar = """
    ceva
    și altceva
    etc.
"""

# string formatting!!!
# exemple
# https://docs.python.org/3/library/string.html#format-examples

template = """
Salut {name},

Te anunțăm că ai un credit restant
în valoare de {amount:.02f} lei.

Conteactează-ne la {email:=^20} cât mai curând!.
"""

print(template.format(name="John Johnescu", amount=560.1268, email="adr@e.sa"))


# -----

# "f-strings"
num = 5
result = 125

f"Cubul numărului {num} este {result}."

# !!! cu f-strings, ce este între acolade se execută!
def cube(x):
    return x ** 3

f"Cubul numărului {num} este {cube(num)}."

def print_triple(num):
    print(f"Triplul numărului {num} este {triple(num)}.")

def triple(x):
    return x * 3

print_triple(15)