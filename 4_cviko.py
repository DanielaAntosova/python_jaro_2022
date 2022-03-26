# Balík
'''Uvažuj, že navrhuješ software pro zásilkovou společnost.

    Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno. První dva atributy nastav pomocí parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.
    Připoj ke třídě funkci deliver, která změní hodnotu parametru doruceno na True.
    Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
    Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.'''

class Package:
    def deliver(self): #metoda třídy
        self.delivered = True
    def __str__(self): 
        if self.delivered is True:
            deliveredText = "Balík byl doručen"
        else:
            deliveredText = "Balík zatím nebyl doručen."
        print(f"Balík je na adresu {self.address} a váží {self.weightInKilos}. {deliveredText}")
    def __init__(self, address, weightInKilos): #spustí se automaticky při vytváříme nový objekt
        self.address = address # parametr
        self.weightInKilos = weightInKilos # parametr
        self.delivered = False # parametr


valuablePackage = Package("Plzeňská 123, Praha", "2 kila")
valuablePackage.__str__()
valuablePackage.deliver()
valuablePackage.__str__()

#kniha

'''Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Kniha, která reprezentuje knihu. Každá kniha bude mít atributy nazev, pocet_stran a cena. Hodnoty nastav ve funkci __init__.

    Přidej knize funkci __str__, která vypíše informace o knize v nějakém pěkném formátu.
    Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. Přidej metodu sleva(), která bude mít jeden parametr - velikost slevy v procentech. Funkce sníží cenu knihy o dané procento.'''

class Book:
    def discount(self, discountInPercents):
        self.price *= (1 - discountInPercents/100)
    def __str__(self):
        print(f"Název knihy: {self.title}. Počet stran: {self.pages}. Cena: {self.price}")
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

kniha = Book("Noc, která mě zabila", 590, 499)
kniha.__str__()
kniha.discount(10)
kniha.__str__()





