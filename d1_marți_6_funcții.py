# Exercițiu:
# scriem o funcție get_greeting(hour)
# ce returnează string-ul potrivit
# pentru ora respectivă

def get_greeting(hour):
    # am acces la hour
    if hour >= 5 and hour < 10:
        return "Bună dimineața"
    elif hour >= 10 and hour < 19:
        return "Bună ziua"
    elif hour>=19 and hour<22:
        return "Bună seara"
    else:
        return "Noapte bună"

greeting = get_greeting(15)
print(greeting)


# Exercițiu:
# scrieți o funcție de convertire din picioare în metri


def ft_to_m(ft):
    M_TO_FT = 3.28084
    return ft / M_TO_FT

# print(ft_to_m(3.3)) # aprox. 1

# Exercițiu:
# scrieți o funcție de convertire din metri în picioare
def m_to_ft(m):
    M_TO_FT = 3.28084
    return m * M_TO_FT

# print(m_to_ft(2))

M_TO_FT = 3.28084

def ft_to_m(ft):
    return ft / M_TO_FT

def m_to_ft(m):
    return m * M_TO_FT



var = 55 # variabilă globală
def func():
    var = 15 # există doar în funcție
    print("în func:", var)

func()
print("după func:", var)

# Exercițiu
# știind că
ONE_MILE = 1.60934 # km
# scrieți funcțiile
# km_to_miles() și miles_to_km()

def km_to_miles(km):
    return km / ONE_MILE

def miles_to_km(miles):
    return miles * ONE_MILE


# Exercițiu
# scrieți o funcție ce returnează 
# numărul cel mai mare dintre două valori
def get_largest(a, b):
    if a > b:
        return a
    else:
        return b

# Exercițiu
# scrieți o funcție ce detectează dacă un număr
# este par:
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(25))

# alternativ, returnăm direct expresia boolean
def is_even(n):
    return n % 2 == 0

# și mai alternativ
def is_even(n):
    return not n % 2 # nu faceți așa ceva, că nu mai citește nimeni

# Exercițiu:
# scrieți o funcție

def is_leap(year):
    pass # no-op, valid sintactic

# care detectează dacă anul este bisect.
#
# un an este bisect dacă:
# - este divizibil cu 4
# - dar nu este divizibil cu 100
#   - mai puțin în cazul în care este divizibil cu 400

def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

# varianta de super-erou
def is_leap(year):
    return year % 4 == 0 and (
        not (year % 100 == 0) or year % 400 == 0
    )

# varianta de programator care evită bug-uri
def is_leap(year):
    # de la cazul cel mai specific la cel mai puțin specific
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(2026, is_leap(2026)) # False
print(2020, is_leap(2020)) # True
print(2000, is_leap(2000)) # True
print(1900, is_leap(1900)) # False

# 3 modalități de a scrie o funcție care "returnează" None
def myfunc():
    pass
    # aceasta nu a returnat nimic

def myfunc():
    return
    # aceasta a returnat, dar... nimic

def myfunc():
    return None
    # aceasta a returnat nimic
