import os
import sys


def set_points(score_board: dict, team_a_name: str, team_b_name: str, team_a_exists: bool,
               team_b_exists: bool, score_a: int, score_b: int) -> dict:
    """
        Updates the points for each teams
    """

    if team_a_exists:
        score_board[team_a_name] += score_a
    elif not team_a_exists:
        score_board[team_a_name] = score_a

    if team_b_exists:
        score_board[team_b_name] += score_b
    elif not team_b_exists:
        score_board[team_b_name] = score_b

    return score_board


def get_score_board(filename) -> dict:
    """
        Takes in a file with scores and teams and tally's up all the scores.
        A win is 3 points and a draw is 1 point.
    """

    if not os.path.exists(filename):
        raise FileNotFoundError

    score_board = {}

    f = open(filename, 'r')
    for x in f:
        game = x.strip().split(',')
        if len(game) != 2:
            continue

        try:
            team_a_name, team_a_score = game[0][0:len(game[0]) - 2].strip(), int(game[0][-1])
            team_b_name, team_b_score = game[1][0:len(game[1]) - 2].strip(), int(game[1][-1])
        except ValueError:
            f.close()
            raise ValueError

        team_a_exists, team_b_exists = False, False

        if score_board.get(team_a_name) is not None:
            team_a_exists = True
        if score_board.get(team_b_name) is not None:
            team_b_exists = True

        if team_a_score == team_b_score:
            score_board = set_points(score_board, team_a_name, team_b_name, team_a_exists, team_b_exists, 1, 1)
        elif team_a_score > team_b_score:
            score_board = set_points(score_board, team_a_name, team_b_name, team_a_exists, team_b_exists, 3, 0)
        elif team_a_score < team_b_score:
            score_board = set_points(score_board, team_a_name, team_b_name, team_a_exists, team_b_exists, 0, 3)
    f.close()

    return score_board


def print_scoreboard(score_board: dict) -> str:
    """
        Formats a dictionary with scores for teams into a ranked scored board string.
        The scores are ranked highest to lowest with a secondary ordering by team
        name where the scores are the same.
    """

    inverted_score_board = {}
    for team, score in score_board.items():
        if inverted_score_board.get(score) is not None:
            inverted_score_board[score].append(team)
        else:
            inverted_score_board[score] = [team]

    sorted_scores = sorted(inverted_score_board, reverse=True)

    scores_str = ''
    rank = 1
    for score in sorted_scores:
        teams = inverted_score_board[score]

        if len(teams) == 1:
            if score == 1:
                scores_str += '%s. %s, %s pt \n' % (rank, teams[0], score)
            else:
                scores_str += '%s. %s, %s pts \n' % (rank, teams[0], score)
        else:
            teams.sort()
            for team in teams:
                if score == 1:
                    scores_str += '%s. %s, %s pt \n' % (rank, team, score)
                else:
                    scores_str += '%s. %s, %s pts \n' % (rank, team, score)

        rank += 1

    return scores_str.strip()


def run(filename):
    try:
        score_board = get_score_board(filename)
        scores_str = print_scoreboard(score_board)
        print(scores_str)
    except ValueError:
        print('invalid score found')
    except FileNotFoundError:
        print('file \'%s\' doesn\'t exist' % sys.argv[1])


if __name__ == '__main__':

    try:
        run(sys.argv[1])
    except IndexError:
        print('not enough arguments to run program, please specify filename')
