# import un modul
import modulename

# import un simbol dintr-un modul
from modulename import symbol

# putem importa mai multe simboluri
from modulename import symbol1, symbol2 #, ...

# putem importa _toate_ simbolurile
from modulename import *

# ^^ nu este recomandat, pentru că riști
# să îți suprascrii simbolurile unul cu celălalt


# există și alias-uri
import modulename as malias
from modulename import symbol as salias
