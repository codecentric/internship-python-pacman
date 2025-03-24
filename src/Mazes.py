from freegames import vector


class Maze:
    def __init__(self, maze, number_of_rows, number_of_columns, tile_size=20):
        self.maze = maze
        self.NTILES_X = number_of_columns 
        self.NTILES_Y = number_of_rows
        self.TILE_SIZE = tile_size
        max_score = 0
        for i in self.maze:
            if i == TILE_DOT:
                max_score += 1
        self.MAX_SCORE = max_score

    def _get_min_x(self):
        return - self.NTILES_X * self.TILE_SIZE // 2
    
    def _get_max_x(self):
        return self.NTILES_X * self.TILE_SIZE // 2
    
    def _get_min_y(self):
        return - self.NTILES_Y * self.TILE_SIZE // 2 
    
    def _get_max_y(self):
        return self.NTILES_Y * self.TILE_SIZE // 2
    
    def offset(self, point):
        """Returns the offset of a 2D point in tiles.
        
        - The point is given in pixels. 
        - The coordinate origin is in the map center.
        - Returns the flat index that corresponds to the index of the tile in the given map.
        """
        MIN_X = self._get_min_x()
        MAX_Y = self._get_max_y()
        x = (point.x - MIN_X) // self.TILE_SIZE
        y = (MAX_Y - self.TILE_SIZE - point.y) // self.TILE_SIZE
        index = int(x + y * self.NTILES_X)
        return index
    
    def point(self, offset):
        """Given a tile offset, returns the 2D point in pixels.
        - The coordinate origin is in the map center.
        """
        MIN_X = self._get_min_x()
        MAX_Y = self._get_max_y()
        x = MIN_X + (offset % self.NTILES_X) * self.TILE_SIZE 
        y = MAX_Y - self.TILE_SIZE - (offset // self.NTILES_X) * self.TILE_SIZE
        return vector(x, y)

    def valid(self, position):
        """Return True if the agent position is valid, 
        i.e. if the agent is allowed to move to this position."""
        index = self.offset(position)
        if self.maze[index] == TILE_WALL:
            return False

        index = self.offset(vector(position.x + self.TILE_SIZE-1, position.y - self.TILE_SIZE+1))
        if self.maze[index] == TILE_WALL:
           return False
        
        MIN_X = self._get_min_x()
        MIN_Y = self._get_min_y()
        is_in_column = (MIN_Y + position.y) % self.TILE_SIZE == 0
        is_in_row = (MIN_X + position.x) % self.TILE_SIZE == 0
        return is_in_row or is_in_column


# tile number interpretations
TILE_WALL = 0
TILE_DOT = 1
TILE_EMPTY = 2


level_1 = [
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


LEVEL1 = Maze(level_1, 20, 20)
