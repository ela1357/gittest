#ifndef ULAMEK_H
#define ULAMEK_H
/*
 * plik nagłówkowy klasy Ulamek
 * 
 */

class Ulamek {
private:
    int licznik; // deklaracja składowej właściwości
    int mianownik;
public:
    Ulamek(int, int); // deklaracja konstruktora, zwraca obiekty, metoda specjalna
    void zapisz(int, int); // deklaracja metody
    void wypisz();
    int get_l();
    int get_m();
    void skracaj(); // metoda drukuje skróconą postać ułamka
};
#endif
