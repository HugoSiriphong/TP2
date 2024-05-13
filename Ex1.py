import json
import csv

def charger_nombres_complexes(chemin_fichier):
    with open(chemin_fichier, 'r') as f:
        donnees = json.load(f)
    return donnees