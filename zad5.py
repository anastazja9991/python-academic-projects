# zadanie 5.

from lab2zadNaZaliczenie.zad5.zad5funkcje import *

przedmiot = input("Podaj nazwę przedmiotu, dla którego chcesz wprowadzić oceny: ")

oceny = []
print("\nAby przerwać wprowadzanie ocen, wpisz 0 (zero).")

while True:
    ocena = int(input("Podaj ocenę (1-6): "))
    if (ocena > 0 and ocena < 7):
        oceny.append(float(ocena))
    elif ocena == 0:
        break
    else:
        print("Błędna ocena.")

drukuj(oceny, przedmiot.capitalize() + " - wprowadzone oceny: ")
s = srednia(oceny)
m = mediana(oceny)
o = odchylenie(oceny, s)
print("\nŚrednia: {0:5.2f}".format(s))
print("Mediana: {0:5.2f}\nOdchylenie: {1:5.2f}".format(m, o))


