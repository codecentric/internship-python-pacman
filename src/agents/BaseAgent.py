from freegames import floor, vector

class BaseAgent:

    def __init__(self, position, valid_function) -> None:
        self.position = position
        self.valid = valid_function

    def __move(self, x, y):
        """Change pacman aim if valid."""
        delta = vector(x, y)
        if self.valid(self.position + delta):
            self.position.move(delta)

    def down(self):
        self.__move(0, -5)

    def up(self):
        self.__move(0, 5)

    def left(self):
        self.__move(-5, 0)

    def right(self):
        self.__move(5, 0)

    def step(self, game_state):
        pass
    