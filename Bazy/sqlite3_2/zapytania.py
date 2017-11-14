#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zapytania.py  

import sqlite3

def wyniki(cur):

    wyniki = cur.fetchall()  #feth - pobierz; fethall - pobierz wszystko
    for row in wyniki:# row - zmienna
        print(tuple(row))
    
    
def dodaj(cur):
    cur.execute(""" 
        INSERT INTO tbKlasy
        VALUES(?, ?, ?, ?)
    """, [None, '3C', 2015,2017])


def aktualizuj(cur):
    cur.execute("""
        Update tbKlasy
        SET klasa = ?
        Where idklasy = ?
    """, ['3D', 13 ])
    
def aktualizuj2(cur):
    cur.execute("""
        Update tbUczniowie
        SET EgzJez = ?
        Where idklasy = ?
    """, ['Paulina Dziedzic',8 ) 
    
    

def usun(cur):
    cur.execute('DELETE FROM tbKlasy WHERE klasa = ? AND roknaboru =?', ['3B', 2015])



def main(args):
    con = sqlite3.connect('szkola.db') # połączenie z bazą
    cur = con.cursor() #utworzenie kursora(gdy coś robię w bazie)
    con.row_factory = sqlite3.Row #możliwość odwoływania się do nazwy kolumn
    
    aktualizuj2(cur)
    #usun(cur)
    con.commit()
    wyniki(cur.execute('SELECT * FROM tbUczniowie'))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
