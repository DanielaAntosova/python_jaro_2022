'''ukol-08: Prodej vstupenek

Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.
Datum 	Cena
1. 7. 2021 - 10. 8. 2021 	250 Kč
11. 8. 2021 - 31. 8. 2021 	180 Kč

Mimo tato data je středisko zavřené.

Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().

Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za ubytování.

Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=. Tyto operátory můžeš použít v podmínce if. Níže vidíš příklad porovnání dvou dat. Program vypíše text "První datum je dřívější než druhé datum.'''

import datetime
from datetime import datetime

první_den_sezony_250 = datetime(2021, 7, 1)
poslední_den_sezony_250 = datetime(2021, 8, 10)
první_den_sezony_180 = datetime(2021, 8, 11)
poslední_den_sezony_180 = datetime(2021, 8, 31)

datum = input("Datum RRRR, MM, DD: ")
počet_osob = int(input("Počet osob: "))
datum = datetime.strptime(datum, "%Y, %m, %d")

if datum < první_den_sezony_250 or datum > poslední_den_sezony_180:
    print("V této době je letní kino uzavřené.")
elif datum >= první_den_sezony_250 and datum <= poslední_den_sezony_250:
    cena = počet_osob * 250
    print(cena)
elif datum >= první_den_sezony_180 and datum <= poslední_den_sezony_180:
    cena = počet_osob * 180
    print(cena)






