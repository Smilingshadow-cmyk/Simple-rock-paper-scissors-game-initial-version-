from score_file import SCORE_FILE


def save_score(score):
    with open(SCORE_FILE, "w") as file:
        file.write(f"wins={score['wins']}\n")
        file.write(f"losses={score['losses']}\n")
        file.write(f"ties={score['ties']}\n")
