# Pacman, classic arcade game.

from random import choice
from turtle import *
from freegames import floor, vector
from agents.HumanPacman import HumanPacman
from WorldRendering import WorldRendering
from Mazes import Mazes

WRITER = Turtle(visible=False)
VERDANA_BOLD = ("Verdana", 16, "bold")

TILE_SIZE = 20
EMPTY_TILE = 2
MAZES = Mazes
MAZE = MAZES.level_1
MAX_SCORE = Mazes.level_1_max_score
WORLD = WorldRendering(MAZE)

state = {'score': 0}

# Return offset of point in tiles.
def offset(point):
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Return True if point is valid in tiles.
def valid(point):
    index = offset(point)
    if MAZE[index] == 0:
        return False

    index = offset(point + 19)
    if MAZE[index] == 0:
        return False
    
    is_in_column = point.y % TILE_SIZE == 0
    is_in_row = point.x % TILE_SIZE == 0
    return is_in_row or is_in_column

# Move pacman and all ghosts.
def move():
    clear()
    index = offset(pacman.position)

    if MAZE[index] == 1:
        MAZE[index] = EMPTY_TILE
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        WORLD.draw_square(x, y)

    WRITER.undo()
    WRITER.write(state['score'], font = VERDANA_BOLD)
    up()
    goto(pacman.position.x + 10, pacman.position.y + 10)
    dot(TILE_SIZE, 'yellow')

    if state['score'] == MAX_SCORE:
        end_game("You won!", "yellow")
        return

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(TILE_SIZE, 'red')

    pacman.step(None)

    update()

    for point, course in ghosts:
        if abs(pacman.position - point) < 20:
            end_game("You lost!", "red")
            return

    ontimer(move, 100)

def end_game(message, tcolor):
    WRITER.penup()
    WRITER.goto(0, 180)
    WRITER.color(tcolor)
    WRITER.pendown()
    WRITER.write(message, align="center", font = VERDANA_BOLD)

pacman = HumanPacman(vector(-40, -80), valid)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
WRITER.goto(160, 160)
WRITER.color('white')
WRITER.write(state['score'], font = VERDANA_BOLD)
listen()
WORLD.world()
move()
done()
