from freegames import vector

class BaseAgent:
    color = 'white'
    
    DOWN = vector(0, -5)
    UP = vector(0, 5)
    LEFT = vector(-5, 0)
    RIGHT = vector(5, 0)

    def __init__(self, position, valid_function) -> None:
        self.position = position
        self.valid = valid_function

    def _move(self, delta):
        """Change the agent's position if valid."""
        if self.valid(self.position + delta):
            self.position.move(delta)
            return True
        return False

    def down(self):
        self._move(self.DOWN)

    def up(self):
        self._move(self.UP)

    def left(self):
        self._move(self.LEFT)

    def right(self):
        self._move(self.RIGHT)

    def step(self, game_state):
        pass
