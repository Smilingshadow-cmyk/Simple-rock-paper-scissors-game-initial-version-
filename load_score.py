from save_score import save_score
from score_file import SCORE_FILE


def load_score():
    score = {
        "wins": 0,
        "losses": 0,
        "ties": 0,
    }

    try:
        with open(SCORE_FILE, "r") as file:
            for line in file:
                name, value = line.strip().split("=")
                score[name] = int(value)
    except FileNotFoundError:
        save_score(score)

    return score
