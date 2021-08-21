
# grafo = {
#     'a': {'b': 9, 'c': 14, 'd': 15},
#     'b': {'e': 23},
#     'c': {'d': 5, 'e': 18, 'f': 30},
#     'd': {'f': 20, 'h': 44},
#     'e': {'h': 19, 'f': 2},
#     'f': {'g': 11, 'h': 16},
#     'g': {'e': 6, 'h': 6},
#     'h': {},
# }
# nos = []
# def getVertex():
#     for value in grafo.keys():
#         nos.append(value)
# # print(visited)

# def dijkstra(start , end):
#     unvisited = {n: float('inf') for n in nos}
#     unvisited[start] = 0
#     visited = {}
#     parents = {}

#     while len(visited) < len(nos):
#         min_ = min(unvisited, key=unvisited.get)
#         #print(min)
#         for neighbour, _ in grafo.get(min_ , {}).items():
#             if neighbour in visited:
#                 continue
#             nDist = unvisited[min_] + grafo[min_].get(neighbour, float('inf'))
#             if nDist < unvisited[neighbour]:
#                 unvisited[neighbour] = nDist
#                 parents[neighbour] = min_
#             # print(f'{neighbour}: {nDist}')
#         visited[min_] = unvisited[min_]
#         unvisited.pop(min_)
#         if min_ == end:
#             break
#     return parents, visited

# def path(parents, start, end):
#     lst = []
#     current = end
#     lst.append(current)
    
#     while current != start:
#         current = parents[current]
#         lst.append(current)

#     while lst:
#         print(lst.pop(), end= " -> ")
#         if len(lst) == 1:
#             print(lst.pop())




# start = 'a'
# end = 'h'
# getVertex()
# parents, visited = dijkstra(start, end)
# print(f'Caminho de {start} para {end}: ', end=" ")
# path(parents, start, end)
# print(f'Tempo gasto para sair da cidade {start} -> {end}: {visited[end]}')
import heapq
grafo  = {
    's': {'2': 9, '6': 14, '7': 15},
    '2': {'3': 23},
    '6': {'7': 5, '3': 18, '5': 30},
    '7': {'5': 20, 't': 44},
    '3': {'t': 19, '5': 2},
    '5': {'4': 11, 't': 16},
    '4': {'3': 6, 't': 6},
    't': {},
}
nos = []
pq = []
nodeData = {}
def getVertex():
    for value in grafo.keys():
        nos.append(value)
# print(visited)

def buildNodeData():
    for x in grafo.keys():
        nodeData[x] = {'time': float('inf'), 'parent': []}

def dijkstra(start , end):
    buildNodeData()
    nodeData[start]['time'] = 0
    visited = [] #Nós visitados
    current = start # nó atual
    while len(visited) < len(grafo):
        if current not in visited:
            visited.append(current)
            # Para cada vizinho do nó qu não foi vizitado re-calcula o tempo gasto
            for neighbour in grafo[current]: 
                if neighbour not in visited:
                    # Calculo do tempo da aresta mais o tempo acumulado até o nó pai
                    time = nodeData[current]['time'] + grafo[current][neighbour]
                    # se o tempo for menor do que o armazenado, substitui o tempo e o nó pai
                    if time < nodeData[neighbour]['time']:
                        nodeData[neighbour]['time'] = time
                        nodeData[neighbour]['parent'] = nodeData[current]['parent'] + list(current)
                    # Armazena numa heap os nós vizinho conhecidos por current
                    heapq.heappush(pq, (nodeData[neighbour]['time'], neighbour))
        heapq.heapify(pq)
        # tira da heap o nó que forma a aresta com o antigo current com menor time
        _, current = heapq.heappop(pq)
    print(f'''DISTANCIA MINIMA: {nodeData[end]['time']}''')
    print(f'''MENOR CAMINHO: {nodeData[end]['parent'] + list(end)}''')    



start = 's'
end = 't'
getVertex()
dijkstra(start, end)