# zadanie 1.

start = int(input("Podaj swoja liczbe poczatkowa: "))
stop = int(input("Podaj swoja liczbe koncowa: "))
odstep = int(input("Podaj wielkosc odstepu miedzy kolejnymi liczbami: "))


for i in range(start, stop, odstep):
    print(i, end=" ")

