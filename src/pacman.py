# Pacman, classic arcade game.

from turtle import *
from freegames import floor, vector
from agents.HumanPacman import HumanPacman
from agents.Ghost import Ghost
from WorldRendering import *
from Mazes import *

WRITER = Turtle(visible=False)
VERDANA_BOLD = ("Verdana", 16, "bold")

MAZE = Mazes.level_1
MAX_SCORE = Mazes.level_1_max_score
WORLD = WorldRendering(MAZE)

state = {'score': 0}

def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(position):
    """Return True if the agent position is valid."""
    index = offset(position)
    if MAZE[index] == TILE_WALL:
        return False

    index = offset(position + 19)
    if MAZE[index] == TILE_WALL:
        return False
    
    is_in_column = position.y % TILE_SIZE == 0
    is_in_row = position.x % TILE_SIZE == 0
    return is_in_row or is_in_column

def update_world():
    """Updates the world repeatedly until the game finishes. 
    - Moves pacman and all ghosts.
    - Checks if game is lost/won.
    """
    clear()
    index = offset(pacman.position)
    if MAZE[index] == TILE_DOT:
        MAZE[index] = TILE_EMPTY
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        WORLD.draw_square(x, y)

    WRITER.undo()
    WRITER.write(state['score'], font = VERDANA_BOLD)
    WORLD.render_agent(pacman)

    for ghost in ghosts:
        ghost.step(None)
        WORLD.render_agent(ghost)

    pacman.step(None)
    update()

    if state['score'] == MAX_SCORE:
        end_game("You won!", "yellow")
        return
    
    for ghost in ghosts:
        if abs(pacman.position - ghost.position) < 20:
            end_game("You lost!", "red")
            return

    ontimer(update_world, 100)

def end_game(message, tcolor):
    WRITER.penup()
    WRITER.goto(0, 180)
    WRITER.color(tcolor)
    WRITER.pendown()
    WRITER.write(message, align="center", font = VERDANA_BOLD)


pacman = HumanPacman(vector(-40, -80), valid)
ghosts = [
    Ghost(vector(-180, 160), valid),
    Ghost(vector(-180, -160), valid),
    Ghost(vector(100, 160), valid),
    Ghost(vector(100, -160), valid),
]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
WRITER.goto(160, 160)
WRITER.color('white')
WRITER.write(state['score'], font = VERDANA_BOLD)
listen()
WORLD.world()
update_world()
done()
