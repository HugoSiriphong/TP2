# TP2
TP2 Hugo Siriphong - Andisen Apasamy

Exercice 1 :

Écrire un programme qui lit un fichier JSON (data.json) contenant des nombres complexes stockés sous la forme d'une liste de tuples et qui écrit chaque nombre complexe dans un fichier CSV sous la forme suivante :

reel,imaginaire
2,3
3,2
1.0,-5.3

Vous avez ci-dessous un exemple de format du fichier JSON

[[2, 3], [3, 2], [1.0, -5.3]


Exercice 2 :

Vous avez un fichier CSV qui contient, sur chaque ligne, le nom d'un Pokémon suivi de ses stats (attributs). Vous devez écrire une fonction qui lit ce fichier et retourne les valeurs sous la forme d'un dictionnaire où la clé est le nom du Pokémon (string) et la valeur est la liste de ses stats (toutes les colonnes qui suivent le nom). La liste de status doit être une liste d'entiers, pas une liste de string; il faut faire la conversion si nécessaire.
Voici le contenu du fichier pokemon.csv qui est utilisé pour les tests:
Pikachu,35,55,30,50,40,90
Charizard,78,84,78,109,85,100
Magikarp,20,10,55,15,20,80
