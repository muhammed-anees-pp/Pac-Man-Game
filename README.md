# 🟡 Pac-Man Game

## 🎮 Overview

This is a simple implementation of the classic **Pac-Man** game built using **Python** and the **Pygame** library.  
Pac-Man navigates a maze to eat pellets while avoiding ghosts. The goal is to collect all pellets to win, with different scores for small and power pellets. The game ends if Pac-Man collides with a ghost.

---

## ✨ Features

- Classic Pac-Man gameplay with maze, pellets, and ghosts
- Four ghosts with random movement patterns
- Score tracking for small pellets (10 points) and power pellets (50 points)
- Win condition when all pellets are collected
- Game over condition on ghost collision
- Arrow key controls for Pac-Man movement

---


## 📦 Requirements

- Python 3.x
- Pygame (version specified in `requirements.txt`)

---

## ⚙️ Setup Instructions

Follow these steps to run the game locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/muhammed-anees-pp/Pac-Man-Game.git
   cd pygame
   ```

2. **Set Up a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv env
   source env/bin/activate        # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Game**
   ```bash
   python main.py
   ```

---

## 🕹️ How to Play

- Use **arrow keys** (← ↑ ↓ →) to move Pac-Man.
- **Collect small pellets** (white dots) for **10 points**.
- **Collect power pellets** (larger white dots) for **50 points**.
- **Avoid ghosts** (yellow, red, blue, and green).
- **Game ends** if you collide with a ghost.
- **Win** by collecting **all pellets** in the maze.
- Your **score** is shown at the bottom of the screen.
