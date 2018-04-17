#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt


def pierwiastek(x, d):
    a = x
    while a - x / a > d:
        a = (a + x / a) / 2
    return a


def main(args):
    x = float(input("Podaj liczbę: "))
    d = float(input("Podaj dokładność: "))

    print("Przybliżona wartość pierwiastka: {:.8f}".format(pierwiastek(x, d)))
    print("Pierwiastek z {:.3f} wynosi {:.8f}".format(x, sqrt(x)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
