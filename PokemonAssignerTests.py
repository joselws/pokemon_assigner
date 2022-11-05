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

    
    # TEST: get_all_pokemons

    def test_get_all_pokemons_crystal(self) -> None:
        """get_all_pokemons works correctly for crystal"""

        team = PokemonAssigner(4)
        team.assign_game(1)

        self.assertTrue(team.get_all_pokemons())
        self.assertNotEqual(team.all_game_pokemons, [])
        self.assertIn("Forretress", team.all_game_pokemons)
        self.assertIn("Sunflora", team.all_game_pokemons)
        self.assertIn("Unown", team.all_game_pokemons)

    def test_get_all_pokemons_rse(self) -> None:
        """get_all_pokemons works correctly for rse"""

        team = PokemonAssigner(4)
        team.assign_game(2)

        self.assertTrue(team.get_all_pokemons())
        self.assertNotEqual(team.all_game_pokemons, [])
        self.assertIn("Swellow", team.all_game_pokemons)
        self.assertIn("Exploud", team.all_game_pokemons)
        self.assertIn("Aggron", team.all_game_pokemons)

    def test_get_all_pokemons_platinum(self) -> None:
        """get_all_pokemons works correctly for platinum"""

        team = PokemonAssigner(4)
        team.assign_game(3)

        self.assertTrue(team.get_all_pokemons())
        self.assertNotEqual(team.all_game_pokemons, [])
        self.assertIn("Pachirisu", team.all_game_pokemons)
        self.assertIn("Wormadam", team.all_game_pokemons)
        self.assertIn("Staraptor", team.all_game_pokemons)


    # TEST: exclude_pokemons

    def test_assert_exclude_pokemons(self) -> None:
        """exclude_pokemons method works correctly"""

        team = PokemonAssigner(4)
        team.assign_game(1)
        team.get_all_pokemons()

        self.assertListEqual(team.pokemons_to_exclude, [])
        self.assertIn("Mantine", team.all_game_pokemons)

        team.pokemons_to_exclude.append("Mantine")
        self.assertListEqual(team.pokemons_to_exclude, ["Mantine"])

        team.exclude_pokemons()
        self.assertNotIn("Mantine", team.all_game_pokemons)

    def test_assert_exclude_pokemons_empty(self) -> None:
        """exclude_pokemons does nothing if it's empty"""

        team = PokemonAssigner(4)
        team.assign_game(1)
        team.get_all_pokemons()

        all_pokemon_list = team.all_game_pokemons
        self.assertListEqual(team.pokemons_to_exclude, [])
        team.exclude_pokemons()
        self.assertListEqual(all_pokemon_list, team.all_game_pokemons)


    # TEST: assign_gen_3_game

    def test_assign_gen_3_game_invalid_game(self) -> None:
        """assign_gen_3_game returns false if game is not rse"""

        team = PokemonAssigner(4)
        team.assign_game(1)
        self.assertFalse(team.assign_gen_3_game(2))
        self.assertListEqual(team.pokemons_to_exclude, [])
    
    def test_assign_gen_3_game_ruby(self) -> None:
        """assign_gen_3_game works correctly on ruby"""

        team = PokemonAssigner(4)
        team.assign_game(2)
        all_initial_pokemon = set(team.all_game_pokemons)
        missing_pokemon = [
            "Ludicolo", "Sableye", "Seviper", "Lunatone",
        ]

        self.assertTrue(team.assign_gen_3_game(1))
        self.assertEqual(team.pokemons_to_exclude, missing_pokemon)
        self.assertTrue(set(team.all_game_pokemons).isdisjoint(set(missing_pokemon)))
        self.assertTrue(set(team.all_game_pokemons).issubset(all_initial_pokemon))

    def test_assign_gen_3_game_sapphire(self) -> None:
        """assign_gen_3_game works correctly on sapphire"""

        team = PokemonAssigner(4)
        team.assign_game(2)
        all_initial_pokemon = set(team.all_game_pokemons)
        missing_pokemon = [
            "Shiftry", "Mawile", "Zangoose", "Solrock"
        ]

        self.assertTrue(team.assign_gen_3_game(2))
        self.assertEqual(team.pokemons_to_exclude, missing_pokemon)
        self.assertTrue(set(team.all_game_pokemons).isdisjoint(set(missing_pokemon)))
        self.assertTrue(set(team.all_game_pokemons).issubset(all_initial_pokemon))

    def test_assign_gen_3_game_emerald(self) -> None:
        """assign_gen_3_game works correctly on emerald"""

        team = PokemonAssigner(4)
        team.assign_game(2)
        all_initial_pokemon = set(team.all_game_pokemons)
        missing_pokemon = [
            "Masquerain",
            "Medicham",
            "Roselia",
            "Zangoose",
            "Lunatone",
        ]

        self.assertTrue(team.assign_gen_3_game(3))
        self.assertEqual(team.pokemons_to_exclude, missing_pokemon)
        self.assertTrue(set(team.all_game_pokemons).isdisjoint(set(missing_pokemon)))
        self.assertTrue(set(team.all_game_pokemons).issubset(all_initial_pokemon))

    def test_assign_gen_3_game_invalid_gen_game(self) -> None:
        """assign_gen_3_game returns false if gen game is not valid"""

        team = PokemonAssigner(4)
        team.assign_game(2)
        all_initial_pokemon = team.all_game_pokemons

        self.assertFalse(team.assign_gen_3_game(0))
        self.assertListEqual(team.pokemons_to_exclude, [])
        self.assertListEqual(all_initial_pokemon, team.all_game_pokemons)


    # TEST: assign_difficulty

    def test_assign_difficulty_invalid(self) -> None:
        """returns false given an invalid difficulty choice"""
        
        team = PokemonAssigner(4)
        team.assign_game(1)
        self.assertFalse(team.assign_difficulty(0))
        self.assertFalse(team.assign_difficulty(4))

    def test_assign_difficulty_crystal_easy(self) -> None:
        """bad crystal pokemon are filtered from available pokemons"""

        team = PokemonAssigner(4)
        team.assign_game(1)
        all_pokemons = team.all_game_pokemons
        self.assertTrue(team.assign_difficulty(1))
        self.assertTrue(set(team.all_game_pokemons).isdisjoint(set(team.pokemons_to_exclude)))
        self.assertTrue(set(team.all_game_pokemons).issubset(set(all_pokemons)))

    def test_assign_difficulty_rse_normal(self) -> None:
        """no pokemon are filtered from available pokemons"""

        team = PokemonAssigner(4)
        team.assign_game(2)
        all_pokemons = team.all_game_pokemons
        self.assertTrue(team.assign_difficulty(2))
        self.assertListEqual(team.all_game_pokemons, all_pokemons)
        self.assertListEqual(team.pokemons_to_exclude, [])

    def test_get_team(self) -> None:
        """Get team works correctly"""

        team = PokemonAssigner(4)
        team.assign_game(1)
        team.get_all_pokemons()
        team.assign_difficulty(1)
        team.get_team()

        self.assertTrue(set(team.assigned_team).issubset(set(team.all_game_pokemons)))
        self.assertEqual(len(set(team.assigned_team)), 4)


if __name__ == "__main__":
    unittest.main()