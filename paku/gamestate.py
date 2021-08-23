import utils
import prim
import player
import ghost
import pellets

import pyxel
import random

player1 = player.Player()
blinky = ghost.Blinky()
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

            # PLAYER PELLET COLISÃO
            player_pos = utils.get_pos_in_grid(player1.posX, player1.posY)
            pellet = pellets_list.pellets_dict.get(player_pos)
            if pellet != None:
                if pellet == 2:
                    player1.points += 9
                    blinky.change_state("frightened")
                pellets_list.pellets_dict.pop(player_pos)
                player1.points += 1

            # PLAYER GHOST COLISÃO
            if player1.atNode == blinky.atNode:
                if blinky.state == "chase":
                    player1.isAlive = False
                    self.state = "game_over"
                elif blinky.state == "frightened":
                    blinky.change_state("eaten")
                
            
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
            
            pellets_list.draw()
            player1.draw()
            blinky.draw()


            
        elif(self.state == "run"):
            utils.draw_grid()

            for i in range(0, len(utils.edges)):
                utils.cave_paint(utils.edges[i][0], utils.edges[i][1])
            
            pyxel.text(utils.WIDTH-40, utils.HEIGHT-20, f'PONTOS: {player1.points}', 7)
            pellets_list.draw()
            player1.draw()
            blinky.draw()

        elif(self.state == "game_over"):
            pyxel.text(utils.WIDTH/2, utils.HEIGHT/2, f'PONTOS: {player1.points}', 7)
            pyxel.text(utils.WIDTH/2, utils.HEIGHT/2-20, 'GAME OVER', 7)
            

