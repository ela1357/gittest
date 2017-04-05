/*
 * cw_06.cpp
 *
 * Copyright 2017 user <user@lap79>
 *
 */


#include <iostream>

using namespace std;


int licz_znaki (char tab[]){
    int sz1, sz2, sz3, sz4;
    sz1 = sz2 = sz3= sz4= 0;
    int i = 0;
    while (tab[i] != '\0'){
        switch(tab[i]) {
             case ',':
                    sz1++;
            break;
            case '.':
                    sz2++;
            break;
            case ' ':
                    sz3++;
            break;
            default:
                    sz4++;
}
    i++;
}
    cout << "Przecinki: " << sz1 << endl;
    cout << "kropki: " << sz2 << endl;
    cout << "Spacje: " << sz3 << endl;
    cout << "Litery: " << sz4 << endl;
    cout << "Wszystkie: " << sz1 + sz2 + sz3 + sz4 << endl;
    return sz1 + sz2 + sz3 + sz4;
}




int main(int argc, char **argv) {

    int rozmiar = 100;
    char tab[rozmiar];
    cin.getline(tab, rozmiar);
    cout << tab << endl;
    licz_znaki(tab);

	return 0;
}
