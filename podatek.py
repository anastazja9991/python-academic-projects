# zadanie z podatkiem

umowa = input("Jeśli jesteś zatrudniony na umowę o pracę wciśnij 'a', jeśli na zlecenie, wciśnij 'b'")
if umowa == "a":
    brutto = float(input("Podaj wysokość wynagrodzenia brutto: "))
    skladkaEmerytalna = brutto * 0.0976
    skladkaRentowa = brutto * 0.015
    skladkaChorobowa = brutto * 0.0245
    sumaSkladek = (skladkaEmerytalna + skladkaRentowa + skladkaChorobowa)
    podstawaSkladkiZdrowotne = brutto - sumaSkladek
    skladkaZdrowotnaDoZaplaty = podstawaSkladkiZdrowotne * 0.09
    skladkaZdrowotnaDoOdliczenia = podstawaSkladkiZdrowotne * 0.0775
    kosztyUzyskaniaPrzychodow = 111.25
    podstawaZaliczkiNaPit = (brutto - kosztyUzyskaniaPrzychodow - sumaSkladek)
    zaliczkaNaPit = (podstawaZaliczkiNaPit * 0.18) - 46.33 - skladkaZdrowotnaDoOdliczenia
    netto = round((brutto - sumaSkladek - skladkaZdrowotnaDoZaplaty - zaliczkaNaPit),2)
    print("Twoje wynagrodzenie netto to:", netto)


elif umowa == "b":
    brutto = float(input("Podaj wysokość wynagrodzenia: "))
    skladkiZleceniobiorcy = float(brutto * 0.1371)
    podstawaSkladkiZdrowotne = brutto - skladkiZleceniobiorcy
    skladkiZdrowotne9 = podstawaSkladkiZdrowotne * 0.09
    skladkiZdrowotne775 = podstawaSkladkiZdrowotne * 0.0775
    kosztyUzyskaniaPrzychodow = (brutto - skladkiZleceniobiorcy)*0.2
    podstawaOpodatkowania = brutto - (kosztyUzyskaniaPrzychodow + skladkiZleceniobiorcy)
    zaliczkaNaPodatek = int(podstawaOpodatkowania * 0.18)
    zaliczkaDoUS = zaliczkaNaPodatek - skladkiZdrowotne775
    netto = round(brutto - (skladkiZleceniobiorcy + skladkiZdrowotne9 + zaliczkaDoUS),2)
    print("Zaliczka na podatek:", zaliczkaNaPodatek)
    print("Twoje wynagrodzenie netto to:", netto)






