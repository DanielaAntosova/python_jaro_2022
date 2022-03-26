#Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.
from pickle import TRUE
from xmlrpc.client import Boolean


def mult(a, b):
    return a * b

print(mult(3,4))

#Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.
def total_price(persons: int, breakfast: Boolean =False): #dva parametry, persons je povinný - nemá žádnou základní defaultní hodnotu a druhý je nepovinný - defaultní hodnotu má
#zadám jen povinný parametr (persons) total_price(3)
#zadám oba parametry- python odvodí podle pozice total_price(3, True)
# zadám oba parametry total_price(3, breakfast=True)
# zadám oba parametry podle názvu (persons=3, breakfast=True)

    if breakfast == True:
      return persons * 850 + persons * 125
    if breakfast == False:
      return persons * 850
    
print(total_price(3))


def total_price(persons, breakfast=False):
    pricePerPerson = 850
    if breakfast is True:
        pricePerPerson += 125
    return pricePerPerson * persons

print(total_price(3))
print(total_price(3, True))

def monthOfBirth(birthNumber):
    month = birthNumber[2] + birthNumber[3]
    month = int(month)
    month = month - 50 
    return month

print(monthOfBirth("9461124387"))

