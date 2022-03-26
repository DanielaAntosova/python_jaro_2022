'''Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:
Registrační značka 	Značka a typ vozidla 	Počet najetých kilometrů
4A2 3020 	Peugeot 403 Cabrio 	47534
1P3 4747 	Škoda Octavia 	41253

Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

    registrační značka automobilu,
    značka a typ vozidla,
    počet najetých kilometrů,
    informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).

Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut nastav jako True, tj. na začátku je vozidlo volné.

Vytvoř objekty, které reprezentují všechny automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát.'''

class Auto:
    def pujc_auto(self): #metoda třídy
        #self.volne = True
    #def __str__(self): 
        if self.volne is True:
            print("Potvrzuji zapůjčení vozidla")
            self.volne = False
        else:
            print("Vozidlo není k dispozici.")

    def get_info(self):  # metoda tridy
        return f"Registrační značka vozidla je {self.registrační_značka} a typ vozidla {self.značka_a_typ_vozidla}."

    def __init__(self, registrační_značka, značka_a_typ_vozidla, počet_kilometrů):
        self.registrační_značka = registrační_značka
        self.značka_a_typ_vozidla = značka_a_typ_vozidla
        self.počet_kilometrů = počet_kilometrů
        self.volne = True


Peugeot = Auto('4A23020', 'Peugeot_403_Cabrio', 47534)
Škoda = Auto('1P34747', 'Škoda_Octavia', 41253)

cosipřejepůjčit = input("Jakou značku si přejete půjčit? Škoda nebo Peugeot? ")

if cosipřejepůjčit == "Škoda":
  print(Škoda.get_info())
  Škoda.pujc_auto()
elif cosipřejepůjčit == "Peugeot":
  print(Peugeot.get_info())
  Peugeot.pujc_auto()
else:
  print("Toto k půjčení nemáme. Nechceš to zkusit ještě jednou?")

cosipřejepůjčit = input("Jakou značku si přejete půjčit? Škoda nebo Peugeot? ")

if cosipřejepůjčit == "Škoda":
  print(Škoda.get_info())
  Škoda.pujc_auto()
elif cosipřejepůjčit == "Peugeot":
  print(Peugeot.get_info())
  Peugeot.pujc_auto()
else:
  print("Toto k půjčení nemáme. Nechceš to zkusit ještě jednou?")









