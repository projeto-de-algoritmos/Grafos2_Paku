import utils
from entity import Entity
import pyxel

class Player(Entity):
    def __init__(self):
        super().__init__()
        
        self.posX = 128
        self.posY = 98
        self.isAlive = True
        self.facing = "right"

    def update(self):
        self.atNode = utils.get_node_in_grid(self.posX, self.posY)
        print(f"player esta em: {self.atNode}")
        
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
        else:
            self.canTurn = False
        
        if self.isAlive and self.canTurn:
            if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
                self.turn("up")
            elif pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
                self.turn("left")
            elif pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
                self.turn("down")
            elif pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                self.turn("right")
                   

        self.move()

    def draw(self):
        pyxel.circ(self.posX, self.posY, 4, 10)

    # def move(self):

    #     go = True
    #     if self.canTurn == True:
    #         close_node = utils.get_close_node(self.atNode, self.facing)
    #         if (self.atNode.get_id(), close_node) not in utils.edges and (close_node, self.atNode.get_id()) not in utils.edges:
    #             go = False

    #     if go:
    #         if self.facing == "down":
    #             self.posY += 1
    #         if self.facing == "right":
    #             self.posX += 1
    #         if self.facing == "up":
    #             self.posY -= 1
    #         if self.facing == "left":
    #             self.posX -= 1
            
    # def turn(self, direction):
    #     if self.canTurn == True:
    #         close_node = utils.get_close_node(self.atNode, direction)
    #         if (self.atNode.get_id(), close_node) in utils.edges or (close_node, self.atNode.get_id()) in utils.edges :
    #             self.facing = direction
                
                
