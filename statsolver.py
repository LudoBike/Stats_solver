#!/usr/bin/python3.4
# -*-coding:UTF-8-*

# Programme qui a partir d'une serie statistique donnée en trouve les attributs


# Import
from statserie import StatSerie
from fonctions import *


# Main
print("Stat solver de Ludovic DRUETTE")
print("version 0.1", end="\n\n")


try:
    serie = StatSerie(valeurs)
    print(serie)
except ValueError:
    exit()
