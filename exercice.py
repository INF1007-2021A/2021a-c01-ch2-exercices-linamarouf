#!/usr/bin/env python
# -*- coding: utf-8 -*-
def Majuscule(mot):
    # TODO completer la fonction ici
    nvmot=''
    for lettre in mot:
        nvmot+= chr(ord(lettre)-32)
    return nvmot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = Majuscule(mots[i])

    print(mots)
