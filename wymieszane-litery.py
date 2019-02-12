# zadanie 3.

import random

slowa = ("python","gdansk","bagietka","gdynia","wsb")
podpowiedzi = ("Skryptowy język programowania.", "Miasto nad morzem.", "Długa bułka z Francji.", "Miasto portowe w Polsce.", "Jedna z wyższych uczelni, m.in. w Gdańsku.")
index = random.randrange(len(slowa))
word = slowa[index]
punkty = 0
podpowiedz = podpowiedzi[index]
#print (word)
poprawnie = word
pomie =""
while word:
    position = random.randrange(len(word))
    pomie += word[position]
    word = word[:position] + word[(position + 1):]
    print(pomie)

print(
"""
Witaj w grze 'Wymieszane litery'!  Uporządkuj litery, aby odtworzyć prawidłowe słowo. (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", pomie)
print("W celu skorzystania z pomocy, wcisnij 'h'")
zgaduj = input("\nTwoja odpowiedź: ")
while zgaduj != poprawnie and zgaduj != "":
    if (zgaduj  == 'h'):
        print(podpowiedz)
        punkty = punkty - 10
    else :
        print("Niestety, to nie to słowo.")
        punkty = punkty - 1
    zgaduj = input("Twoja odpowiedź: ")

if zgaduj == poprawnie:
    print("Zgadza się! Zgadłeś!\n")
    punkty = punkty + 100
    print("Dziękuję za udział w grze.")
    print("Twoje punkty: ", punkty)
