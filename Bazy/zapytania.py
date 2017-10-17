#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zapytania.py
import sqlite3


def kw_c(cur):
    cur.execute("""
        SELECT siedziba, SUM(placa) AS pensje
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial = dzial.id
        GROUP BY siedziba
        ORDER BY pensje ASC
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

def kw_d(cur):
    nazwa = input("Podaj nazwę działu: ")
    siedziba = input("Podaj nazwę siedziby: ")
    print(nazwa, siedziba)
    
    cur.execute("""
        SELECT nazwisko, imie, dzial.id, dzial.nazwa, dzial.siedziba
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial = dzial.id
        AND dzial.nazwa = ?
        AND siedziba = ?
    """, (nazwa, siedziba))
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
    
def kw_e(cur):
    cur.execute("""
        SELECT nazwisko, stanowisko,
        pracownicy.placa *
        (SELECT premia.premia
        FROM premia
        WHERE pracownicy.stanowisko = premia.id) 
        AS premia
        FROM pracownicy
        ORDER BY premia DESC
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

def kw_f(cur):
    cur.execute("""
        SELECT AVG(placa)
        FROM pracownicy 
        WHERE imie LIKE '%a'
    """)

    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

    cur.execute("""
        SELECT AVG(placa)
        FROM pracownicy 
        WHERE imie NOT LIKE '%a'
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))
        
def kw_g(cur):
    cur.execute("""
        SELECT imie, nazwisko, stanowisko,
        (JulianDay())
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

def main(args):
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor() # utworzenie kurosra
    con.row_factory = sqlite3.Row
    
    # kw_c(cur)
    # kw_d(cur)
    # kw_e(cur)
    kw_f(cur)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
