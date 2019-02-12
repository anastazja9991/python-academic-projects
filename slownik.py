import os

def zapisz(slownik):
    pliktxt = open(plik, "w")
    for wyraz in slownik:
        znaczenie = slownik[wyraz]
        pliktxt.write(wyraz + ":" +znaczenie + "\n")
    pliktxt.close()

def wczytaj(plik):
    if os.path.isfile(plik):
        with open(plik, "r") as pliktxt:
            for linia in pliktxt:
                kluczWartosc = linia.split(":")
                klucz = kluczWartosc[0]
                znaczenie = kluczWartosc[1].replace("\n", "")
                slownik[klucz] = znaczenie
    return len(slownik)

slownik = {}
plik = "slowniczek.txt"
wczytaj(plik)
print("Podaj dane w formacie: wyraz obcy: znaczenie1, znaczenie2. Aby zakończyć wprowadzanie danych, wpisz koniec: ")
while True:
    wyraz = input()
    if wyraz == "koniec":
        break
    kluczWartosc = wyraz.split(":")
    if (len(kluczWartosc) != 2):
        print("Niepoprawny format")
        break
    klucz = kluczWartosc[0]
    wartosc = kluczWartosc[1]
    if slownik.__contains__(klucz):
        nadpisac = input("Definicja słowa " + klucz + " już istnieje. Czy nadpisać? (t/n)")
        if nadpisac == "t":
            slownik[klucz] = wartosc
    else:
        slownik[klucz] = wartosc
zapisz(slownik)

