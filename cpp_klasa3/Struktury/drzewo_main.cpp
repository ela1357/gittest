/*
 * drzewo_bin.cpp
 * 
 * Copyright 2018  <>
 * 
 */


#include <iostream>
#include "drzewo.hpp"

using namespace std;

int main(int argc, char **argv)
{
	Drzewo drzewo;
    drzewo.dodajWezel(10);
	drzewo.dodajWezel(8);
	drzewo.dodajWezel(4);
	drzewo.dodajWezel(9);
	drzewo.dodajWezel(20);
	drzewo.dodajWezel(16);
	drzewo.dodajWezel(30);
    
    cout << "Posortowane drzewo (niemalejąco): ";
    drzewo.wyswietlRosnaco();
    
	return 0;
}
