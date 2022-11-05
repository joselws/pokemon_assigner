"""
Class used to get a random pokemon team
games: crystal, rse, platinum
difficulties: easy, normal, hard
"""

from random import choice
from enum import Enum
from typing import List


class Game(Enum):
    """Enum for each Pokemon Game"""

    CRYSTAL = 1
    RSE = 2
    PLATINUM = 3


class Gen3Game(Enum):
    """Enum for each Pokemon Generation 3 game"""

    RUBY = 1
    SAPPHIRE = 2
    EMERALD = 3


class Difficulty(Enum):
    """Enum for each difficulty type"""

    EASY = 1
    NORMAL = 2
    HARD = 3


class PokemonAssigner:
    """Random pokemon assigner object class for this program"""

    def __init__(self, team_size: int) -> None:
        self.all_game_pokemons: List[str] = []
        self.assigned_team: List[str] = []
        self.pokemons_to_exclude: List[str] = []
        self.team_size: int = team_size
        self.difficulty: Difficulty
        self.game: Game
        self.gen_game: Gen3Game

    @staticmethod
    def valid_team_size(team_size: int) -> bool:
        """Returns True if the number is between 1 and 6"""

        try:
            if 1 <= team_size <= 6:
                return True
            return False
        except TypeError as error:
            print(f"Error {error}")
            return False

    def assign_difficulty(self, difficulty: int) -> bool:
        """Returns True on successful operation"""

        try:
            self.difficulty = Difficulty(difficulty)
        except ValueError as error:
            print(f"Error {error}. Number must be 1, 2, or 3")
            return False

        self.pokemons_to_exclude.clear()

        if self.difficulty is Difficulty.EASY and self.game is Game.CRYSTAL:
            self.pokemons_to_exclude = [
                "Noctowl",
                "Raticate",
                "Furret",
                "Butterfree",
                "Beedrill",
                "Ledian",
                "Ariados",
                "Togetic",
                "Unown",
                "Jumpluff",
                "Venomoth",
                "Azumarill",
                "Shuckle",
            ]

        if self.difficulty is Difficulty.EASY and self.game is Game.RSE:
            self.pokemons_to_exclude = [
                "Mightyena",
                "Linoone",
                "Beautifly",
                "Dustox",
                "Pelipper",
                "Volbeat",
                "Illumise",
                "Castform",
                "Clamperl",
                "Luvdisc",
                "Masquerain",
            ]

        if self.difficulty is Difficulty.EASY and self.game is Game.PLATINUM:
            self.pokemons_to_exclude = [
                "Bibarel",
                "Kricketune",
                "Wormadam",
                "Mothim",
                "Beautifly",
                "Dustox",
                "Pachirisu",
                "Seaking",
                "Chimecho",
                "Sudowoodo",
                "Chatot",
                "Noctowl",
                "Pelipper",
            ]

        if self.difficulty is Difficulty.HARD and self.game is Game.CRYSTAL:
            self.pokemons_to_exclude = [
                "Meganium",
                "Typhlosion",
                "Feraligatr",
                "Gengar",
                "Politoed",
                "Slowbro",
                "Slowking",
                "Alakazam",
                "Scizor",
                "Heracross",
                "Machamp",
                "Tauros",
                "Starmie",
                "Vaporeon",
                "Espeon",
                "Kingdra",
                "Ursaring",
                "Donphan",
                "Dodrio",
                "Lapras",
            ]

        if self.difficulty is Difficulty.HARD and self.game is Game.RSE:
            self.pokemons_to_exclude = [
                "Swampert",
                "Blaziken",
                "Ludicolo",
                "Gardevoir",
                "Gyarados",
                "Skarmory",
                "Flygon",
                "Altaria",
                "Claydol",
                "Starmie",
                "Heracross",
                "Glalie",
                "Walrein",
            ]

        if self.difficulty is Difficulty.HARD and self.game is Game.PLATINUM:
            self.pokemons_to_exclude = [
                "Staraptor",
                "Gyarados",
                "Roserade",
                "Gastrodon",
                "Heracross",
                "Blissey",
                "Garchomp",
                "Lucario",
                "Milotic",
                "Abomasnow",
                "Weavile",
                "Gardevoir",
                "Gallade",
                "Vaporeon",
                "Espeon",
                "Glaceon",
                "Togekiss",
                "Magnezone",
                "Rhyperior",
                "Dusknoir",
                "Electrivire",
                "Mamoswine",
                "Absol",
                "Empoleon",
                "Torterra",
                "Infernape",
            ]

        self.exclude_pokemons()
        return True

    def assign_game(self, game: int) -> bool:
        """Returns True on successful operation"""
        try:
            self.game = Game(game)
            return True
        except ValueError as error:
            print(f"Error {error}. Number must be 1, 2, or 3")
            return False

    def assign_gen_3_game(self, game: int) -> bool:
        """Returns True on successful operation"""
        try:
            self.gen_game = Gen3Game(game)
            self.pokemons_to_exclude.clear()

            if self.gen_game is Gen3Game.RUBY:
                self.pokemons_to_exclude = [
                    "Ludicolo",
                    "Sableye",
                    "Seviper",
                    "Lunatone",
                ]
            elif self.gen_game is Gen3Game.SAPPHIRE:
                self.pokemons_to_exclude = [
                    "Shiftry", "Mawile", "Zangoose", "Solrock"
                ]
            elif self.gen_game is Gen3Game.EMERALD:
                self.pokemons_to_exclude = [
                    "Masquerain",
                    "Medicham",
                    "Roselia",
                    "Zangoose",
                    "Lunatone",
                ]

            self.exclude_pokemons()
            return True
        except ValueError as error:
            print(f"Error {error}. Number must be 1, 2, or 3")
            return False

    def get_all_pokemons(self) -> bool:
        """Get a list of all Pokemon for the given game"""

        # Redo the list on every call
        self.all_game_pokemons.clear()

        if self.game is Game.CRYSTAL:
            filename = "./resources/pokemon_crystal.txt"
        elif self.game is Game.RSE:
            filename = "./resources/pokemon_emerald.txt"
        elif self.game is Game.PLATINUM:
            filename = "./resources/pokemon_platinum.txt"

        # Get all pokemon from this file
        with open(filename, mode="rt", encoding="ascii") as file:
            pokemons = file.readlines()

        # Add them to the pokemon list attribute
        for pokemon in pokemons:
            self.all_game_pokemons.append(pokemon.strip())

        return True

    def exclude_pokemons(self) -> None:
        """
        Exclude pokemons located in pokemons_to_exclude
        from all_game_pokemons
        """

        for pokemon in self.pokemons_to_exclude:
            if pokemon in self.all_game_pokemons:
                self.all_game_pokemons.remove(pokemon)

    def get_team(self) -> None:
        """Get random pokemon team"""

        self.assigned_team.clear()

        while len(self.assigned_team) < self.team_size:
            pokemon = choice(self.all_game_pokemons)
            if pokemon not in self.assigned_team:
                self.assigned_team.append(pokemon)
