# Task1_Hangman

A simple text-based Hangman game built in Python as **Task 1** of the CodeAlpha Python Programming Internship.

## About the Project
The computer picks a random word and the player guesses it one letter at a time. Each wrong guess brings the player closer to losing. The game runs fully in the console with no graphics or audio.

## Features
- Random word chosen from 5 predefined words
- Maximum of **6 incorrect guesses**
- Shows the word progress (e.g. `p _ t h o n`) after every guess
- Displays guessed letters and remaining attempts
- Input validation (single letters only, no repeated guesses)
- Play-again option after each game

## Concepts Used
`random` module, `while` loops, `if-else`, strings, lists/sets, functions

## Requirements
- Python 3.8 or higher
- No external libraries needed

## How to Run
```bash
python hangman.py
```

## Sample Output
```
=== HANGMAN ===
Guess the word. You can make 6 wrong guesses.

_ _ _ _ _ _
Wrong guesses left: 6
Guessed letters: -
Enter a letter: p
Good guess!

p _ _ _ _ _
...
You won! The word was 'python'.
```

## How It Works
1. A word is picked using `random.choice()`.
2. The player enters a letter each turn.
3. Correct letters are revealed; wrong letters reduce the attempts left.
4. The game ends when the whole word is guessed (win) or 6 wrong guesses are used (loss).

## Project Structure
```
Task1_Hangman/
├── hangman.py
└── README.md
```

## Possible Improvements
- Load words from a file
- Add ASCII hangman drawing
- Add difficulty levels

## Author
Spoorthi M Naik, CodeAlpha Python Programming Intern
