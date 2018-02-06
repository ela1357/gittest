/*
 * lista.cpp
 * 
 * Copyright 2018  <>
 * 
 */


#include <iostream>
#include "lista.hpp"

Lista::Lista(){
    head = NULL;
    tail = NULL;
}

Lista::~Lista(){
    while(Usun()) {;};
}

void Lista::Dodaj(int wartosc) {
    ELEMENT *el = new ELEMENT;
    el->wartosc = wartosc;
    el->nast = NULL;
    if (head == NULL) { // dodanie pierwszego elementu listy
        head = el;
        tail = el;
    } else {
        tail->nast = el; // ustawienie wskaźnika nast dotychczasowego 
        // ostatniego elementu na dres nowego ostatniego elementu
        tail = el; // aktualizujemy wskaźnik ogon aby wskazywal na nawy dodany element
    }
}

void Lista::Wyswietl() {
    ELEMENT *el = head;
    while (el != NULL) {
        std::cout << el->wartosc << " "; // zamiast using namespace std;
        el = el->nast;
    }
    std::cout << std::endl;
}

bool Lista::Usun() {
    if (head != NULL) {
        if(head == tail) {
            delete head; // usuwa element a nie wskażnik
            head = NULL;
            tail = NULL;
        } else {
            ELEMENT *el = head;
            while(el->nast != tail) { // szukam przedostatniego elementu
                el = el->nast; // zapis adresu przedostatniego elementu
            }
            delete el->nast;
            el->nast = NULL;
            tail = el;
        }
        return true;
    }
    return false;
}

void Lista::Wstaw(int pozycja, int wartosc) {
    ;
}
