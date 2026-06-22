Number Guessing Game
A fun, interactive command-line interface (CLI) game written in Python where players have a limited number of attempts to guess a randomly generated number.  
PY

Features
Random Generation: Generates a secret number between 1 and 100 for every new game.  
PY

Directional Feedback: Tells the player if their guess is "Too high!" or "Too low!" after each attempt.  
PY

Attempt Tracking: Keeps track of the remaining guesses, allowing a maximum of 10 attempts.  
PY

Input Validation: Safely handles non-integer inputs without interrupting the gameplay loop.  
PY

Prerequisites
Python 3.x installed on your system.

How to Run
Save the code file to your local directory (e.g., GuessingGame.py).

Open your terminal or command prompt and navigate to that directory.

Run the script:

Bash
python GuessingGame.py
Usage Example
Plaintext
--- Number Guessing Game ---
I have generated a random number between 1 and 100.
Can you guess what it is? You have 10 attempts.
Enter your guess: 50
Too low!
Enter your guess: 75
Too high!
Enter your guess: 62
Congratulations! You guessed the correct number in 3 attempts.
