# Pac-man Game in Python

This is a simple implementation of the arcade game Pac-man written in Python. The original source code is from [Free Python Games](https://github.com/grantjenks/free-python-games/blob/master/src/freegames/pacman.py).

## Introduction

In the arcade game Pac-man the player controls the yellow token. The goal is to eat all pellets (small yellow dots) within a maze to win a level. Each pellet eaten by moving Pac-man over it increases the players score by one point. To make things difficult there are also four ghosts (red token) in the maze who try to stop Pac-man. When a ghost reaches Pac-mans position the player loses the game. The ghosts are controlled by the computer. It is only possible to move within the maze, the walls cannot be crossed.

### Controlling Pac-man

The Pac-man token can be controlled by pressing the arrow keys on the keyboard. It is possible to stop the token by not pressing a key. Be aware that the ghosts will still move on.

### Limitations

The simple implementation of the game has some limitations in comparison to the original arcade game:

- There are no power pellets that strengthen Pac-man to eat ghosts to temporarily lock them up at their starting position in the middle of the map.
- There are no fruits.
- There are no portals to jump from one side of the screen to the other.
- Ghosts are stupid and will only change to a randomly selected direction if they run into a wall.
- There is only one level.

## Setup

In order to run the game a local installation of Python is required, which bundles up Tkinter and turtle, which is required to let the application run in a window with graphical output. In addition, the package `freegames` is required, which can be installed using the python package manager from [requirements.txt](requirements.txt):

``` shell
python3 -m pip install -r requirements.txt
```

## Running the Game

The game can be started either from the command line with the following command:

```shell
python3 pacman.py
```

or by starting the file directly from your preferred IDE.

## Exercises

Before changing the code, make sure to branch from main.

### (1) Design a new maze

Create and design an additional maze for Pac-man and the ghosts

<details>
    <summary>Hints</summary>

- Study the original maze array in [pacman.py](src/pacman.py)
- What is the meaning of 0 and 1 in the array?
- Why is the array wrapped in lines of 20 values?

</details>

### (2) Change the ghosts

Change the number of ghosts in the maze and their starting positions.
_Advanced:_ Give the ghosts their original names and colors.

<details>
    <summary>Hints</summary>

- The ghosts are initialised in an array in the `pacman.py`file.
- Each ghost in the array is a `Ghost` object. Check out the respective `Ghost` class to find out more.
- Original ghost names and colors:
  - Blinky: red
  - Pinky: pink
  - Inky: teal
  - Clyde: orange

</details>

### (3) Make the ghosts take better decisions

- Study the current decision-making of the ghosts. How do they decide which way to go?
- The ghosts should _sense_ their surrounding for Pac-man. If Pac-man is within 3 tiles, they should chase him.
- _Advanced:_ While chasing, the speed (moving distance) of the ghosts is slightly increased.
- _Advanced:_ When losing sight, the speed (moving distance) of the ghosts is slightly decreased.

<details>
    <summary>Hints</summary>

- The code for the ghost agents is within the file `agents/Ghost.py`
- The `step` method in the `Ghost` class is called each time the world is updated.

</details>

### (4) Make Pac-man move autonomous

- Pac-man should no longer be controlled by humans.
- Implement an autonomous agent that controls Pac-man.
- Pac-man should _sense_ his surrounding and avoid ghosts.
- The agent must collect all pellets to win the game.

<details>
    <summary>Hints</summary>

- Create a new Pacman agent class
- Implement the `step(self, game_state)` method inside the new agent class, which decides for a direction based on the `game_state` parameter
- Replace the old pac-man instance with an instance of your agent class
</details>