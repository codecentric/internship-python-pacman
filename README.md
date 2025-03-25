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

- __Before changing the code, make sure to branch from main.__
- You don't need to do all exercises. If the [easy] exercises are very easy for you, feel free to skip to more difficult onces.
- You may adapt the exercises to your degree of knowledge or add some tasks that you think are exciting.
- Note: The tasks are roughly labelled by difficulty, but tasks of the same category might still take different amounts of time.

### (1) Design a new maze [easy]
Create and design an additional maze for Pac-man and the ghosts

<details>
    <summary>Hints</summary>

- Study the original maze array in [Mazes.py](src/Mazes.py)
- What is the meaning of 0 and 1 in the array?
- Why is the array wrapped in lines of 20 values?
</details>

<details>
    <summary>Required knowledge: Classes</summary>

- What is an instance/object?
- How do I create instances of a class? What is a constructor and how do I use it?
- How do I create different instances of a class with different properties?
</details>


### (2) Random start positions [easy]
Make the start positions of ghosts and pacman random.

<details>
    <summary>Hints</summary>

- Check in the maze which tiles are valid positions.
- The function `random.choice()` from the python package `random` selects a random item from a list.
- The Maze function `point()` converges a tile offset to a 2d pixel point.
</details>

### (3) Change the ghosts [easy]

Change the number of ghosts in the maze and their starting positions.

_Advanced:_ Give the ghosts their original names and colors.

<details>
    <summary>Hints</summary>

- The ghosts are initialised in an array in the [pacman.py](src/pacman.py) file.
- Each ghost in the array is a `Ghost` object. Check out the respective [Ghost](src/agents/Ghost.py) class to find out how the ghost color is set.
- Original ghost names and colors:
  - Blinky: red
  - Pinky: pink
  - Inky: teal
  - Clyde: orange

</details>

<details>
    <summary>Required knowledge: Classes</summary>

- How do I add new attributes to a class?
- How do I create different instances of a class with different properties? (here: different positions, colors and names)
- _optional_: Inheritance (here: `Ghost` inherits its constructor from `BasesAgent`)

</details>


### (4) Add new pellet types [easy/advanced]

Add a pellet that gives 100 points when Pac-man picks it up.

_Advanced_: Add a pellet that lets Pac-man eat ghosts, when he touches them. After a short time, the ghosts should be revived.


<details>
    <summary>Hints</summary>

- Different tile types (e.g. tiles with pellet) are defined in [Mazes.py](src/Mazes.py). With `COMMAND + left click` on the variable name, you can see where and how the pellet tiles are processed in the game logic. 
- After adding the 100 points pellet to the game, is it still possible to win?

</details>

### (5) Enhance the steering of Pac-Man  [advanced]

Make the steering of Pac-Man more convenient.
- Pac-man should always go forward automatically, the user should not have to click for each step he makes.
- If given the input to change direction, Pac-man changes direction accordingly if he reaches a passage within 3 time steps.


<details>
    <summary>Hints</summary>

- One time step is defined as one iteration of `update_world` (see [pacman.py](src/pacman.py)).
- How do the ghosts keep walking smoothly in the same direction? Can we steal the idea?
- How can we implement a timer that counts the time steps in the Pac-man class?

</details>



### (6) Add restart option and highscore [advanced]

- After one game has ended, there should be an option to restart the game.
- Remember previous scores and display a highscore.
- _Advanced_: Save the latest highscore to a file, such that it can be loaded even when the game was closed.
- _Advanced_: Make it possible to progress to a second level after the first level was won (i.e. change the maze).

<details>
    <summary>Hints</summary>

- The whole game takes place in the `update_world` function (see [pacman.py](src/pacman.py)), which is called recursively (loop).
- The loop exits when the game end is detected.

</details>


### (7) Add sound [hard]

- Play a sound when the game is won and another when the game is lost.
- Play a sound at special events, e.g. when a special pellet is collected or a ghost is eaten.

<details>
    <summary>Hints</summary>

- Research how to play sounds in python (on the internet).

</details>
<details>
    <summary>Required knowledge: Threads</summary>

- Playing sound such that the game does freeze requires threads.
- Threads are used to do multiple things in parallel/on the same time.
</details>

### (8) Make the ghosts take better decisions [hard]

- Study the current decision-making of the ghosts. How do they decide which way to go?
- The ghosts should _sense_ their surrounding for Pac-man. If Pac-man is within 3 tiles, they should chase him.
- _Advanced:_ While chasing, the speed (moving distance) of the ghosts is slightly increased.
- _Advanced:_ When losing sight, the speed (moving distance) of the ghosts is slightly decreased.

<details>
    <summary>Hints</summary>

- The code for the ghost agents is within the file [agents/Ghost.py](src/agents/Ghost.py)
- The `step` method in the `Ghost` class is called each time the world is updated.

</details>

### (9) Make Pac-man autonomous [hard/very hard]

- Pac-man should no longer be controlled by humans.
- Implement an autonomous agent that controls Pac-man.
- Pac-man should _sense_ his surrounding and avoid ghosts.
- The agent should collect all pellets and win the game.

<details>
    <summary>Hints</summary>

- Create a new Pac-man agent class.
- Implement the `step(self, game_state)` method inside the new agent class, which decides for a direction based on the `game_state` parameter.
- What could be a simple strategy to move into a direction where pellets are while avoiding ghosts? Can we steal ideas from the ghost behaviour? (We can come far without the use of way planning.)
</details>

<details>
    <summary>Advanced: Way Planning and Search Algorithms</summary>

- As a multi-objective way planning task, Pac-mans strategy can become quite complex. Objectives are:
  - to collect all pellets
  - to avoid ghosts
  - to finish fast (preferrably)
- Shortest path algorithms can help to find a way to the next pellets, when there are no pellets nearby anymore: After the maze array is transformed to a graph, one can apply shortest path algorithms (e.g. A*) to navigate fast to the remaining pellets.
- But: Using a search algorithm for the navigation from the start is not recommended: Finding the shortest path that visits all tiles is already NP-hard (Traveling Salesman Problem). And we also need to take ghosts into account!
</details>