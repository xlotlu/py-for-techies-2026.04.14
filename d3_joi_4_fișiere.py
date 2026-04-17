open("test.txt", encoding="utf-8")

# 'test.txt' este rezolvat _relativ_ la
# "current working directory".
# (care este by default directorul în care era shell-ul
#  care a executat python)


# notă importantă în computing:
# nu citiți și scrieți în același timp
# în același fișier
# din două procese separate....


# varianta 1 de folosit fișiere:
# citim totul în memorie
f = open("test.txt", encoding="utf-8")
content = f.read()
# acum totul e în memorie
print(content)

# varianta 2 de folosit fișiere:
# iterăm linie cu linie
f = open("test.txt", encoding="utf-8")
for line in f:
    print(line)


# context manager!
with open("test.txt", encoding="utf-8") as f:
    print(f.read())
    #1 / 0
# (se ocupă ca file handlerul să fie întotdeauna închis)


# scrieți o funcție
def readfile(fname):
    pass
# ce returnează conținutul fișierului `fname`.

def readfile(fname):
    with open(fname, encoding="utf-8") as f:
        return f.read()

print(readfile("quote.txt"))


# de ținut minte, raw strings:
f1 = "C:\\Users\\andrei"
f2 = r"C:\Users\andrei"

f1 == f2


# scrieți o funcție
def grep(fname, match):
    pass

# ce printează toate liniile din `fname`
# ce conțin substring-ul `match`.
#
# nu uitați că:
# 1) file handler-ul este iterabil
# 2) operatorul `in`

def grep(fname, match):
    with open(fname, encoding="utf-8") as f:
        for line in f:
            if match in line:
                # eliminăm \n din linie dacă există
                line = line.removesuffix("\n")
                print(line)

grep("data/quote.txt", "times")

# modificați funcția grep
# să returneze o listă de linii
# (în loc de a le face print)

def grep2(fname, match):
    out = []
    with open(fname, encoding="utf-8") as f:
        for line in f:
            if match in line:
                line = line.removesuffix("\n")
                out.append(line)
    return out
    
for match in grep2(path,'times'):
    print("»", match)


# file opening modes:
open("file.txt", encoding="utf-8")
# este echivalent cu
open("file.txt", "rt", encoding="utf-8")

# pentru a scrie într-un fișier:
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("my content")

# Exercițiu:
# scrieți o funcție
def writeinto(fname, content):
    pass
# ce scrie string-ul `content` în fișierul `fname`

def writeinto(fname, content):
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

writeinto("outfile.txt", "my content")

from datetime import datetime
writeinto("outfile.txt",
          f"salutare, este ora {datetime.now()}")