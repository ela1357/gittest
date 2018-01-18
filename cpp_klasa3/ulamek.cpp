/*
 * ulamek.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

class Ulamek {
private:
    int licznik; // deklaracja składowej właściwości
    int mianownik;
public:
    Ulamek(int, int); // deklaracja konstruktora, zwraca obiekty, metoda specjalna
    void zapisz(int, int); // deklaracja metody
    void wypisz() {
        cout << licznik << "/" << mianownik;
    }
    int get_l() {
        return licznik;
    }
    int get_m() {
        return mianownik;
    }
    void skracaj(); // metoda drukuje skróconą postać ułamka
};

void Ulamek::skracaj() {
    ; // wykorzystaj algorytm euklidesa optymalny
}

void Ulamek::zapisz(int l, int m) {
    licznik = l;
    if (m != 0) mianownik = m;
    else {
        cout << "Mianownik nie może być zerem!";
        exit(1);
    }
}

Ulamek::Ulamek(int l, int m) {
    licznik = l;
    if (m != 0) mianownik = m;
    else {
        cout << "Mianownik nie może być zerem!";
        exit(1);
    }
}

int main(int argc, char **argv)
{
	//Ulamek u1, u2; // deklaracja obiektu, czyli instacji klasy
    Ulamek u1(3, 7); // definicja obiektu
    Ulamek u2(1, 4); // definicja obiektu
	//u1.zapisz(3, 7);
    //u2.zapisz(1, 4);
    cout << "Ułamek 1: ";
    u1.wypisz();
    cout << endl << "Ułamek 2: ";
    u2.wypisz();
    
    u1.zapisz(7, 9);
    cout << endl << "Licznik: " << u1.get_l() << endl;
    cout << "Mianownik: " << u1.get_m() << endl;
    
    Ulamek u3(u1.get_l(), u1.get_m());
    u3.wypisz();
    
    return 0;
}

