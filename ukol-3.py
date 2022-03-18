from math import floor
def stanoveni_ceny():
    zprava = input("Zadej zprávu, kterou chceš napsat: ")
    delka = len(zprava)
    cena = floor((delka/180 + 1))*3
    return cena
def overeni_cisla():
      telcislo = input("Zadej telefonní číslo, kam chceš zprávu zaslat: ")
      if (telcislo[0:3] == "420"):
        if (len(telcislo) == 12):
            return True and print(stanoveni_ceny())
        else:
            return False
      else:
        if (len(telcislo) == 9):
            return True and print(stanoveni_ceny())
        else:
            return False
print(overeni_cisla())







'''def total_price(persons, breakfast=False):
    pricePerPerson = 850
    if breakfast is True:
        pricePerPerson += 125
    return pricePerPerson * persons'''