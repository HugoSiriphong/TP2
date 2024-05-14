import json
import csv

def charger_nombres_complexes(chemin_fichier):
    with open(chemin_fichier, 'r') as f:
        donnees = json.load(f)
    return donnees

def ecrire_csv_nombres_complexes(nombres_complexes, chemin_fichier):
    with open(chemin_fichier, 'w', newline='') as f:
        ecrivain = csv.writer(f)
        ecrivain.writerow(['reel', 'imaginaire'])
        for nombre in nombres_complexes:
            ecrivain.writerow([nombre[0], nombre[1]])