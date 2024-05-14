import csv

def lire_pokemon_csv(pokemon):


    pokemon_stats = {}

    with open(pokemon, newline='') as csvfile:
        lire = csv.reader(csvfile)
        for i in lire:  # i signifie rangée
            nom_pokemon = i[0]
            stats_str = i[1:]
            stats_int = [int(stat) for stat in stats_str]
            pokemon_stats[nom_pokemon] = stats_int

    return pokemon_stats




