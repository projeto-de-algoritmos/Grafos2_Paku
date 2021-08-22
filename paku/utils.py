import graph

import pyxel

WIDTH = 256
HEIGHT = 196

g = graph.Graph()
tree = graph.Graph()
edges = []
delay = 0

def draw_grid():
    for i in range(0, 18):
        pyxel.line(15*i, 0, 15*i, HEIGHT, 7)

    for i in range(0, 14):
        pyxel.line(0, 15*i, WIDTH, 15*i, 7)
        
    for i in range(1, 17):
        for j in range(1, 13):
            pyxel.pset(15*i, 15*j, 8)

def rect_custom(x1, y1, x2, y2, color):

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    pyxel.rect(x1, y1, x2-x1, y2-y1, color)
    # pyxel.pset(x1, y1, x2-x1, y2-y1, color)

def coord_str(x, y):
    return (str(x) + "-" + str(y))

def coord_int(coord):
    st = coord.split("-")
    return [int(st[0]), int(st[1])]

def cave_paint(current, bro):
    current_pos = coord_int(current)
    bro_pos = coord_int(bro)

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

    rect_custom(x1, y1, x2, y2, 8)


# DEBUG

# DESCOBRE QUANTAS CELULAS POSSO TER
# for i in range(1, 21):
#     print("pixels por celula: ")
#     print((256-i-1)/i)
#     print("celulas: ")
#     print(i)
#     print()