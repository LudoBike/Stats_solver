#!/usr/bin/python3.4
# -*-coding:UTF-8-*

# Programme qui a partir d'une serie statistique donnée en trouve les attributs


# Import
from statserie import StatSerie
from functions import *


# Main
print("Stat solver de Ludovic DRUETTE")
print("version 0.1", end="\n\n")

valeurs = keyboard_input()
try:
    serie = StatSerie(valeurs)
    print(serie)
except ValueError:
    exit()

choice = user_choice("Que voulez-vous faire", \
                     "Sauvegarder cette serie", \
                     "Quitter")

if (choice == 1):
    print("Dans quel fichier souhaitez-vous sauvegarder")
    serie.save(input(">"))
else:
    exit()
