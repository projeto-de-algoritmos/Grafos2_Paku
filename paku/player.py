<<<<<<< HEAD
=======
# import graph
>>>>>>> 33935f0230642d337e9b0765c73e6dd5b7fd70d7
import utils

import pyxel

class Player:
    def __init__(self, atNode=None):
        self.posX = 8
        self.posY = 8
        self.isAlive = True
        self.atNode = atNode
        self.canTurn = True
        self.facing = "right"

    def update(self):
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
            x = ((self.posX+7)//15) - 1
            y = ((self.posY+7)//15) - 1
            self.atNode = utils.g.get_node(utils.coord_str(x, y))

        else:
            self.canTurn = False
        
        if self.isAlive and self.canTurn:
            if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
                if self.facing != "down":
                    self.turn("up")
            if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
                if self.facing != "right":
                    self.turn("left")
            if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
                if self.facing != "up":
                    self.turn("down")
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                if self.facing != "left":
                   self.turn("right")
                   

        self.move()

    def draw(self):
        pyxel.circ(self.posX, self.posY, 4, 10)

    def move(self):

        go = True
        if self.canTurn == True:
            close_node = utils.get_close_node(self.atNode, self.facing)
            if (self.atNode.get_id(), close_node) not in utils.edges and (close_node, self.atNode.get_id()) not in utils.edges:
                go = False

        if go:
            if self.facing == "down":
                self.posY += 1
            if self.facing == "right":
                self.posX += 1
            if self.facing == "up":
                self.posY -= 1
            if self.facing == "left":
                self.posX -= 1
            
    def turn(self, direction):
        if self.canTurn == True:
            close_node = utils.get_close_node(self.atNode, direction)
            if (self.atNode.get_id(), close_node) in utils.edges or (close_node, self.atNode.get_id()) in utils.edges :
                self.facing = direction
                
                
