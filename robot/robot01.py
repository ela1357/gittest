#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:

    def act(self, game):

        # typy pól: 'spawn' - wejście, 'normal' - pole na które moge wejść,
        # 'obstacle' - pola na które nie mozna wejść,
        # 'invalid' - pole nie należy do planszy
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

        # print(game.robots)

        def czy_wrog(poz):
            if game.robots.get(poz) is not None:
                if game.robots[poz].player_id != self.player_id:
                    return True
            return False

        # funkcja zwróci prawdę,jeżeli w odległości 2 kroków z przodu jest wróg
        def zprzodu(l1, l2):
            if rg.wdist(l1, l2) == 2:
                if abs(l1[0] - l2[0]) == 1:
                    return False
                else:
                    return True
            return False

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

        if czy_wejscie(self.location):
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        # funkcja zwróci współrzędne pola środkowego między dwoma innymi
        # oddalonymi o 2 kroki
        def miedzypole(p1, p2):
            return (int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2))

        for poz, robot in game.get('robots').items():
            if czy_wrog(poz):
                if rg.wdist(poz, self.location) == 2:
                    if zprzodu(poz, self.location):
                        return ['attack', miedzypole(poz, self.location)]
                    if rg.wdist(rg.toward(loc, rg.CENTER_POINT), self.location) == 1:
                        return ['attack', rg.toward(poz, rg.CENTER_POINT)]
                    else:
                        return ['attack', (self.location[0], poz[1])]

        if len(lista_wrogow_obok) > 2 and self.hp < 27:
            return['suicide']
        elif len(lista_wrogow_obok):
            return['attack', lista_wrogow_obok[0]]

        # jeżeli jesteś w środku, popełnij samobójstwo
        # if self.location == rg.CENTER_POINT:
        #    return ['guard']

        # idź do środka planszy, ruch domyślny
        dystansCP = rg.wdist(self.location, rg.CENTER_POINT)
        # if czy_wejscie(self.location):
        if dystansCP > 6:
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        return ['guard']
