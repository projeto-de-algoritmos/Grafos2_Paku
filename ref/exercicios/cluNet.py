# Prim
# ??? Conferir se é o caminho de menor pesso ou maior
# menor
import heapq

grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 5, 'D': 4, 'E': 4},
    'C': {'A': 3, 'B': 5, 'E': 5},
    'D': {'B': 4, 'E': 2, 'F': 3},
    'E': {'B': 4, 'C': 5, 'D': 2, 'F': 5},
    'F': {'D': 3, 'E': 5},
}

# grafo = {
#     '1': {'2': 6, '4': 5, '3': 1},
#     '2': {'1': 6, '3': 5, '5': 3},
#     '3': {'2': 5, '4': 5, '1': 1, },
#     '4': {'3': 9, '5': 10},
#     '5': {'3': 14, '4': 10, '2': 4, '6': 2},
#     '6': {'5': 2, '7': 1, '8': 6},
# }
tree = {}
edges = []
def buildTree():
    for key in grafo.keys():
        tree.setdefault(key, [])
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    for node, neighbours in tree.items():
        print(f'{node}: {neighbours}')
        

#maior

def prim(start):
    candidatas = []
    visited = []
    for u in grafo[start].keys():
        heapq.heappush(candidatas,(grafo[start][u], (start, u)))
    visited.append(start)
    while len(visited) < len(grafo.keys()):
        # heapq._heapify_max(candidatas)
        _ , (u,v) = heapq._heappop_max(candidatas)
      
        if v not in visited:
            visited.append(v)
            edges.append((u,v))
            current = v
            for value in grafo[v].keys():
                # if value != current:
                heapq.heappush(candidatas,(grafo[v][value], (v, value)))
    buildTree()
    sum = 0
    
    for u, v in edges:
        sum += grafo[u][v]
        print(grafo[u][v], end=" + ")
    print(f'= {sum}')
    
source = 'A'
prim(source)