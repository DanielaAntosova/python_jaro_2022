# definice funkce
def pozdrav():
    print("Ahoj!")

# volani funkce
pozdrav()

# definice funkce
def pozdrav(jmeno: str):
    print(f"Ahoj {jmeno}!")

# volani funkce
jmeno_uzivatele = input("Zadej tve jmeno: ")

pozdrav(jmeno_uzivatele)

# definice funkce
def pozdrav(jmeno: str):
    print(f"Ahoj {jmeno}!")
    print("Vitej u nas ve firme")

# volani funkce
jmeno_zamestnance = input("Zadej tve jmeno: ")
jmeno_manazera = input("Zadej jmeno nadrizeneho: ")

pozdrav(jmeno_zamestnance)
pozdrav(jmeno_manazera)

# varianta 1
def secti_dve_cisla(a, b):
    vysledek = a + b
    return vysledek

# varianta 2
def secti_dve_cisla(a, b):
    return a + b


vysledek_souctu = secti_dve_cisla(1, 2)
print(vysledek_souctu)

def prevod_eur_na_czk(pocet_eur: int):
    """
    Funkce prevadi eura na koruny 
    s pevnym kurzem 25kc.
    """
    kurz = 25
    return pocet_eur * kurz

print(prevod_eur_na_czk(10))

def prevod_eur_na_czk(pocet_eur: int, kurz: float = 25):
    """
    Funkce prevadi eura na koruny 
        """
    return pocet_eur * kurz

print(prevod_eur_na_czk(pocet_eur=10, kurz=24.7))#když zde nezadám vysloveně kurz, tak se mi tam dá ten defaultní viz výše

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