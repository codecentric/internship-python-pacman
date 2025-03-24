# Pacman, classic arcade game.

from agents.HumanPacman import HumanPacman
from agents.Ghost import Ghost
from WorldRendering import *
from Mazes import *

def update_world():
    """Updates the world repeatedly until the game finishes. 
    - Moves pacman and all ghosts.
    - Checks if game is lost/won.
    """
    clear()
    index = MAZE.offset(pacman.position)
    if MAZE.maze[index] == TILE_DOT:
        MAZE.maze[index] = TILE_EMPTY
        state["score"] += 1
        WORLD.render_empty_tile(index)
    WORLD.render_score(state["score"])

    # move all agents
    for ghost in ghosts:
        ghost.step(get_agent_game_state(ghost))
        WORLD.render_agent(ghost)
    pacman.step(get_agent_game_state(pacman))
    WORLD.render_agent(pacman)
    update()

    # check for game end
    if state["score"] == MAZE.MAX_SCORE:
        WORLD.render_end_game("You won!", "yellow")
        return
    for ghost in ghosts:
        if abs(pacman.position - ghost.position) < TILE_SIZE:
            WORLD.render_end_game("You lost!", "red")
            return

    ontimer(update_world, 100)

def get_agent_game_state(agent):
    """Returns the part of the world that the given agent can see.
    Currently, each agent has a complete view of the world.
    """
    agent_state = {}
    agent_state["score"] = state["score"]
    agent_state["max_score"] = MAZE.MAX_SCORE
    agent_state["surrounding"] = MAZE.maze
    agent_state["pacman"] = pacman.position
    agent_state["ghosts"] = [ghost.position for ghost in ghosts]
    return agent_state

MAZE = LEVEL1
WORLD = WorldRendering(MAZE)
WRITER = Turtle(visible=False)


# level 1
pacman = HumanPacman(vector(-40, -80), MAZE.valid)
ghosts = [
    Ghost(vector(-180, 160), MAZE.valid),
    Ghost(vector(-180, -160), MAZE.valid),
    Ghost(vector(100, 160), MAZE.valid),
    Ghost(vector(100, -160), MAZE.valid),
]

state = {"score": 0}
setup(420, 420, 370, 0) # window
hideturtle()
tracer(False)
listen()
WORLD.world()
update_world()
done()
