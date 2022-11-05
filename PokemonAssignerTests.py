import unittest
from pokemon_assigner_class import PokemonAssigner, Game, Gen3Game, Difficulty


class TestPokemonAssigner(unittest.TestCase):
    """
    Tests for the PokemonAssigner class
    """

    # TESTS: creation

    def test_class_correctly_created(self) -> None:
        """class all initial empty attributes"""
        team = PokemonAssigner(3)
        self.assertFalse(team.all_game_pokemons)
        self.assertFalse(team.assigned_team)
        self.assertFalse(team.pokemons_to_exclude)
        self.assertEqual(team.team_size, 3)

    
    # TESTS: valid_team_size static method

    def test_valid_team_size(self) -> None:
        """Returns true if number is between 1 and 6 inclusive"""
        self.assertTrue(PokemonAssigner.valid_team_size(1))
        self.assertTrue(PokemonAssigner.valid_team_size(4))
        self.assertTrue(PokemonAssigner.valid_team_size(6))

    def test_invalid_team_size(self) -> None:
        """Returns false if number not in 1-6 range"""
        self.assertFalse(PokemonAssigner.valid_team_size(0))
        self.assertFalse(PokemonAssigner.valid_team_size(7))

    def test_invalid_team_size_exception(self) -> None:
        """Returns false if an error is encountered"""
        self.assertFalse(PokemonAssigner.valid_team_size("test"))

    
    # TESTS: assign_game method

    def test_assign_game_crystal(self) -> None:
        """Assigning game of crystal works"""
        team = PokemonAssigner(4)

        self.assertTrue(team.assign_game(1))
        self.assertIs(team.game, Game.CRYSTAL)

    def test_assign_game_rse(self) -> None:
        """Assigning game of rse works"""
        team = PokemonAssigner(4)

        self.assertTrue(team.assign_game(2))
        self.assertIs(team.game, Game.RSE)

    def test_assign_game_platinum(self) -> None:
        """Assigning game of platinum works"""
        team = PokemonAssigner(4)

        self.assertTrue(team.assign_game(3))
        self.assertIs(team.game, Game.PLATINUM)

    def test_assign_invalid_game(self) -> None:
        """Returns False on error"""
        team1 = PokemonAssigner(4)
        team2 = PokemonAssigner(4)

        self.assertFalse(team1.assign_game(0))
        self.assertFalse(team2.assign_game(4))



if __name__ == "__main__":
    unittest.main()