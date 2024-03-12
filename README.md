A simple 2D fighting game implemented in Python using the Pygame library.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Controls](#controls)
- [Gameplay](#gameplay)

## Description

Basic fighting game where two players (Warrior and Wizard) engage in combat. The game features simple controls, basic AI for the second player, and a scoring system.

## Features

- Two playable characters: Warrior and Wizard
- Basic AI for the second player
- Simple scoring system
- Game restarts after a player's defeat

## Requirements

- Python 3.X
- Pygame library

## Installation

```
pip install pygame
```


1. Clone the repository:

```
git clone https://github.com/Vulnpire/s-2d-game.git
cd s-2d-game
```

## Controls

-   Player 1 (Wizard):
      Move Left: A
      Move Right: D
      Jump: W
      Attack 1: R
      Attack 2: T

-   Player 2 (Warrior):
      Move Left: Left Arrow
      Move Right: Right Arrow
      Jump: Up Arrow
      Attack 1: Numpad 1
      Attack 2: Numpad 2

## Gameplay
The game starts with a countdown, and players can move and attack when the countdown reaches zero.
Each player has a health bar, and the game restarts after a player is defeated.
