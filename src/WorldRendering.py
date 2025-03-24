from turtle import *
from freegames import vector
from Mazes import TILE_DOT, TILE_WALL, Maze

TILE_SIZE = 20

class WorldRendering:
    WRITER = Turtle(visible=False)
    SCORE_WRITER = Turtle(visible=False)

    def __init__(self, maze:Maze, font=("Verdana", 16, "bold")):
        self.maze = maze
        self.font = font


    def draw_square(self, x, y):
        """Draw square using path at (x, y)"""
        self.WRITER.up()
        self.WRITER.goto(x, y)
        self.WRITER.down()
        self.WRITER.begin_fill()

        for i in range(4):
            self.WRITER.forward(TILE_SIZE)
            self.WRITER.left(90)

        self.WRITER.end_fill()

    def world(self):
        """Draw world using path"""
        bgcolor("black")
        self.WRITER.color("blue")

        for index in range(len(self.maze.maze)):
            tile = self.maze.maze[index]

            if tile != TILE_WALL:
                x,y = self.maze.point(index)
                self.draw_square(x, y)

                if tile == TILE_DOT:
                    self.WRITER.up()
                    center = self.get_tile_center(vector(x,y))
                    self.WRITER.goto(center)
                    self.WRITER.dot(2, "white")

    def render_agent(self, agent):
        up()
        x, y = self.get_tile_center(agent.position)
        goto(x, y)
        dot(TILE_SIZE, agent.color)

    def render_empty_tile(self, index):
        x,y = self.maze.point(index)
        self.draw_square(x, y)

    def render_score(self, score):
        self.SCORE_WRITER.undo()
        x = self.maze._get_max_x() - 2 * TILE_SIZE
        y = self.maze._get_max_y() - 2 * TILE_SIZE
        self.SCORE_WRITER.goto(x, y)
        self.SCORE_WRITER.color("white")
        self.SCORE_WRITER.write(score, font=self.font)

    def render_end_game(self, message, tcolor):
        self.WRITER.penup()
        self.WRITER.goto(0, self.maze._get_max_y() - 0.8 * TILE_SIZE)
        self.WRITER.color(tcolor)
        self.WRITER.pendown()
        self.WRITER.write(message, align="center", font=self.font)

    def get_tile_center(self, position):
        return vector(position.x + TILE_SIZE/2, position.y + TILE_SIZE/2)
