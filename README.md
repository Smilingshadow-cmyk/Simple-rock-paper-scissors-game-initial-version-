# Rock Paper Scissors

A simple command-line Rock Paper Scissors game written in Python. The game lets a player compete against the computer, tracks wins, losses, and ties, and saves the score between sessions.

## Features

- Play Rock Paper Scissors from the terminal
- Random computer choice for every round
- Automatic winner detection
- Persistent score tracking using `scores.txt`
- Menu option to view old scores
- Modular Python files for easier reading and maintenance

## Project Structure

```text
rock_paper_scissors/
|-- main.py
|-- get_computer_choice.py
|-- get_winner.py
|-- load_score.py
|-- print_score.py
|-- save_score.py
|-- score_file.py
|-- scores.txt
`-- README.md
```

## File Overview

- `main.py` starts the game and displays the main menu.
- `get_computer_choice.py` randomly selects rock, paper, or scissors for the computer.
- `get_winner.py` compares the player choice and computer choice.
- `load_score.py` loads saved scores from `scores.txt`.
- `save_score.py` saves the latest score after each round.
- `print_score.py` displays the current score.
- `score_file.py` stores the path to the score file.
- `scores.txt` keeps the saved wins, losses, and ties.

## Requirements

- Python 3.x

No external packages are required.

## How to Run

Open a terminal in the `rock_paper_scissors` folder and run:

```bash
python main.py
```

If your system uses the Python launcher, run:

```bash
py main.py
```

## How to Play

1. Choose `1` from the menu to start a new game.
2. Type one of the following choices:
   - `rock`
   - `paper`
   - `scissors`
3. Type `4` during a game to stop and return to the menu.
4. Choose `2` from the menu to view the saved score.
5. Choose `3` to exit the program.

## Score Format

Scores are stored in `scores.txt` using this format:

```text
wins=0
losses=0
ties=0
```

The program reads and updates this file automatically.

## Example

```text
===== Rock Paper Scissors =====
1. New Game
2. Old Score
3. Exit
Choose an option: 1

New Game Started!
Type rock, paper, or scissors.
Type 4 to stop this game and go back to the menu.

Your choice: rock
Computer chose: scissors
You win this round!
```

## Notes

- Keep `scores.txt` in the same folder as the Python files.
- If `scores.txt` is missing, the program will create a new score file automatically.
- Use lowercase inputs for choices: `rock`, `paper`, or `scissors`.
