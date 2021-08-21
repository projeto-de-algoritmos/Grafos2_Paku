import pygame
import random
import time


WIDTH, HEIGHT = 510, 510
FPS = 30

GREEN = (000, 255, 000)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 000)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

class Node:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.neighbors = []

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors.append(neighbor)

class Edge:
    def __init__(self, node_u, node_v):
        self.u = node_u
        self.v = node_v
        self.weight = None
    
    def draw_edge(self):
        pygame.draw.line(screen, WHITE, (self.u.x, self.u.y),(self.v.x, self.v.y))

vertex = []
tree = []

def paint(u, v, w):
    if v.x > u.x:
        pygame.draw.rect(screen, RED, (u.x+1, u.y+1, w-1, w-1), 0)
    elif v.x < u.x:
        pygame.draw.rect(screen, RED, (u.x - w+1, u.y+1, 2*w-1, w-1), 0)
    elif v.y > u.y:
        pygame.draw.rect( screen, RED, (u.x+1, u.y+1, w-1 ,2*w-1), 0)
    elif v.y < u.y:
        pygame.draw.rect(screen, RED, (u.x+1, u.y - w+1, w-1, 2*w-1), 0)

    pygame.display.update()

def build_grid(x, y, lines, columns, w):
    initial = x
    for i in range(0,lines+1):
        vertex.append([])
        x = initial
        for j in range(0, columns+1):
            vertex[i].append(Node(x, y))
            x += w
        y += w
    
    for i in range(0,lines+1):
        for j in range(0,columns):
            vertex[i][j].neighbors.append(Edge(vertex[i][j],vertex[i][j+1]))
            vertex[i][j+1].neighbors.append(Edge(vertex[i][j+1],vertex[i][j]))
            for edge in vertex[i][j].neighbors:
                edge.draw_edge()
        pygame.display.update()

    for i in range(0,lines):
        for j in range(0,columns+1):
            vertex[i][j].neighbors.append(Edge(vertex[i][j],vertex[i+1][j]))
            vertex[i+1][j].neighbors.append(Edge(vertex[i+1][j],vertex[i][j]))
            for edge in vertex[i][j].neighbors:
                edge.draw_edge()
    pygame.display.update()

    #no inicial
    tree.append(vertex[0][0])
    paint(vertex[0][0], vertex[0][1], w)
stack = []
solution = {}
visited = []

def build_maze_dfs(node, w):
    '''
        Constroi o labirinto utilizando DFS
    '''
    #point_cell(x,y)
    stack.append(node)

    while len(stack):
        # right = (x + w, y)
        # left = (x - w, y)
        # up = (x, y - w)
        # down = (x, y + w) 

        time.sleep(0.02)
        cell = []
        for neighbor in node.neighbors:
            if neighbor.v not in visited:
                cell.append(neighbor.v)

        # if right not in visited and right in grid:
        #     cell.append('r')
        # if left not in visited and left in grid:
        #     cell.append('l')
        # if up not in visited and up in grid:
        #     cell.append('u')
        # if down not in visited and down in grid:
        #     cell.append('d')
        
        if len(cell) > 0:
            n = (random.choice(cell))
            
            paint(node, n, w)
            solution[node] = n
            node = n
            visited.append(node)
            stack.append(node)
        else:
            node = stack.pop()
            time.sleep(0.02)
            # point_cell(x, y)

numb_columns = 10
numb_lines = 10
w = (WIDTH - 10)/numb_columns
x, y = 5, 5

# Desenha o grid
build_grid(x, y, numb_lines, numb_columns, w)
build_maze_dfs(vertex[0][0], w)
# Desenha o labirinto
# Game loop
running = True
while running:
    clock.tick(FPS)
    if x >= 400 or y >= 400:
        print(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False