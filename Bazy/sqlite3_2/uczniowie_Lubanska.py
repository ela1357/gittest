#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zapytania.py
import sqlite3


def kw_a(cur):
    cur.execute("""
        SELECT Imie, Nazwisko, tbKlasy.Klasa
        FROM tbUczniowie, tbKlasy
        WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
        AND Klasa LIKE '1A'
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

def kw_b(cur):
    cur.execute("""
        SELECT MAX(EgzHum)
        FROM tbUczniowie
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
    
def kw_c(cur):
    cur.execute("""
        SELECT AVG(EgzMat)
        FROM tbUczniowie
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

def kw_d(cur):
    cur.execute("""
        SELECT Imie, Nazwisko, tbOceny.Ocena, tbPrzedmioty.Przedmiot
        FROM tbUczniowie, tbOceny, tbPrzedmioty
        WHERE tbOceny.UczenID = tbUczniowie.IDUcznia
        AND tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
        AND Nazwisko LIKE 'Nowak'
    """)

    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

        
def kw_e(cur):
    cur.execute("""
        SELECT AVG(Ocena), Przedmiot, Datad
        FROM tbPrzedmioty, tbOceny
        WHERE tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
        AND Przedmiot LIKE 'fizyka'
        AND strftime('%m', Datad) LIKE '10'
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor() # utworzenie kurosra
    con.row_factory = sqlite3.Row
    
    # kw_a(cur)
    # kw_b(cur)
    # kw_c(cur)
    # kw_d(cur)
    kw_e(cur)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
