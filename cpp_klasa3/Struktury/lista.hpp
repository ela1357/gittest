#ifndef LISTA_HPP
#define LISTA_HPP

struct ELEMENT{ // rekurencyjny sposób deklarowania listy
    int wartosc;
    ELEMENT *nast; // wskaźnik do nastepnego elementu listy
};

class Lista {
    private: // hermetyzacja danych
        ELEMENT *head;
        ELEMENT *tail;
    public: // interfejs publiczny (API klasy)
        Lista(); // konstruktor
        ~Lista (); // destruktor, sprząta po klasie // memory leaks - wycieki pamięci
        void Dodaj(int);
        void Wyswietl();
        bool Usun();        
};

#endif
