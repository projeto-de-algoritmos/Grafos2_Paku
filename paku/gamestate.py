import utils
import prim
import player
import pellets

from blinky import Blinky 
from clyde import Clyde
from pinky import Pinky
from inky import Inky

import pyxel
import random

player1 = player.Player()
ghosts = []
ghosts.append(Blinky(0, 0))
ghosts.append(Inky(0, utils.GRID_HEIGHT-1))
ghosts.append(Pinky(utils.GRID_WIDTH-1, 0))
ghosts.append(Clyde(utils.GRID_WIDTH-1, utils.GRID_HEIGHT-1))
pellets_list = pellets.Pellets()

class GameState:
    def __init__(self):
        self.state = "menu"
        self.points = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if(self.state == "menu"):
            ...
        if(self.state == "start"):

            pellets_list.fill_dict()

            for i in range(0, utils.GRID_WIDTH):
                for j in range(0, utils.GRID_HEIGHT):
                    utils.g.add_node(utils.coord_str(i, j))

            for i in range(0, utils.GRID_WIDTH):
                for j in range(0, utils.GRID_HEIGHT):
                    if(i != 0):
                        utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i-1, j), random.randint(1, 20))
                    if(j != 0):
                        utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j-1), random.randint(1, 20))
                    if(i != utils.GRID_WIDTH-1):
                        utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i+1, j), random.randint(1, 20))
                    if(j != utils.GRID_HEIGHT-1):
                        utils.g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j+1), random.randint(1, 20))

            # if menu var ...
            start = utils.coord_str(random.randint(0, utils.GRID_WIDTH-1), random.randint(0, utils.GRID_HEIGHT-1))
            utils.path, utils.edges = prim.prim_maze(utils.g, start, utils.edges)

            # utils.path, utils.edges = utils.mirror(utils.path, utils.edges)
            utils.path = utils.mirror()

            self.state = "prim"
                
        elif(self.state == "prim"):

            if(utils.delay!=len(utils.edges)-1):
                utils.delay += 1
            else:
                self.state = "run"

        elif(self.state == "run"):
            player1.update()
            (player1.atNode)

            ghosts[1].blinky_pos = [ghosts[0].posX, ghosts[0].posY]
            for ghost in ghosts:
                ghost.update(player1.atNode, player1.facing)

            # PLAYER PELLET COLISÃO
            player_pos = utils.get_pos_in_grid(player1.posX, player1.posY)
            pellet = pellets_list.pellets_dict.get(player_pos)
            if pellet != None:
                if pellet == 2:
                    player1.points += 40
                    
                    for ghost in ghosts:
                        if ghost.state != "eaten":
                            ghost.change_state("frightened")
                        
                pellets_list.pellets_dict.pop(player_pos)
                player1.points += 10

            # PLAYER GHOST COLISÃO
            for ghost in ghosts:
                if player1.atNode.get_id() == ghost.atNode.get_id():
                    if ghost.state == "chase":
                        player1.isAlive = False
                        self.state = "game_over"
                    elif ghost.state == "frightened":
                        player1.points += 100
                        ghost.change_state("eaten")
                    
            
        elif(self.state == "game_over"):
            ...

    def draw(self):
        pyxel.cls(1)

        if(self.state == "menu"):
            ...
        elif(self.state == "start"):
            utils.draw_grid()
            
        elif(self.state == "prim"):
            utils.draw_grid()

            if utils.edges != []:
                for i in range(0, utils.delay+1):
                    utils.cave_paint(utils.edges[i][0], utils.edges[i][1])
            
            pellets_list.draw()
            player1.draw()

            for ghost in ghosts:
                ghost.draw()


            
        elif(self.state == "run"):
            utils.draw_grid()

            for i in range(0, len(utils.edges)):
                utils.cave_paint(utils.edges[i][0], utils.edges[i][1])
            
            pyxel.text(utils.WIDTH-60, utils.HEIGHT-10, f'PONTOS: {player1.points}', 7)
            pellets_list.draw()
            player1.draw()
            
            for ghost in ghosts:
                ghost.draw()

        elif(self.state == "game_over"):
            pyxel.text(utils.WIDTH/2, utils.HEIGHT/2, f'PONTOS: {player1.points}', 7)
            pyxel.text(utils.WIDTH/2, utils.HEIGHT/2-20, 'GAME OVER', 7)
            

