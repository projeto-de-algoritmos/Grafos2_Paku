from entity import Entity
import utils

import pyxel
import random

# Scatter
# Chase
# Frightened
# Eaten

class Ghost(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.mode = "chase"
        self.home = [0, 0]
        self.target = None
        self.color = 0
      
    def draw(self):
        pyxel.circ(self.posX, self.posY, 4, self.color)
        utils.rect_custom(self.posX-4, self.posY, self.posX+5, self.posY+5, self.color)
        pyxel.circ(self.posX-2, self.posY-1, 1, 7)
        pyxel.circ(self.posX+2, self.posY-1, 1, 7)
        pyxel.pset(self.posX-2, self.posY-1, 0)
        pyxel.pset(self.posX+2, self.posY-1, 0)


# O Vermelho
# O target é a posição do Player
class Blinky(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.posX = 8
        self.posY = 8
        self.home = [self.posX, self.posY]
        self.color = 8
        self.facing = "right"


    def update(self):
        self.atNode = utils.get_node_in_grid(self.posX, self.posY)
        
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
            # calc_target(player_pos)
        else:
            self.canTurn = False

        if self.canTurn:
            dir = ["up", "down", "right", "left"]

            if self.facing == "up": dir.remove("down")
            elif self.facing == "left": dir.remove("right")
            elif self.facing == "down": dir.remove("up")
            elif self.facing == "right": dir.remove("left")

            dir.remove(self.facing)
            choice = random.choice(dir)
            self.turn(choice)
                   
        self.move()

    def calc_target(self, player_pos):
        ...
    