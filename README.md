Pac-Man Game

Overview

This is a simple implementation of the classic Pac-Man game built using Python and the Pygame library. The game features a maze where Pac-Man navigates to eat pellets while avoiding ghosts. The objective is to collect all pellets to win the game, with scoring for small pellets (10 points) and power pellets (50 points). The game ends if Pac-Man collides with a ghost.

Features





Classic Pac-Man gameplay with a maze, pellets, and ghosts



Four ghosts with random movement patterns



Score tracking for pellets and power pellets



Win condition when all pellets are collected



Game over condition on collision with ghosts



Arrow key controls for Pac-Man movement

Folder Structure

pygame/
├── env/                    # Virtual environment (ignored by Git)
├── assets/                 # Game images
│   ├── pacman.png
│   ├── yellow.png
│   ├── red.png
│   ├── blue.png
│   ├── green.png
├── main.py                 # Main game code
├── .gitignore              # Git ignore file
├── requirements.txt        # Dependency list
├── README.md               # This file

Requirements

The project uses the following Python library:





Pygame: For game development and rendering graphics

The exact versions are specified in requirements.txt.

Setup Instructions

To run the game on your local machine, follow these steps:





Clone the Repository:

git clone <repository-url>
cd pygame



Set Up a Virtual Environment (optional but recommended):

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate



Install Dependencies:

pip install -r requirements.txt



Run the Game:

python main.py

How to Play





Use the arrow keys (Left, Right, Up, Down) to move Pac-Man through the maze.



Collect small pellets (white dots) for 10 points each.



Collect power pellets (larger white dots) for 50 points each.



Avoid the ghosts (yellow, red, blue, and green). Colliding with a ghost ends the game.



Win the game by collecting all pellets in the maze.



The current score is displayed at the bottom of the screen.