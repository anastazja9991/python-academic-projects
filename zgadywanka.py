# zadanie 4.

import random

slowa=("zgadywanka", "szkoła", "zadanie", "ocena", "losowanie")
word = random.choice(slowa)
dlugosc = len(word)
szansa = 0
poprawna = word

print("Oto słowo dla Ciebie. Składa się z",dlugosc,"liter. Możesz pięć razy zapytać o literę. Zaczynamy!")
x = input("Podaj literę: ")

for szansa in range (0,4):
    if x in poprawna:
        print("TAK!")
        szansa += 1
        print("Pozostały",5-szansa,"szanse")
        x = input("Podaj literę: ")
    elif x not in poprawna:
        print("NIE :( ")
        szansa += 1
        print("Pozostały",5-szansa,"szanse")
        x = input("Podaj literę: ")

    if szansa == 4:
        odp = input(print("Wykorzystałeś już 5 prób! Podaj odpowiedź: "))

if odp == poprawna:
    print("Zgadłeś słowo!")
else:
    print("Nie udało się :( ")


