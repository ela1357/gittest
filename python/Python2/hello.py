#!/usr/bin/env python
# -*- coding: utf-8 -*-

ROK_TERAZ = 2017
ROK_PYTHON = 1991

def parzyste(n):
    ile = list(range(0, n + 1, 2))
    print(ile)
    return len(ile)

def main(args):
    imie = input("Jak się nazywasz?")
    print("Witaj", imie)
    wiek = int(input("Ile masz lat?"))
    print("Urodziłeś się w ", ROK_TERAZ - wiek)
    
    n = int(input("Podaj liczbę: "))
    print("Parzystych: ", parzyste(n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
