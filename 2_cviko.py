#Uvažujme vysvědčení, které máme zapsané jako slovník.

#Napiš program, který spočte průměrnou známku ze všech předmětů.
    #Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}
suma_znamek = 0

for znamka in school_report.values:
      suma_znamek += znamka
print(f"Průměrná známka {suma_znamek/len(school_report)}.")


'''for x, y in school_report.items():
    if y == 1:
        print(x)
'''


for znamka in school_report.values():
    if znamka == 1:
            print(school_report.keys)

'''Proč to mám blbě
Plus tady jsme pracovali už s klíčem a s hodnotou, proto už jsme nepoužívali .values, ale .items
Protože jsme chtěli nejdřív zjistit předmět kde má 1, tak to byla hodnota. A následně jsme chtěli vypsat jaké to jsou předměty, takže to byl klíč'''



'''Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

    Napiš program, který spočte celkový počet stran, které Gustav přečetl.
    Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.'''

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

totalPages = 0
for book in books:
    totalPages += book["pages"]
print(f"Gustav celkem přečetl {totalPages} stran.")

pocet_dobrych_knih = 0
for book in books:
  if book["rating"] >= 8:
    pocet_dobrych_knih += 1
    print(pocet_dobrych_knih)

dobre_knihy = []
pocet_dobrych_knih = 0
pocet_dobrych_stranek = 0

for book in books:
    if book["rating"] >= 8:
        pocet_dobrych_knih += 1
        pocet_dobrych_stranek += book["pages"]
        dobre_knihy.append(book["title"])  # pridej na konec seznamu

print(dobre_knihy)
print(pocet_dobrych_knih)
print(pocet_dobrych_stranek)

'''V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.'''

plates = {
    "4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"
  }

for spz in plates:
    if spz[1] == "P":
        print(f"Majitel auta {plates[spz]} ma SPZ z Plzenskeho kraje: {spz}")






