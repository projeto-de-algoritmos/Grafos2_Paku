import utils 
import pyxel
import random

# DESCOBRE QUANTAS CELULAS POSSO TER
# for i in range(1, 21):
#     print("pixels por celula: ")
#     print((256-i-1)/i)
#     print("celulas: ")
#     print(i)
#     print()

def rect_custom(x1, y1, x2, y2, color):

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    pyxel.rect(x1, y1, x2-x1, y2-y1, color)

def coord(x, y):
    return (str(x) + "-" + str(y))

def inv_coord(coord):
    st = coord.split("-")
    return [int(st[0]), int(st[1])]
     

class Node:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + str([x.id for x in self.adjacent])

    # Adiciona vizinho a lista de adjacência
    def add_bro(self, bro, weight=0):
        self.adjacent[bro] = weight
    
    # Retorna lista de vizinho
    def get_bros(self):
        return self.adjacent.keys()  

    # Retorna ID do nó
    def get_id(self):
        return self.id

    # Retorna PESO da aresta do nó com o vizinho
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

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

    # Retorna lista de nós 
    def get_nodes(self):
        return self.node_dict.keys()


g = Graph()

for i in range(0, 17):
    for j in range(0, 13):
        g.add_node(coord(i, j))

for i in range(0, 17):
    for j in range(0, 13):
        if(i != 0):
            g.add_edge(coord(i, j), coord(i-1, j), random.randint(1, 20))
        if(j != 0):
            g.add_edge(coord(i, j), coord(i, j-1), random.randint(1, 20))
        if(i != 16):
            g.add_edge(coord(i, j), coord(i+1, j), random.randint(1, 20))
        if(j != 12):
            g.add_edge(coord(i, j), coord(i, j+1), random.randint(1, 20))


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
        
App()