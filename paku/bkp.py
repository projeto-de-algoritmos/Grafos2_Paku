import utils 

import heapq
import pyxel
import random

class Node:
    def __init__(self, node):
        self.id = node
        self.bros = {}

    def __str__(self):
        return str(self.id) + str([x.id for x in self.bros])

    # Adiciona vizinho a lista de adjacência
    def add_bro(self, bro, weight=0):
        self.bros[bro] = weight
    
    # Retorna lista de vizinhos
    def get_bros(self):
        return self.bros.keys()  

    # Retorna ID do nó
    def get_id(self):
        return self.id

    # Retorna PESO da aresta do nó com o vizinho
    def get_weight(self, neighbor):
        return self.bros[neighbor]

class Graph:
    def __init__(self):
        self.node_dict = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.node_dict.values())

    # Adciona nó ao grafo
    def add_node(self, node):
        self.num_nodes = self.num_nodes + 1
        new_node = Node(node)
        self.node_dict[node] = new_node
        return new_node

    # Retorna nó se ele estiver no grafo
    def get_node(self, n):
        if n in self.node_dict:
            return self.node_dict[n]
        else:
            return None

    # Adiciona aresta entre 2 nós
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.node_dict:
            self.add_node(frm)
        if to not in self.node_dict:
            self.add_node(to)

        self.node_dict[frm].add_bro(self.node_dict[to], cost)
        self.node_dict[to].add_bro(self.node_dict[frm], cost)

    # Retorna dicionário com nós
    def get_nodes(self):
        return self.node_dict.keys()

g = Graph()

for i in range(0, 17):
    for j in range(0, 13):
        g.add_node(utils.coord(i, j))

for i in range(0, 17):
    for j in range(0, 13):
        if(i != 0):
            g.add_edge(utils.coord(i, j), utils.coord(i-1, j), random.randint(1, 20))
        if(j != 0):
            g.add_edge(utils.coord(i, j), utils.coord(i, j-1), random.randint(1, 20))
        if(i != 16):
            g.add_edge(utils.coord(i, j), utils.coord(i+1, j), random.randint(1, 20))
        if(j != 12):
            g.add_edge(utils.coord(i, j), utils.coord(i, j+1), random.randint(1, 20))


tree = Graph()
edges = []
def paint(current, bro):
    current_pos = utils.coord_convert(current)
    bro_pos = utils.coord_convert(bro)

    x1 = current_pos[0]*15+1
    y1 = current_pos[1]*15+1
    x2 = bro_pos[0]*15+1
    y2 = bro_pos[1]*15+1
    
    if x1 < x2 or y1 < y2:
        x2 += 14
        y2 += 14
    elif x1 > x2 or y1 > y2:
        x1 += 14
        y1 += 14

    utils.rect_custom(x1, y1, x2, y2, 8)
         
def buildTree(start):
    visited = []
    for i in range(0, 17):
        for j in range(0, 13):
            tree.add_node(utils.coord(i, j))

    for edge in edges:
        tree.add_edge(edge[0], edge[1], 0)

def prim(start):
    candidatas = []
    visited = []
    for u in g.node_dict[start].get_bros():
        heapq.heappush(candidatas,(g.node_dict[start].get_weight(u), (g.node_dict[start].get_id(), u.get_id())))
    visited.append(g.node_dict[start].get_id())
    
    while len(visited) < g.num_nodes:
        _ , (node_u,node_v) = heapq.heappop(candidatas)

        if node_v not in visited:
            visited.append(node_v)
            edges.append((node_u,node_v))
            current = node_v
            for bro in g.node_dict[current].get_bros():
                heapq.heappush(candidatas,(g.node_dict[current].get_weight(bro), (current, bro.get_id())))
                
    buildTree(start)

start = utils.coord(random.randint(0, 16), random.randint(0, 12))
prim(start)

class App:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="Project Paku")
        pyxel.mouse(True)       
        self.delay = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        for i in range(0, 18):
            pyxel.line(15*i, 0, 15*i, utils.HEIGHT, 7)

        for i in range(0, 14):
            pyxel.line(0, 15*i, utils.WIDTH, 15*i, 7)
        
        for i in range(0, self.delay+1):
            paint(edges[i][0], edges[i][1])

        if(self.delay!=len(edges)-1):
            self.delay += 1
App()