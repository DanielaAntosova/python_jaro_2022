def overeni_cisla():
    telcislo = input("Zadej telefonní číslo, kam chceš zprávu zaslat: ")
    if ("420" in telcislo):
        if (len(telcislo) == 12):
            return True
        else:
            return False
    else:
        if (len(telcislo) == 9):
            return True
        else:
            return False

print(overeni_cisla)