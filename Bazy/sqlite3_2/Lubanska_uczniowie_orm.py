# -*- coding: utf-8 -*-


from peewee import *
#from dane import *

baza_plik = "szkola.sqlite3"
baza = SqliteDatabase(baza_plik)  # ':memory:'

class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    rok_naboru = IntegerField(null=False)
    rok_matury = IntegerField(null=False)


class Przedmiot(BazaModel):
    nazwa = CharField(null=False)
    imien = CharField(null=False)
    nazwiskon = CharField(null=False)
    plecn = IntegerField()


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = IntegerField(null=False)
    klasa_id = ForeignKeyField(Klasa, related_name='szkola')
    egzhum = IntegerField(null=False)
    egzmat = IntegerField(null=False)
    egzjez = IntegerField(null=False)


class Ocena(BazaModel):
    datad = DateField(null=False)
    uczen_id = ForeignKeyField(Uczen, related_name='szkola')
    przedmiot_id = ForeignKeyField(Przedmiot, related_name='szkola')
    ocena = DecimalField(decimal_places=2, default=0)

baza.connect()

def kwerenda_a():
    query = (Uczen
            .select(Uczen.klasa_id)
            .group_by(Uczen.klasa_id.startswith('1A'))
            )

    for obj in query:
        print(obj.Uczen.imie, obj.Uczen.nazwisko)
