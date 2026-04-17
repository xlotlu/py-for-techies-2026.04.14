# Scrieți o funcție ce copiază conținutul fișierelor:
def cp(infile, outfile):
    with open(infile, "r" , encoding="utf-8") as in_f:
        content = in_f.read()

    with open(outfile, "w" , encoding="utf-8") as out_f:
        out_f.write(content)


def cp(infile, outfile):
    with open(infile, "r" , encoding="utf-8") as in_f:
        content = in_f.read()

        with open(outfile, "w" , encoding="utf-8") as out_f:
            out_f.write(content)


# pot fi deschise multiple context managere simultan!!!
# (în același `with` statement)

def cp(infile, outfile):
    with open(infile, "r" , encoding="utf-8") as in_f, open(outfile, "w" , encoding="utf-8") as out_f:
        content = in_f.read()
        out_f.write(content)

# line continuation: un backslash la sfârșitul rândului
var = "un string incredibil de lung" + \
      " o chestie"

var = (
    "un string incredibil de lung"
    + " o chestie"
)


# rescriu, cu finețe cosmetică:
def cp(infile, outfile):
    with open(infile, "r" , encoding="utf-8") as in_f, \
         open(outfile, "w" , encoding="utf-8") as out_f:
        content = in_f.read()
        out_f.write(content)

# sau, folosesc paranteze
def cp(infile, outfile):
    with (
        open(infile, "r" , encoding="utf-8") as in_f,
        open(outfile, "w" , encoding="utf-8") as out_f
    ):
        content = in_f.read()
        out_f.write(content)

# adaptăm să meargă și pentru fișiere binare:
def cp(infile, outfile):
    with (
        open(infile, "rb") as in_f,
        open(outfile, "wb") as out_f
    ):
        out_f.write(in_f.read())


# Știind că
#  - open(mode="w") este mod de scriere ce trunchează fișierul existent
#  - open(mode="x") este mod de scriere ce refuză să facă overwrite
#
# modificați funcția cp() astfel:
def cp(infile, outfile, overwrite=False):
    if overwrite:
        mode = "wb"
    else:
        mode = "xb"

    # echivalent cu:

    mode = "wb" if overwrite else "xb"

    with (
        open(infile, "rb") as in_f,
        open(outfile, mode) as out_f
    ):
        out_f.write(in_f.read())



# Scrieți o funcție
def get_words(file):
    pass
# ce returnează o listă a cuvintelor din `file`

import string

# NON_WORD_CHARS = string.punctuation
NON_WORD_CHARS = '!"#$%&\'()*+,./:;<=>?@[\\]^`{|}~'

def get_words(file):
    with open(file, encoding="utf-8") as f:
        content = f.read()
        # cum scăpăm de caracterele non-alfa?
        # sanitizăm pe `content`:
        for chr in NON_WORD_CHARS:
            content = content.replace(chr, " ")

        return content.split()

print(get_words("test.txt"))


# dat fiind string-ul
s = "Bună ziua, string-ul știe slicing"

# printați:

# - primele 6 caractere din string
print(s[:6])
# - ultimele 7 caractere
print(s[-7:])
# - caracterele de la indexul 5 la 15 (inclusiv)
print(s[5:16])
# - întregul string citit de la coadă la cap
print(s[::-1])
