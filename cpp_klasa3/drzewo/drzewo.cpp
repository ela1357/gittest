/*
 * drzewo_bin.cpp
 * 
 * Copyright 2018  <>
 * 
 */


#include <iostream>
#include "drzewo.hpp"

using namespace std;

int Drzewo::stworzWezel(int wartosc) {
    Wezel *nowyWezel = new Wezel;
    nowyWezel->wartosc = wartosc;
    nowyWezel->lewy = NULL;
    nowyWezel->prawy = NULL;
    
    return nowyWezel;
}

void Drzewo::dodajWezel(Wezel *wezel, int wartosc) {
    if (korzen == NULL) { // drzewo jest puste
        korzen = stworzWezel(wartosc); // utworzenie 1. elementu
    } else {
        if (wartosc < wezel->wartosc) { // wstawiamy wartość do lewego poddrzewa
            if(wezel->lewy != NULL) {
                dodajWezel(wezel->lewy, wartosc); // rekurencyjne wywołanie dodawania do lewego poddrzewa
            } else { // lewy potomek nie istnieje
                wezel->lewy = stworzWezel(wartosc); // tworzymy nowy węzeł
            }
        } else { // wstawiamy wartość do prawego poddrzewa
            if(wezel->prawy != NULL) {
                dodajWezel(wezel->prawy, wartosc); // rekurencyjne wywołanie dodawania do prawego poddrzewa
            } else { // lewy potomek nie istnieje
                wezel->prawy = stworzWezel(wartosc); // tworzymy nowy węzeł
            }
        }
    }
}

// funkcja rekurencyjnie przegląda drzewo
void Drzewo::wyswietlRosnaco(Wezel *wezel) {
    if (wezel != NULL) { // jeżeli węzeł nie jest punty
        // rekurencyjnie wyświetl lewe poddrzewo
        wyswietlRosnaco(wezel->lewy);
        // wypisz wartość akyualnego węzła
        cout << wezel->wartosc << ", ";
        // rekurencyjnie wyświetl prawe poddrzewo
        wyswietlRosnaco(wezel->prawy);
    }
}

void Drzewo::wyswietlMalejaco(Wezel *wezel) {
    if (wezel != NULL) { // jeżeli węzeł nie jest pusty
        // rekurencyjnie wyswietl lewo poddrzewo
        wyswietlMalejaco(wezel->prawy);
        // wypisz wartość aktualnego węzła
        cout << wezel->wartosc << ", ";
        // rekurencyjnie wyswietl prawe poddrzewo
        wyswietlMalejaco(wezel->lewy);
    }
}
