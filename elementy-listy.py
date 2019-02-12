# zadanie 10.

lista = []
liczby = int(input("Podaj ile liczb chcesz wprowadzić: "))


for i in range(liczby):
    lista.append(int(input("Podaj liczby: ")))

    # ELEMENTY LISTY I ICH INDEKSY
print("")
print("Elementy listy i indeksy: ")
for i, x in enumerate(lista):
    print(x, "[",i,"]")

    # ELEMENTY W ODWROTNEJ KOLEJNOŚCI
print("Elementy w odwrotnej kolejności: ")
for x in reversed(lista):
    print(x)

    # ELEMENTY POSORTOWANE
print ("")
print("Elementy posortowane: ")
for x in sorted(lista):
    print(x)

    # USUŃ PIERWSZE WYSTĄPIENIE PODANEGO ELEMENTU
print ("")
x = int(input("Którą liczbe usunąć? "))
lista.remove(x)
print(lista)

    # USUŃ ELEMENT O PODANYM INDEKSIE
print("")
x = int(input("Podaj numer indeksu liczby, którą chcesz usunąć: "))
lista.remove(lista[x])
print(lista)

    # INDEKS PIERWSZEGO WYSTĄPIENIA ORAZ ILOŚĆ WYSTĄPIEŃ PODANEGO ELEMENTU
print("")
x = int(input("Podaj liczbę dla której mam zliczyć ilość wystąpień oraz podać jej indeks: "))
print("")
print("Liczba, którą wskazałeś występuje w liście",lista.count(x),"razy,")
print("a indeks jej pierwszego wystąpienia to",lista.index(x),".")

    # ELEMENTY Z LISTY OD INDEKSU i DO j
print("")
i = int(input("Podaj indeks początkowy: "))
j = int(input("Podaj indeks końcowy: "))
print(lista[i:j+1])
