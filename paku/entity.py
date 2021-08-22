import utils

class Entity:
    def __init__(self) -> None:
        self.posX = 0
        self.posY = 0
        self.atNode = None
        self.canTurn = True
        self.facing = None
        
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