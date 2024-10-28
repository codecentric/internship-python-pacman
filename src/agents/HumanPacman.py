from . import BaseAgent
from turtle import onkey

class HumanPacman(BaseAgent.BaseAgent):
    color = 'yellow'
    
    def step(self, game_state):
        onkey(lambda: self.right(), 'Right')
        onkey(lambda: self.left(), 'Left')
        onkey(lambda: self.up(), 'Up')
        onkey(lambda: self.down(), 'Down')