"""
User interface with the Pokemon Randomizer program
"""

from pokemon_assigner_class import PokemonAssigner, Game


def main() -> None:
    """Program that makes use of the pokemon_assigner class"""

    print("Welcome! Randomize your pokemon team here!")

    # Get team size
    while True:
        team_size = int(input("Select your team size: "))
        if PokemonAssigner(team_size):
            break
        print("Invalid team size! Try again.")

    # Initialize class
    team = PokemonAssigner(team_size)

    # Get game
    while True:
        print(
            "Select your game:\
            \n(1) for Crystal\
            \n(2) for RSE(Ruby/Sapphire/Emerald)\
            \n(3) for Platinum"
        )
        game = int(input("Game: "))
        if team.assign_game(game):
            team.get_all_pokemons()
            break

    # Optional: Get game if generation is RSE
    if team.game is Game.RSE:
        while True:
            print(
                "Select your game:\
                \n(1) for Ruby\
                \n(2) for Sapphire\
                \n(3) for Emerald"
            )
            gen_game = int(input("Game: "))
            if team.assign_gen_3_game(gen_game):
                break

    # Get difficulty
    while True:
        print(
            "Select game difficulty:\
            \n(1) for Easy(Bad pokemons filtered out)\
            \n(2) for Normal(No changes)\
            \n(3) for Hard(Good pokemons filtered out)"
        )
        difficulty = int(input("Difficulty: "))
        if team.assign_difficulty(difficulty):
            team.get_all_pokemons()
            break

    # Get random team
    while True:
        team.get_team()
        print(f"Your random team is: {team.assigned_team}")
        print(
            "What do you want to do now?\
            \n(1) Get another random team\
            \n(2) Start from the beginning\
            \n(3) Exit"
        )
        option = int(input("Your option: "))

        if option == 1:
            continue
        if option == 2:
            main()
        if option == 3:
            break
        else:
            print("Invalid option, terminating program.")
            break


if __name__ == "__main__":
    main()
