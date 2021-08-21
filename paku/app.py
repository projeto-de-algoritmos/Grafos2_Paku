import utils 
import graph
import prim

import heapq
import pyxel
import random


class App:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="Project Paku", fps=30)
        pyxel.mouse(True)       
        self.delay = 0

        self.gamestate = GameState()

        self.g = graph.Graph()
        self.tree = graph.Graph()
        self.edges = []

        for i in range(0, 17):
            for j in range(0, 13):
                self.g.add_node(utils.coord_str(i, j))

        for i in range(0, 17):
            for j in range(0, 13):
                if(i != 0):
                    self.g.add_edge(utils.coord_str(i, j), utils.coord_str(i-1, j), random.randint(1, 20))
                if(j != 0):
                    self.g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j-1), random.randint(1, 20))
                if(i != 16):
                    self.g.add_edge(utils.coord_str(i, j), utils.coord_str(i+1, j), random.randint(1, 20))
                if(j != 12):
                    self.g.add_edge(utils.coord_str(i, j), utils.coord_str(i, j+1), random.randint(1, 20))

        start = utils.coord_str(random.randint(0, 16), random.randint(0, 12))
        self.tree, self.edges = prim.prim_maze(self.g, start, self.edges)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        gamestate.update()


    def draw(self):
        pyxel.cls(0)

        for i in range(0, 18):
            pyxel.line(15*i, 0, 15*i, utils.HEIGHT, 7)

        for i in range(0, 14):
            pyxel.line(0, 15*i, utils.WIDTH, 15*i, 7)
            
        for i in range(1, 17):
            for j in range(1, 13):
                pyxel.pset(15*i, 15*j, 8)
        
        for i in range(0, self.delay+1):
            utils.cave_paint(self.edges[i][0], self.edges[i][1])

        if(self.delay!=len(self.edges)-1):
            self.delay += 1
App()