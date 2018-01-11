/*
 * wskazniki.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int x = 11;
    cout << x << endl; // wartość zmiennej
    cout << &x << endl; // adres zmiennej w pamięci, 0x - oznacza wartość szesnastkową
    cout << * &x << endl; // odczytuje wartość w danym adresie (operatowr wskaźnikowy / derereferencji)
    
    int *px; // definicja wskaźnika do typu całkowitego
    px = &x; // inicjiacja wskaźnika
    // wskaźnik zawsze zawiera adres pamięci
    cout << px << endl;
    cout << *px << endl;
    
    int y = 100;
    px = &y;
    cout << px << endl;
    cout << *px << endl;
	
    return 0;
}

