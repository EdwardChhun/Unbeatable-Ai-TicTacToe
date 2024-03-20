# Unbeatable AI Tic Tac Toe

Welcome to Unbeatable AI Tic Tac Toe! This is a console-based Tic Tac Toe game where you can play against an unbeatable AI opponent. The AI uses the Minimax algorithm to determine its moves, ensuring that it plays optimally and never loses. Keep in mind, this program makes X goes first.

Here is a link regarding the [Minimax Algorithm](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/) by geeksforgeeks.com

## How to Play

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where you cloned or downloaded the repository.
4. Run the `runner.py` file with Python 3 to start the game:
    ```bash
    python runner.py
    ```
5. Follow the prompts to choose whether you want to play as "X" or "O".
6. Make your moves by entering the coordinates of the cell where you want to place your mark.
7. Watch as the AI opponent makes its moves.
8. The game ends when one player wins or the board is full (a tie).

## Features

- **Unbeatable AI**: The AI opponent uses the Minimax algorithm to ensure optimal gameplay. It analyzes all possible future moves to make the best decision at each turn.
- **Interactive Gameplay**: The game provides an interactive console interface where players can make their moves by entering coordinates.
- **Tie Detection**: The game detects ties when the board is full and declares a tie if there's no winner.
- **Player Choice**: Players can choose to play as "X" or "O" at the start of the game.

## Requirements

- Python 3.x
- PyGame

# Install Requirements
- Run this in your console
```
pip3 install -r requirements.txt
```

## Implementation Details

- The game is implemented in Python.
- The AI opponent uses the Minimax algorithm, a recursive algorithm commonly used in two-player games like Tic Tac Toe and chess, to determine its moves.
- The game state is represented by a 3x3 grid, with each cell being either empty, "X", or "O".

## Future Improvements

- Graphical User Interface (GUI): Implement a graphical interface using libraries like Pygame or Tkinter for a more visually appealing gameplay experience.
- Difficulty Levels: Add options for different difficulty levels, allowing players to choose the AI's playing strength.
- Online Multiplayer: Implement online multiplayer functionality to allow players to compete against each other over the internet.
- Faster optimization for computer, implementing Depth-Limited Minimax Algorithm
## Credits

- The Minimax algorithm implementation for the AI opponent is based on concepts from artificial intelligence and game theory.
- Developed by Edward Chhun.
- Inspired by CS50AI, Introduction to AI with Python 2024

## Questions

- If there's any questions or if you need any help, contact Edwardchhun3@gmail.com

## Screenshots

![Main Window](https://github.com/EdwardChhun/Unbeatable-Ai-TicTacToe/blob/main/images/play-ttt.png)
![Play as O](https://github.com/EdwardChhun/Unbeatable-Ai-TicTacToe/blob/main/images/play-O.png)
![Computer Thinking](https://github.com/EdwardChhun/Unbeatable-Ai-TicTacToe/blob/main/images/ttt-computer-thinking.png)
![Tie](https://github.com/EdwardChhun/Unbeatable-Ai-TicTacToe/blob/main/images/ttt-tie.png)
![X Wins](https://github.com/EdwardChhun/Unbeatable-Ai-TicTacToe/blob/main/images/ttt-X-Wins.png)

