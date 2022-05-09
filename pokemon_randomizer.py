from PokemonAssignerClass import PokemonAssigner

# Get the necessary parameters
game = int(input("Select game (1 for crystal and 2 for emerald): "))
hard_mode = input("Select difficulty ('hard'/'easy'/'full random'): ")
num_pokemon = int(input("How many pokemon do you want in your team? Max 6: "))

# Create the instance of the challenge
pok_rand = PokemonAssigner(game, hard_mode, num_pokemon)

# Filter out the good pokemons of the challenge if hard mode was selected
if pok_rand.difficulty == 'hard' or pok_rand.difficulty == 'easy':
    pok_rand.excludePokemons()

while True:
    print("Showing randomized pokemons: ")
    pok_rand.getRandomTeam()
    
    leave = input("Do you wish to finish? yes/no: ")
    if leave == "yes":
        break
    else:
        print("")