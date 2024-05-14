import csv

def lire_pokemon_csv(pokemon):

    pokemon_stats = {}

    with open(pokemon, newline='') as csvfile:
        lire = csv.reader(csvfile)
        for i in lire:  # i = rangée
            nom_pokemon = i[0]
            stats_str = i[1:]
            stats_int = [int(stat) for stat in stats_str]
            stats_format ="".join([f"({stat_label} {stat_value})" for stat_label, stat_value in zip(["HP", "ATTAQUE", "DEFENSE", "SP ATTAQUE", "SP DEFENSE", "VITESSE"], stats_int)])
            # FORMATAGE DU DICTIONNAIRE
            pokemon_stats[nom_pokemon] = stats_format

    return pokemon_stats

fichier_csv = "pokemon.csv"
donnees_pokemon = lire_pokemon_csv(fichier_csv)
print(donnees_pokemon)
