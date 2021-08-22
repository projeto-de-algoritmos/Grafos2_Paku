import utils
import prim
import player
import ghost

import pyxel
import random

player1 = player.Player()
blinky = ghost.Blinky()

class GameState:
    def __init__(self):
        self.state = "menu"

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if(self.state == "menu"):
            ...
        if(self.state == "start"):
            for i in range(0, 17):
                for j in range(0, 13):
                    utils.g.add_node(utils.coord_str(i, j))

            for i in range(0, 17):
                for j in range(0, 13):
                    if(i != 0):
                        utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i-1, j), random.randint(1, 20))
                    if(j != 0):
                        utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j-1), random.randint(1, 20))
                    if(i != 16):
                        utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i+1, j), random.randint(1, 20))
                    if(j != 12):
                        utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j+1), random.randint(1, 20))

            # if menu var ...
            start = utils.coord_str(random.randint(0, 16), random.randint(0, 12))
            utils.path, utils.edges = prim.prim_maze(utils.g, start, utils.edges)

            self.state = "prim"
                
        elif(self.state == "prim"):

            if(utils.delay!=len(utils.edges)-1):
                utils.delay += 1
            else:
                self.state = "run"

        elif(self.state == "run"):
            player1.update()
            blinky.update(player1.atNode)
        elif(self.state == "game_over"):
            ...

    def draw(self):
        pyxel.cls(0)

        if(self.state == "menu"):
            ...
        elif(self.state == "start"):
            utils.draw_grid()
            
        elif(self.state == "prim"):
            utils.draw_grid()

            if utils.edges != []:
                for i in range(0, utils.delay+1):
                    utils.cave_paint(utils.edges[i][0], utils.edges[i][1])

            player1.draw()
            blinky.draw()
            
        elif(self.state == "run"):
            utils.draw_grid()

            for i in range(0, len(utils.edges)):
                utils.cave_paint(utils.edges[i][0], utils.edges[i][1])
            
            player1.draw()
            blinky.draw()

        elif(self.state == "game_over"):
            ...

