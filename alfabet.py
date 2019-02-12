# zadanie 9.

print("Alfabet od dużej litery do małej:")

for i in range(65, 91):
    litera = chr(i)

    tmp = litera + litera.lower()
    if i >= 65 and i<= 91:
        print(tmp, end="")


print("\nAlfabet od małej litery do dużej:")

for i in range(97, 123):
    litera = chr(i)

    tmp = litera + litera.upper()
    if i >= 97 and i<= 123:
        print(tmp, end="")
