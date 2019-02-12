# zadanie 7.

x = 3

def szyfruj(txt):
    zaszyfrowany = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - x:
            zaszyfrowany += chr(ord(txt[i]) + x - 26)
        else:
            zaszyfrowany += chr(ord(txt[i]) + x)
    return zaszyfrowany


def main(args):
    tekst = input("Podaj ciąg do zaszyfrowania:\n")
    print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
