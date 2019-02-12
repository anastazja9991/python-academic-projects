# zadanie 8.

import math

a = int(input("Podaj długość pierwszego boku: "))
b = int(input("Podaj długość drugiego boku: "))
c = int(input("Podaj długość trzeciego boku: "))

if a + b > c and a + c > b and b + c > a:
    print("")
    print("Z podanych boków można zbudować trójkąt.")
    print("")
    print("Obwód wynosi:", (a + b + c))
p = 0.5 * (a + b + c)
P = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Pole wynosi:", P)


if (a**2 + b**2 == c**2 or
        a**2 + c**2 == b**2 or
            b**2 + c**2 == a**2):
                print("Jest to trójkąt prostokątny.")

else:
    print("")
    print("Z podanych boków nie można zbudować trójkąta prostokątnego.")
