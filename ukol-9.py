'''ukol-08: Adopce zvířat

Stáhni si dataset, který obsahuje seznam zvířat k adopci v ZOO Praha. Zdroj dat je Národní katalog otevřených dat.

    Data si načti pomocí metody pandas.read_csv(). Pozor, nastav oddělovač na znak středníku. Využij parametr sep.

    Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?

    Které zvíře se nachází na záznamu s indexem 34? Vypiš pomocí iloc název tohoto zvířete v češtině i angličtině.'''

import pandas
zvirata = pandas.read_csv("adopce-zvirat.csv", sep=";")
print(zvirata.shape)
print(zvirata.columns)
print(zvirata.iloc[34, 1:3])

'''Bonus

V lekci jsme zmínili, že existují i jiné typy indexů, než jen číselný, který sám vyrobí pandas. Například v kontextu souboru se zvířaty se nabízí hned několik sloupců, které bychom mohli využít jako index, které nejsou číselné.

    Načti znovu data, ale tentokrát nastav parametr index_col na název sloupce, který obsahuje název zvířete v češtině. Všimni si, že sloupec teď povýší na index a už se nenachází mezi "běžnými" sloupci.

    Pomocí <tvoje-promenna>.index.is_unique ověř, zda je nový index unikátní.

    Seřazený index je efektivnější a přehlednější. Seřaď index pomocí metody .sort_index(). Bacha, metoda vrátí novou tabulku se seřazeným indexem. Budeš tedy chtít přepsat původní tabulku.

    Vyhledej řádek indexovaný názvem "Outloň váhavý". Namísto metody .iloc využij .loc.

    Rozsahy fungují podobně jako u číselných indexů. Vyhledej záznamy mezi "Želva Smithova" a "Želva žlutočelá".'''

zvirata = pandas.read_csv("adopce-zvirat.csv", sep=";", index_col="nazev_cz")
print("\nIs the Pandas index having unique values?\n",zvirata.index.is_unique)
zvirata = zvirata.sort_index()
print(zvirata.loc["Outloň váhavý"])
print(zvirata.loc["Želva Smithova":"Želva žlutočelá"])




