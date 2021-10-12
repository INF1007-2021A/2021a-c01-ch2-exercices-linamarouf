#!/usr/bin/env python
# -*- coding: utf-8 -*-
def Majuscule(mot):
    # TODO completer la fonction ici
    return (mot.upper())


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
