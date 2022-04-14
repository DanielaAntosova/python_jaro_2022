'''Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

Napište program, který na výstup vypíše součet všech ujetých kilometrů.'''

nazev_souboru = "C:/Users/Danca/Documents/python_jaro/python_jaro_2022/auta.txt"

with open(nazev_souboru, encoding="utf-8") as vstup:
    auta = vstup.readlines()

auta_ocistena = [auto.strip() for auto in auta]
auta_ocistena = [auto.split() for auto in auta]

#strip = zbaví nás mezer na začátku a na konci
#split = rozdělí řetězec podle mezer

auta_pripravena_ke_scitani = [float(auto[1].replace(",", ".")) for auto in auta_ocistena]
print(f"Počet najetých kilometrů je: {sum(auta_pripravena_ke_scitani)} tisíc kilometrů")









