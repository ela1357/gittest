/*
 * hello.cpp
 * 
 * Copyright 2017  <>
 * 
 */


#include <iostream>

using namespace std;

#define ROK_TERAZ 2017
#define ROK_CPP 1983

int parzyste(int n){
    int i;
    for (i = 0; i <= n; i += 2)
        cout << i << " ";
    return i/2;
}

int main(int argc, char **argv)
{
    // ~const int cpp = 1983
    int wiek, rok_urodzenia, n;
    string tekst;
    cout << "Jak masz na imię?" << endl;
    cin >> tekst;
    cout << "Hello " << tekst << "!" << endl;
    cout << "Ile masz lat?" << endl;
    cin >> wiek;
    rok_urodzenia = ROK_TERAZ - wiek;
    cout << "Urodziłeś się w " << rok_urodzenia << endl;
    
    if (rok_urodzenia > ROK_CPP){
        cout << "Jestem starszy!" << endl;
    }
    else if (rok_urodzenia < ROK_CPP){
        cout << "Jestem młodszy!" << endl;
    }
    else if (rok_urodzenia == ROK_CPP){
        cout << "Jesteśmy w tym samym wieku!" << endl;
    }
    
    cout << "Podaj liczbę: " << endl;
    cin >> n;
    cout << "Parzystych: " << parzyste(n) << endl;
    
	return 0;
}

