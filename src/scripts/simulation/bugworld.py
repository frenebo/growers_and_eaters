import numpy as np

class Grower:
    def __init__(self, x,y):
        self._x = x
        self._y = y
    
    def set_pos(self, x, y):
        self._x = x
        self._y = y
    
    def get_pos(self):
        return self._x, self._y

class BugWorld:
    def __init__(self,
                 width=100,
                 height=100,
                 ):
        self.width = width
        self.height = height

        self.growers = []
    
    
    def add_random_growers(self, count):
        x_positions = np.random.uniform(0, self.width-1, count)
        y_positions = np.random.uniform(0, self.height-1, count)
        grower_coords = np.vstack([x_positions, y_positions]).T
        for x,y in grower_coords:
            self.growers.append(
                Grower(x,y)
            )
        
    def iterate_simulation(self):
        for g in self.growers:
            oldx, oldy = g.get_pos()
            # move to random point within a 2x2 square centered on starting position
            newx = oldx + np.random.uniform(-1,1)
            newy = oldy + np.random.uniform(-1,1)
            g.set_pos(newx,newy)
        # g_positions = [g.get_pos() for g in self.growers]
        # print(g_positions)
        # g_positions += np.random.uniform(0,1, (len(self.growers), 2))
