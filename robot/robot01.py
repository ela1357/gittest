#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:

    def act(self, game):

        # typy pól: 'spawn' - wejście, 'normal' - pole na które moge wejść,
        # 'obstacle' - pola na które nie mozna wejść, 'invalid' - pole nie należy do planszy
        # rg.loc_types() - zwraca typy pola
        # funkcja zwróci prawdę, jeżeli "poz" wskazuje punkt wejścia
        def czy_wejscie(poz):
            if 'spawn' in rg.loc_types(poz):
                return True
            return False

        # return ['guard']
        # return ['suicide']
        # return ['move', (4,5)]
        # return ['attack', (5, 4)]
        # ilu_wrogow = 0

        print(game.robots)

        lista_wrogow_obok = []

        # jeżeli obok są przeciwnicy, atakuj
        # wersja z pętlą przeglądającą wszystkie pola zajęte przez roboty
        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:  # rozpoznanie wroga
                # print(rg.dist(poz, self.location))
                if rg.dist(poz, self.location) <= 1:
                    lista_wrogow_obok.append(poz)
                    # ilu_wrogow +=1
                    # return ['attack', poz]

        print(lista_wrogow_obok)

        # rg.toward() - najkrótsza droga pomiędzy dwoma lokalizacjami
        # eg.dist() _ odległość miedzy dwoma lokalizacjami

        if len(lista_wrogow_obok) > 2 and self.hp < 27:
            return['suicide']
        elif len(lista_wrogow_obok):
            return['attack', lista_wrogow_obok[0]]

        # jeżeli jesteś w środku, popełnij samobójstwo
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # idź do środka planszy, ruch domyślny
        if czy_wejscie(self.poz):
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

