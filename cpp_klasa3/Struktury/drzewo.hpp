#ifndef DRZEWO_HPP
#define DRZEWO_HPP

struct Wezel{ // rekurencyjny sposób deklarowania listy
    int wartosc;
    Wezel *lewy; // wskaźnik do nastepnego elementu listy
    Wezel *prawy;
};

class Drzewo {
    private: // hermetyzacja danych
        Wezel *korzen;
        Wezel* stworzWezel(int);
    public: // interfejs publiczny (API klasy)
        Drzewo(); // konstruktor
        ~Drzewo (); // destruktor, sprząta po klasie // memory leaks - wycieki pamięci
        void dodajWezel(Wezel *wezel, int);
        void wyswietlRosnaco(Wezel *wezel);  
};

#endif
