import unittest
from span_assessment import scores


class TestScores(unittest.TestCase):

    def test_set_points_success(self):
        score_board = {}
        team_a = "team a"
        team_b = "team b"
        score_board[team_a] = 2
        team_a_exists, team_b_exists = True, False

        score_board = scores.set_points(score_board, team_a, team_b, team_a_exists, team_b_exists, 1, 1)

        self.assertEqual(3, score_board[team_a], f'Teams A score is shown {score_board[team_a]} rather than 3')
        self.assertEqual(1, score_board[team_b], f'Teams B score is shown {score_board[team_a]} rather than 1')

    def test_print_scoreboard_success(self):
        scores_dict = {'Lions': 3, 'Snakes': 1, 'FC Awesome': 2}
        expected_scores_str = "1. Lions, 3 pts \n2. FC Awesome, 2 pts \n3. Snakes, 1 pt"

        scores_str = scores.print_scoreboard(scores_dict)

        self.assertEqual(expected_scores_str, scores_str)

    def test_print_scoreboard_empty_scores(self):
        scores_dict = {}
        expected_scores_str = ""

        scores_str = scores.print_scoreboard(scores_dict)

        self.assertEqual(expected_scores_str, scores_str)

    def test_get_score_board_success(self):
        expected_score_board = {'Lions': 2, 'Snakes': 1, 'Tarantulas': 3, 'FC Awesome': 1}

        score_board = scores.get_score_board("tests/test_data.txt")

        self.assertEqual(expected_score_board, score_board)

    def test_get_score_board_empty_file(self):
        expected_score_board = {}

        score_board = scores.get_score_board("tests/test_data_empty.txt")

        self.assertEqual(expected_score_board, score_board)

    def test_get_score_board_invalid_filename(self):
        with self.assertRaises(FileNotFoundError):
            scores.get_score_board("tests/test_xyz.txt")

    def test_get_score_board_invalid_score(self):
        with self.assertRaises(ValueError):
            scores.get_score_board("tests/test_data_invalid_score.txt")


if __name__ == '__main__':
    unittest.main()
