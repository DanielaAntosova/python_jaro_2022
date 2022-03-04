baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kód = input("Zadej kód balíku: ")
if kód in baliky:
  jo_nebo_ne = baliky[kód]
  if jo_nebo_ne == True:
    print("Balík byl předán kurýrovi.")
  else:
    print("Balík zatím nebyl předán kurýrovi.")
else:
    print("Máš blbý kód.")