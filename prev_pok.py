# This program randomly selects a given amount of pokemons 
# from the chosen pokemon game list text file.
# This program is used to randomize pokemon crystal and emerald runs

from random import choice, shuffle

# Prompts user to choose between crystal and emerald
while True:
    game = int(input("Which game you want to choose? 1 for crystal, 2 for emerald, and 3 for platinum: "))
    if game == 1:
        filename = '/home/joselws/Documents/python/fun/resources/pokemon_crystal.txt'
        break
    elif game == 2:
        filename = '/home/joselws/Documents/python/fun/resources/pokemon_emerald.txt'
        break
    elif game == 3:
        filename = '/home/joselws/Documents/python/fun/resources/pokemon_platinum.txt'
        break
    else:
        print("Choice not valid! Please try again.")

# Get all the pokemons from the respective file 
with open(filename) as file:
    pokemons  = file.readlines()

# All pokemons from the respective file go in this list
pokemon_list = []
for pokemon in pokemons:
    pokemon_list.append(pokemon.strip())
    pokemon_list.append(pokemon.strip())

# NOTE: The reason why we add each pokemon twice is to balance probabilities,
# Since some pokemons appear both in the starter_pokemons the pokemon_list,
# They are naturally twice as likely to appear, so to balance all pokemons out,
# Pokemons in pokemon_list appear twice

# Now the starter pokemons according to the selected game
# This guarantees that you can get started with your randomized game asap

# For crystal
if game == 1:
    starter_pokemons = ['Meganium', 'Typhlosion', 'Feraligatr', 'Pidgeot', 'Noctowl',
    'Raticate', 'Furret', 'Butterfree', 'Beedrill', 'Ledian', 'Ariados', 'Golem', 'Crobat', 
    'Gengar', 'Victreebel', 'Jumpluff', 'Poliwrath', 'Politoed', 'Arcanine']

# For emerald
if game == 2:
    starter_pokemons = ['Blaziken', 'Swampert', 'Sceptile', 'Mightyena', 'Linoone', 'Beautifly',
    'Dustox', 'Ludicolo', 'Shiftry', 'Swellow', 'Pelipper', 'Gardevoir', 'Breloom', 'Slaking', 
    'Vigoroth', 'Ninjask', 'Shedinja', 'Exploud', 'Azumarill', 'Delcatty', 'Crobat']

# For platinum
if game == 3:
    starter_pokemons = ['Torterra', 'Infernape', 'Empoleon', 'Staraptor', 'Bibarel', 'Kricketune',
    'Luxray', 'Gyarados', 'Crobat', 'Wormadam', 'Mothim', 'Beautifly', 'Dustox']


# Prompts the amount of pokemon to have in the team
num_pokemon = int(input("How many pokemon do you want in your team? Max 6: "))

# Prompts for hard mode, eliminate the good pokemon from the respective games
while True:
    mode = input("Do you want a hard mode? y/n : ")
    if mode == 'y':
        break
    if mode == 'n':
        break
    else:
        print("Not a valid option! Please try again!")

# Hard mode was selected
if mode == 'y':
    # For crystal
    if game == 1:
        excluded_pokemons = ['Meganium', 'Typhlosion', 'Feraligatr', 'Golem', 'Gengar',
        'Steelix', 'Politoed', 'Gyarados', 'Slowbro', 'Slowking', 'Alakazam', 'Forretress',
        'Nidoqueen', 'Nidoking', 'Scizor', 'Heracross', 'Arcanine', 'Granbull', 'Machamp',
        'Tauros', 'Starmie', 'Vaporeon', 'Espeon', 'Umbreon', 'Kingdra', 'Ursaring', 'Donphan',
        'Skarmory', 'Dodrio', 'Rhydon', 'Lapras']
    
    # For emerald
    if game == 2:
        excluded_pokemons = ['Blaziken', 'Swampert', 'Sceptile', 'Ludicolo', 'Gardevoir',
        'Slaking', 'Hariyama', 'Gyarados', 'Aggron', 'Skarmory', 'Flygon', 'Altaria', 'Claydol', 
        'Armaldo', 'Starmie', 'Banette', 'Absol', 'Heracross', 'Rhydon', 'Glalie', 'Walrein']

    # For Platinum
    if game == 3:
        excluded_pokemons = ['Torterra', 'Infernape', 'Empoleon', 'Staraptor', 'Gyarados',
        'Roserade', 'Heracross', 'Blissey', 'Garchomp', 'Lucario', 'Milotic', 'Togekiss']

    # Eliminate the good pokemons from the respective games
    for pokemon in excluded_pokemons:
        while pokemon in pokemon_list:
            pokemon_list.remove(pokemon)
        if pokemon in starter_pokemons:
            starter_pokemons.remove(pokemon)


# A nice shuffle prior selection
shuffle(pokemon_list)
shuffle(starter_pokemons)

# The final chosen pokemons by the program for your run
chosen_pokemons = []

# Begin by selecting the starter pokemon
chosen_pokemons.append(choice(starter_pokemons))

# Selects the remaining pokemons for your run
while len(chosen_pokemons) < num_pokemon:
    selected_pokemon = choice(pokemon_list)
    # Do not include the same pokemon more than once
    if selected_pokemon in chosen_pokemons:
        continue
    else:
        chosen_pokemons.append(selected_pokemon)

print(chosen_pokemons)
