# from this page: https://joshuacclark.medium.com/dijkstras-algorithm-with-adjacency-lists-ae2e9301d315 
from collections import defaultdict
import heapq

class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

    def minDistance(self, dist, seen):
        min_d = float('inf')

        for v in range(self.V):
            if v not in seen and dist[v] < min_d:
                min_d = dist[v]
                min_vertex = v
        return min_vertex

    def slow_dijkstra(self, source):
        dist = [float('inf')] * self.V
        seen = set()
        dist[source] = 0

        for _ in range(self.V):
            u = self.minDistance(dist, seen)
            seen.add(u)

            for node, weight in self.graph[u]:
                if node not in seen and dist[node] > dist[u] + weight:
                    dist[node] = dist[u] + weight
        
        self.printSolution(dist)

    def dijkstra(self, source):
        dist = [float('inf')] * self.V
        seen = set()
        heap = []
        dist[source] = 0

        heapq.heappush(heap, (source, dist[source]))

        while len(heap) >0:
            node, weight = heapq.heappop(heap)
            seen.add(weight)

            for conn, w in self.graph[node]:
                if conn not in seen:
                    d = weight + w
                    if d < dist[conn]:
                        dist[conn] = d
                        heapq.heappush(heap, (conn, d))

        self.printSolution(dist)

    def printGraph(self):
        print(self.graph)

    def printSolution(self, dist):
        print("Vertex: \t Distance:")
        for node in range(self.V):
            print(node+1, '\t\t\t', dist[node])

G = Graph(6)
G.addEdge(0,1,3)
G.addEdge(0,3,5)
G.addEdge(0,2,2)
G.addEdge(1,4,3)
G.addEdge(3,5,2)
G.addEdge(2,4,1)
G.addEdge(2,5,6)
G.addEdge(5,,4)
G.addEdge(6,100,2)

# G.addEdge(1,2,10) # G.addEdge(2,5,2)
# G.addEdge(3,2,11)
# G.addEdge(1,3,15)
# G.addEdge(5,4,9)
# G.addEdge(3,4,6)
G.dijkstra(0)
