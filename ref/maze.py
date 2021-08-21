import pygame
import random
import time

WIDTH, HEIGHT = 510, 510
FPS = 30

GREEN = (000, 255, 000)
WHITE = (255, 255, 255)
RED = (255, 0, 0)



pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

grid = []

def build_grid(initial_x, y, lines, columns, w):
    '''
        Desenha o Grid: Recebe x inicial, y inicial e o tamanho de cada quadrado do grid
    '''
    for _ in range(0,lines):
        x = initial_x
        for _ in range(0, columns):
            pygame.draw.line(screen, WHITE,(x, y), (x + w, y))
            pygame.draw.line(screen, WHITE,(x + w, y), (x + w, y + w))
            pygame.draw.line(screen, WHITE,(x + w, y + w), (x, y + w))
            pygame.draw.line(screen, WHITE,(x, y + w), (x, y))
            grid.append((x,y))
            x += w
        y += w

def paint_right(pos_x, pos_y):
    pygame.draw.rect(screen, RED, (pos_x+1, pos_y+1, 2*w-1, w-1), 0)
    pygame.display.update()

def paint_left(pos_x, pos_y):
    pygame.draw.rect(screen, RED, (pos_x - w+1, pos_y+1, 2*w-1, w-1), 0)
    pygame.display.update()

def paint_up(pos_x, pos_y):
    pygame.draw.rect(screen, RED, (pos_x+1, pos_y - w+1, w-1, 2*w-1), 0)
    pygame.display.update()

def paint_down(pos_x, pos_y):
    pygame.draw.rect(screen, RED, (pos_x+1, pos_y+1, w-1 ,2*w-1), 0)
    pygame.display.update()

def point_cell(x, y):
    pygame.draw.rect(screen, GREEN, (x +1, y +1, w-2, w-2), 0)
    pygame.display.update()


stack = []
solution = {}
visited = []

def build_maze_dfs(x, y):
    '''
        Constroi o labirinto utilizando DFS
    '''
    # point_cell(x,y)
    stack.append((x, y))

    while len(stack):
        right = (x + w, y)
        left = (x - w, y)
        up = (x, y - w)
        down = (x, y + w) 

        time.sleep(0.02)
        cell = []

        if right not in visited and right in grid:
            cell.append('r')
        if left not in visited and left in grid:
            cell.append('l')
        if up not in visited and up in grid:
            cell.append('u')
        if down not in visited and down in grid:
            cell.append('d')
        
        if len(cell) > 0:
            option = (random.choice(cell))
            
            if option == 'r':

                paint_right(x,y)
                solution[x,y] = right
                x,y = right
                visited.append((x,y))
                stack.append((x,y))

            elif option == 'l':
                paint_left(x,y)

                solution[x,y] = left
                x,y = left
                visited.append((x,y))
                stack.append((x,y))
            elif option == 'u':
                paint_up(x,y)
                solution[x,y] = up
                x,y = up
                visited.append((x,y))
                stack.append((x,y))
            
            elif option == 'd':
                paint_down(x,y)
                solution[x,y] = down
                x,y = down
                visited.append((x,y))
                stack.append((x,y))
        
        else:
            x,y = stack.pop()
            time.sleep(0.02)
            # point_cell(x, y)


# Define o tamanho do labirinto
numb_columns = 10
numb_lines = 10
w = (WIDTH - 10)/numb_columns
x, y = 5, 5

# Desenha o grid
build_grid(x, y, numb_lines, numb_columns, w)

build_maze_dfs(x, y)
print(solution)
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