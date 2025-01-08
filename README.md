# battleship-vs-ai

## Overview

The Battleship Game is a console-based, turn-based strategy game where a player competes against an AI to sink each other's ships. The game is played on a 5x5 grid, and the objective is to sink all of the opponent's ships before your own ships are destroyed. Players place their ships strategically on the board, then take turns attacking the opponent's grid by selecting coordinates. The AI uses basic decision-making to target random coordinates and switch to a more targeted approach when it hits a ship.

## Features

- **Turn-Based Gameplay**: Players and AI take turns attacking each other's ships.
- **Ship Placement**: Players place ships manually by entering coordinates and orientation (horizontal or vertical).
- **AI Opponent**: The AI starts by attacking randomly, then targets adjacent cells when a hit is made to improve its chances of sinking larger ships.
- **Game End Condition**: The game ends when one player sinks all of the opponent's ships.
- **Grid Display**: The game uses a 5x5 grid, with ships marked by `S`, hits marked by `X`, and misses marked by `O`.

## Game Mechanics

### 1. **Board Size**
- The game is played on a 5x5 grid.

### 2. **Ship Symbols**
- **Player's Ships**: Represented by the symbol `S`.
- **Hits**: Indicated by `X`.
- **Misses**: Indicated by `O`.
- **Empty Cells**: Represented by `~`.

### 3. **Ship Configuration**
- Different ship sizes are represented as a tuple `(size, quantity)`. For example, `(3, 2)` would represent two ships of size 3.
- Players can place ships manually on the board, specifying their coordinates and orientation (horizontal or vertical).
- **AI Ship Placement**: The AI randomly places ships on the board, ensuring that they fit within the grid without overlapping existing ships.

### 4. **Game Rules**
- **Player's Turn**: The player attacks by entering coordinates (e.g., `A1`, `C3`) to hit the AI’s ships.
- **AI's Turn**: The AI initially attacks randomly. After a hit, the AI switches to "targeting mode" to try adjacent cells to increase the likelihood of hitting consecutive cells for larger ships.
- **Game End**: The game ends when either the player or the AI sinks all the opponent's ships.

## AI Logic

- The AI starts by selecting random grid coordinates for its attacks.
- Once the AI hits a ship, it switches to "target mode", where it targets adjacent cells (up, down, left, or right) to try and sink a ship by hitting consecutive parts of it.
- The AI continues targeting adjacent cells until it misses or sinks the entire ship.

## Project Structure
## Setup and Requirements

### Prerequisites
- Python 3.x

### How to Play

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the `Battleship` directory.
3. Run the game by executing the following command:

```bash
python main.py
