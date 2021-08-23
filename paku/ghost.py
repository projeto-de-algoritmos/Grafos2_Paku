from entity import Entity
import utils

import pyxel
import random

class Ghost(Entity):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.state = "chase"
        self.posX = utils.align_in_grid(x) + 1
        self.posY = utils.align_in_grid(y) + 1
        self.home = [self.posX, self.posY]
        self.target = None
        self.color = 0
        self.base_color = 0
        self.gost_path = []
      
    def draw(self):
        if self.state != "eaten":
            pyxel.circ(self.posX, self.posY, 4, self.color)
            utils.rect_custom(self.posX-4, self.posY, self.posX+5, self.posY+5, self.color)

            if pyxel.frame_count%30 >= 15:
                pyxel.pset(self.posX-4, self.posY+5, self.color)
                pyxel.pset(self.posX-2, self.posY+5, self.color)
                pyxel.pset(self.posX, self.posY+5, self.color)
                pyxel.pset(self.posX+2, self.posY+5, self.color)
                pyxel.pset(self.posX+4, self.posY+5, self.color)
            else:
                pyxel.pset(self.posX-3, self.posY+5, self.color)
                pyxel.pset(self.posX-1, self.posY+5, self.color)
                pyxel.pset(self.posX+1, self.posY+5, self.color)
                pyxel.pset(self.posX+3, self.posY+5, self.color)


        pyxel.circ(self.posX-2, self.posY-1, 1, 7)
        pyxel.circ(self.posX+2, self.posY-1, 1, 7)
        pyxel.pset(self.posX-2, self.posY-1, 0)
        pyxel.pset(self.posX+2, self.posY-1, 0)

        # Código para desenhar o caminho encontrado pelo Dijkstra
        # if self.gost_path != []:
        #     for i in self.gost_path:
        #         pos = utils.coord_int(i)
        #         pyxel.circ(pos[0]*15+7, pos[1]*15+7, 2, 11)
                
        #         if i == self.gost_path[-1]:
        #             pyxel.circ(pos[0]*15+7, pos[1]*15+7, 1, 8)
    
    def random_move(self):
        # CÓDIGO DE MOVIMENTAÇÃO ALETÓRIA DO FANTASMA 
        dir = self.directions()

        if dir == []:
            dir = ["up", "down", "right", "left"]

        return random.choice(dir)

    def change_state(self, state):
        self.state = state

        if state == "chase":
            self.facing = utils.inv_dir(self.facing)
            self.color = self.base_color

        if state == "frightened":
            self.facing = utils.inv_dir(self.facing)
            self.color = 12

        if state == "eaten":
            self.posX = self.home[0]
            self.posY = self.home[1]
            self.color = 0
