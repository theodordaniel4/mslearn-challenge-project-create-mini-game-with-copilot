import unittest
from app import RockPaperScissorsGame

class TestRockPaperScissorsGame(unittest.TestCase):
    def setUp(self):
        self.game = RockPaperScissorsGame()

    def test_initial_score_and_rounds(self):
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.rounds_played, 0)

    def test_computer_choice(self):
        self.assertIn(self.game.get_computer_choice(), ['rock', 'paper', 'scissors'])

    def test_play_round_win(self):
        result = self.game.play_round('rock', 'scissors')
        self.assertEqual(result, 'win')
        self.assertEqual(self.game.score, 1)
        self.assertEqual(self.game.rounds_played, 1)

    def test_play_round_lose(self):
        result = self.game.play_round('rock', 'paper')
        self.assertEqual(result, 'lose')
        self.assertEqual(self.game.score, -1)
        self.assertEqual(self.game.rounds_played, 1)

    def test_play_round_tie(self):
        result = self.game.play_round('rock', 'rock')
        self.assertEqual(result, 'tie')
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.rounds_played, 1)

if __name__ == '__main__':
    unittest.main()