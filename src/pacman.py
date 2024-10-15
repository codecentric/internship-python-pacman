# Pacman, classic arcade game.

from random import choice
from turtle import *
from freegames import floor, vector
from agents.HumanPacman import HumanPacman

MAZE_WRITER = Turtle(visible=False)
STATE_WRITER = Turtle(visible=False)
VERDANA_BOLD = ("Verdana", 16, "bold")

TILE_SIZE = 20
EMPTY_TILE = 2

state = {'score': 0}

# fmt: off
maze = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on

max_score = 0

for i in maze:
    if i == 1:
        max_score+= 1

# Draw square using path at (x, y).
def square(x, y):
    MAZE_WRITER.up()
    MAZE_WRITER.goto(x, y)
    MAZE_WRITER.down()
    MAZE_WRITER.begin_fill()

    for count in range(4):
        MAZE_WRITER.forward(20)
        MAZE_WRITER.left(90)

    MAZE_WRITER.end_fill()

# Return offset of point in tiles.
def offset(point):
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Return True if point is valid in tiles.
def valid(point):
    index = offset(point)
    if maze[index] == 0:
        return False

    index = offset(point + 19)
    if maze[index] == 0:
        return False
    
    is_in_column = point.y % TILE_SIZE == 0
    is_in_row = point.x % TILE_SIZE == 0
    return is_in_row or is_in_column

# Draw world using path.
def world():
    bgcolor('black')
    MAZE_WRITER.color('blue')

    for index in range(len(maze)):
        tile = maze[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                MAZE_WRITER.up()
                MAZE_WRITER.goto(x + 10, y + 10)
                MAZE_WRITER.dot(2, 'white')

# Move pacman and all ghosts.
def move():
    STATE_WRITER.undo()
    STATE_WRITER.write(state['score'], font = VERDANA_BOLD)

    clear()

    index = offset(pacman.position)

    if maze[index] == 1:
        maze[index] = EMPTY_TILE
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.position.x + 10, pacman.position.y + 10)
    dot(TILE_SIZE, 'yellow')

    if state['score'] == max_score:
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

    ontimer(move, 50)

def end_game(message, tcolor):
    STATE_WRITER.penup()
    STATE_WRITER.goto(0, 180)
    STATE_WRITER.color(tcolor)
    STATE_WRITER.pendown()
    STATE_WRITER.write(message, align="center", font = VERDANA_BOLD)

pacman = HumanPacman(vector(-40, -80), valid)
aim = vector(5, 0)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
STATE_WRITER.goto(160, 160)
STATE_WRITER.color('white')
STATE_WRITER.write(state['score'], font = VERDANA_BOLD)
listen()
world()
move()
done()
