'''ukol-10: Teplota ve městech

Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.

Dále napiš následující dotazy:

    Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.
    Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
    Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
    Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.'''

import pandas
#pandas.set_option('display.max_rows', None)

teplota = pandas.read_csv("temperature.csv")
print(teplota.head())

teplota = teplota.set_index("City")
print(teplota.loc["Prague"])

velké_vedro_80_min = teplota["AvgTemperature"] > 80
print(velké_vedro_80_min)

střední_vedro_60_min = teplota["AvgTemperature"] > 60

Evropa = teplota["Region"].isin(["Europe"])
print (teplota[střední_vedro_60_min & Evropa])

příšerná_klendra = teplota["AvgTemperature"] < -20
print (teplota[velké_vedro_80_min|příšerná_klendra])






