from entity import Entity
import utils

import pyxel
import random
import heapq

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
        self.gost_path = []
      
    def draw(self):
        pyxel.circ(self.posX, self.posY, 4, self.color)
        utils.rect_custom(self.posX-4, self.posY, self.posX+5, self.posY+5, self.color)
        pyxel.circ(self.posX-2, self.posY-1, 1, 7)
        pyxel.circ(self.posX+2, self.posY-1, 1, 7)
        pyxel.pset(self.posX-2, self.posY-1, 0)
        pyxel.pset(self.posX+2, self.posY-1, 0)

        # Código para ver o caminho encontrado pelo Dijkstra
        for i in self.gost_path:
            pos = utils.coord_int(i)
            pyxel.circ(pos[0]*15+7, pos[1]*15+7, 2, 11)
            
            if i == self.gost_path[-1]:
                pyxel.circ(pos[0]*15+7, pos[1]*15+7, 1, 8)
    

# O Blinky (Ghost Vermelho): Utiliza o Algoritmo de Dijkstra para achar o menor caminho até o Player 
class Blinky(Ghost):
    def __init__(self) -> None:
        super().__init__()
        self.posX = 8
        self.posY = 8
        self.home = [self.posX, self.posY]
        self.color = 8
        self.facing = "right"

    def update(self, player_node):
        self.atNode = utils.get_node_in_grid(self.posX, self.posY)
        
        if (self.posX+7)%15 == 0 and (self.posY+7)%15 == 0:
            self.canTurn = True
            self.calc_target(player_node)
        else:
            self.canTurn = False

        # CÓDIGO DE MOVIMENTAÇÃO ALETÓRIA DO FANTASMA
        
        # if self.canTurn:
        #     dir = ["up", "down", "right", "left"]

        #     if self.facing == "up": dir.remove("down")
        #     elif self.facing == "left": dir.remove("right")
        #     elif self.facing == "down": dir.remove("up")
        #     elif self.facing == "right": dir.remove("left")

        #     choice = random.choice(dir)
        #     self.turn(choice)

        if self.canTurn and self.gost_path != []:
            next_node = utils.coord_int(self.gost_path[-1])
            ghost_node = utils.coord_int(self.atNode.get_id())

            dir = self.facing

            if ghost_node[0] > next_node[0]:
                if self.facing != "right":
                    dir = "left"
            elif ghost_node[0] < next_node[0]:
                if self.facing != "left":
                    dir = "right"
            elif ghost_node[1] > next_node[1]:
                if self.facing != "down":
                    dir = "up"
            elif ghost_node[1] < next_node[1]:
                if self.facing != "up":
                    dir = "down"

            self.turn(dir)

        self.move()

    def calc_target(self, player_node):
        visited = [] #Nós visitados
        end = player_node.get_id()
        current = self.atNode.get_id()
        pq  = []
        nodeData = {}
        for x in utils.path.get_nodes():
            nodeData[x] = {'weight': float('inf'), 'parent': []}
        
        nodeData[current]['weight'] = 0
        while len(visited)+1 < utils.path.num_nodes:
            if current not in visited:
                visited.append(current)
                node_dij = utils.path.get_node(current)
                for neighbour in node_dij.get_bros():
                    neighbour = neighbour.get_id()

                    if neighbour not in visited:
                        weight = nodeData[current]['weight'] + 1
                        if weight < nodeData[neighbour]['weight']:
                            nodeData[neighbour]['weight'] = weight
                            nodeData[neighbour]['parent'] = current

                        heapq.heappush(pq, (nodeData[neighbour]['weight'], neighbour))
                heapq.heapify(pq)
            _, current = heapq.heappop(pq)
            
        x = end
        self.gost_path = []
        while x != self.atNode.get_id():
            self.gost_path.append(x)
            x = nodeData[x]['parent']
