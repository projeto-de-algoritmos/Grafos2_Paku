import utils
import graph

import heapq
import random

def buildTree(g, tree, edges):
    for i in range(0, 17):
        for j in range(0, 13):
            tree.add_node(utils.coord_str(i, j))

    for edge in edges:
        tree.add_edge(edge[0], edge[1], 0)

def breakWalls(tree: graph.Graph, edges):

    for i in range(0, 17):
        for j in range(0, 13):
            node = tree.node_dict[utils.coord_str(i, j)]


            if len(node.get_bros()) == 1:
                side = [1, 2, 3, 4]
                coords = utils.coord_int(node.get_id())

                for bro in node.get_bros():
                    bro_coords = utils.coord_int(bro.get_id())

                if coords[0] > bro_coords[0]: # bro a esquerda
                    side.remove(3)
                elif coords[0] < bro_coords[0]: # bro a direita
                    side.remove(1)
                elif coords[1] > bro_coords[1]: # bro acima
                    side.remove(4)
                elif coords[1] < bro_coords[1]: # bro abaixo
                    side.remove(2)

                if(coords[0] == 0):
                    side.remove(3)
                if(coords[1] == 0):
                    side.remove(4)
                if(coords[0] == 16):
                    side.remove(1)
                if(coords[1] == 12):
                    side.remove(2)

                s = random.choice(side)
                side.remove(s)

                if s == 1: # DIREITA
                    next_node = tree.get_node(utils.coord_str(coords[0]+1, coords[1]))
                elif s == 2: # BAIXO
                    next_node = tree.get_node(utils.coord_str(coords[0], coords[1]+1))
                elif s == 3: # ESQUERDA
                    next_node = tree.get_node(utils.coord_str(coords[0]-1, coords[1]))
                elif s == 4: # CIMA
                    next_node = tree.get_node(utils.coord_str(coords[0], coords[1]-1))

                tree.add_edge(node, next_node, 0)
                edges.append((node.get_id(), next_node.get_id()))


def prim_maze(g, start, edges):
    tree = graph.Graph()
    edges = []
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
                
    buildTree(g, tree, edges)
    breakWalls(tree, edges)

    return tree, edges