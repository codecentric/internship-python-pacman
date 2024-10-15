from turtle import *

class WorldRendering:
    WRITER = Turtle(visible=False)

    def __init__(self, maze):
        self.maze = maze

    # Draw square using path at (x, y).
    def draw_square(self, x, y):
        self.WRITER.up()
        self.WRITER.goto(x, y)
        self.WRITER.down()
        self.WRITER.begin_fill()

        for count in range(4):
            self.WRITER.forward(20)
            self.WRITER.left(90)

        self.WRITER.end_fill()

    # Draw world using path.
    def world(self):
        bgcolor('black')
        self.WRITER.color('blue')

        for index in range(len(self.maze)):
            tile = self.maze[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                self.draw_square(x, y)

                if tile == 1:
                    self.WRITER.up()
                    self.WRITER.goto(x + 10, y + 10)
                    self.WRITER.dot(2, 'white')