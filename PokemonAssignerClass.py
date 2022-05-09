# This class will select you a random pokemon team according to specified:
# Game, difficulty, and number of pokemons

from random import choice

class PokemonAssigner():
    """Random pokemon assigner object class for this program"""
    
    def __init__(self, game, difficulty, pokemon_amount):
        """Initialize the game, difficulty, and pokemon amount instance"""
        self.game = game
        self.difficulty = difficulty
        self.pokemon_amount = pokemon_amount
        self.starters = self.getStarterPokemons()
        self.available_pokemons = self.getAllPokemons()
        self.random_team = []


    def getAllPokemons(self):
        """Get a list of all Pokemon for the given game"""
        # Redo the list on every call
        if 'available_pokemons' in vars(self):
            self.available_pokemons.clear()

        if self.game == 1:
            filename = '/home/joselws/Documents/python/fun/resources/pokemon_crystal.txt'
        elif self.game == 2:
            filename = '/home/joselws/Documents/python/fun/resources/pokemon_emerald.txt'

        # Get all pokemon from this file
        with open(filename) as file:
            pokemons = file.readlines()

        all_pokemons = []
        # Add them to the pokemon list attribute
        for pokemon in pokemons:
            all_pokemons.append(pokemon.strip())

        return all_pokemons
        

    def getStarterPokemons(self):
        """Get the starter pokemons available for the given game and difficulty"""
        # Redo the list on every call
        if 'starters' in vars(self):
            self.starters.clear()

        # For Crystal
        if self.game == 1:
            starter_pokemons = ['Meganium', 'Typhlosion', 'Feraligatr', 'Pidgeot', 'Noctowl',
                    'Raticate', 'Furret', 'Butterfree', 'Beedrill', 'Ledian', 'Ariados', 'Golem', 'Crobat', 
                    'Gengar', 'Victreebel', 'Jumpluff', 'Poliwrath', 'Politoed', 'Arcanine']

        # For emerald
        if self.game == 2:
            starter_pokemons = ['Blaziken', 'Swampert', 'Sceptile', 'Mightyena', 'Linoone', 'Beautifly',
                    'Dustox', 'Ludicolo', 'Shiftry', 'Swellow', 'Pelipper', 'Gardevoir', 'Breloom', 'Slaking', 
                    'Vigoroth', 'Ninjask', 'Shedinja', 'Exploud', 'Azumarill', 'Delcatty', 'Crobat']

        return starter_pokemons


    def excludePokemons(self):
        """
        Filter Pokemons out of the list  off all pokemons and starters
        according to the difficulty and game
        """

        # Filter out the good pokemons
        if self.difficulty == 'hard':
            # For crystal
            if self.game == 1:
                excluded_pokemons = ['Meganium', 'Typhlosion', 'Feraligatr', 'Gengar',
                        'Politoed', 'Slowbro', 'Slowking', 'Alakazam', 
                        'Scizor', 'Heracross', 'Machamp',
                        'Tauros', 'Starmie', 'Vaporeon', 'Espeon','Kingdra', 'Ursaring', 'Donphan',
                        'Dodrio', 'Lapras']
            
            # For emerald
            if self.game == 2:
                excluded_pokemons = ['Sceptile', 'Swampert', 'Blaziken', 'Ludicolo', 'Gardevoir',
                        'Gyarados', 'Skarmory', 'Flygon', 'Altaria', 'Claydol', 
                        'Starmie', 'Heracross', 'Glalie', 'Walrein']

        # Filter out the bad pokemon
        elif self.difficulty == 'easy':
            # For Crystal
            if self.game == 1:
                excluded_pokemons = ['Noctowl', 'Raticate', 'Furret', 'Butterfree', 'Beedrill'
                        'Ledian', 'Ariados', 'Togetic', 'Unown', 'Jumpluff', 'Venomoth',
                        'Azumarill', 'Shuckle']

            # For emerald
            if self.game == 2:
                excluded_pokemons = ['Mightyena', 'Linoone', 'Beautifly', 'Dustox', 'Pelipper',
                        'Volbeat', 'Illumise', 'Castform', 'Clamperl', 'Luvdisc']

        # Exclude these pokemons from the Pokemon list
        for pokemon in excluded_pokemons:
            if pokemon in self.available_pokemons:
                self.available_pokemons.remove(pokemon)

            if pokemon in self.starters:
                self.starters.remove(pokemon)

    
    def getRandomTeam(self):
        """
        Get the specified number of pokemons from the pokemon_list
        and the starters
        """
        # Clear out the random team first
        self.random_team.clear()

        # Get the starter Pokemon
        self.random_team.append(choice(self.starters))

        # Get the rest of the pokemons
        while len(self.random_team) < self.pokemon_amount:
            pokemon = choice(self.available_pokemons)
            if pokemon not in self.random_team:
                self.random_team.append(pokemon)
        
        print(self.random_team)


    def showSelectedPokemon(self):
        """Prints the random_team attribute"""
        print(self.random_team)