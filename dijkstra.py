
# class Graph():
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)] for row in range(vertices)]



#     def printSolution(self, dist):
#         print("Vertex \t Distance from Source")
#         for node in range(self.V):
#             print(node, "\t\t", dist[node])

#     def minDistance(self, dist, spSet):
#         min = 1e7
#         for v in range(self.V):
#             if dist[v] < min and spSet[v] == False:
#                 min = dist[v]
#                 min_index = v
#         return min_index



graph = {} 
graph['home'] = [['c', 5],['a', 3], ['b', 2] ]
graph['a'] = [['home', 3],['d', 3], ['b', 2] ]
graph['b'] = [['home', 2],['d',1], ['e', 6] ]
graph['c'] = [['home', 5],['d',1], ['e', 2] ]
graph['d'] = [['a', 3],['b',1], ['f', 4] ]
graph['e'] = [['c', 2],['b',6], ['f', 4], ['x', 4] ]
graph['f'] = [['e', 1],['d',4], ['x', 2] ]
graph['x'] = [['f', 2],['3',4]]


visited = []
distance = {}
cur_node = 'home'
to_visit = []
distance[cur_node] = 0


# 1. Loop through all the nodes and add them to to_visit
# 2. Set each distance to infinity, except for the head node.

for i in graph.keys():
    if i != cur_node:
        distance[i] = 1e7
        to_visit.append(i)

print(to_visit)
m = min(distance, key=distance.get)


# visited.append(to_visit.pop(to_visit.index(cur_node)))
# 3. Start the while loop
while len(to_visit) > 0:

    cur_node = min(distance, key=distance.get)
    visited.append(cur_node)

    if graph[cur_node]:
        print("has neightbors")
        for i in graph[cur_node]:
            min_distance = 


            distance[i] = distanc
#         # visited.append(to_visit.pop(to_visit.index(cur_node)))

    cur_node = to_visit.pop(0)






    




    

print('to visit', to_visit, "visited", visited,  cur_node, "\n", distance)
