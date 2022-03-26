from operator import itemgetter


sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

#print(sales.keys())
#print(sales.values())
#print.items()) všechny dvojice (klíče, hodnota)

'''nazvy = ['Zkus mě chytit', 'Vrah zavolá v deset', 'Zločinný steh']
for nazev in nazvy:
    print(nazev)

for nazev in nazvy:
  if len(nazev) > 15:
    print(f"")

jmeno = "lenka"
for pismeno in jmeno:
    print(pismeno)
    print(pismeno.uppper())'''

'''for book in sales:
  if len(book) > 15:
    print(book) # chci dostat klíč
    print(sales[book]) #chci dostat hodnotu
    print(f'Titulu {book} se prodalo {sales[book]} ks.')'''

'''print(sales.items())
for book, count in sales.items():
    if len(book) > 15:
        print(f'Titulu {book} se prodalo {sales[count]} ks.')'''

for item in sales.items():
    key, value = item
    key = item[0]
    value = item[1]
    print(item)
