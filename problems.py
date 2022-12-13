#!/bin/python
import csv
import math

# PROBLEM 1
                
class Graph:
  def __init__(self, edge_list, num_nodes):
    self.graph = edge_list
    self.rev_graph = self.reverse_graph()
    self.num_nodes = num_nodes

    self.traversed_nodes_p1 = []
    self.traversed_nodes_p2 = []

    self.counter = 0
    self.scc_size_list = []

    self.scc_sl()

  def reverse_graph(self):
    r_graph = [];
    for e in self.graph:
      tail = e[0]; 
      head = e[1];
      r_graph.append([head, tail])
    r_graph = sorted(r_graph, key = lambda x: x[0])
    return r_graph

  def dfs_p1(self, starting_node, g, t_nodes): 
    if (starting_node not in t_nodes):
      t_nodes.insert(0, starting_node)
    for i in range (len(g)): 
      if (g[i][0] == starting_node and g[i][1] not in t_nodes):
        self.dfs_p1(g[i][1], g, t_nodes)
  
  def dfs_loop_p1 (self):
    for i in range (1, self.num_nodes+1):
      self.dfs_p1(i, self.rev_graph, self.traversed_nodes_p1)

  def dfs_p2(self, starting_node, g, t_nodes): 
    if (starting_node not in t_nodes):
      self.counter += 1
      t_nodes.append(starting_node)
    for i in range (len(g)): 
      if (g[i][0] == starting_node and g[i][1] not in t_nodes):
        self.dfs_p2(g[i][1], g, t_nodes)
  
  def dfs_loop_p2 (self):
    for i in self.traversed_nodes_p1:
      self.counter = 0
      self.dfs_p2(i, self.graph, self.traversed_nodes_p2)
      if self.counter > 0:
        self.scc_size_list.append(self.counter)
  
  def scc_sl (self):
    self.dfs_loop_p1()
    self.dfs_loop_p2()

    self.scc_size_list.sort()
    self.scc_size_list.reverse()

# Create a graph given in the above diagram
edges = []
with open("color_07.csv", 'r') as file:
    csvreader = csv.reader(file)
    count = 0
    for row in csvreader:
        if row[0] == "vertex":
            continue
        else:
            if len(row) == 1:
                continue
            else:
                # print("row", row)
                for i in range(len(row)):
                    if i != 0 and row[i] != '':
                        edge = (int(row[0]), int(row[i]))
                        edges.append(edge)
            count += 1
list = Graph(edges, count)
print(list.scc_size_list)

# PROBLEM 2


# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
 
# Library for INT_MAX
import sys
 
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, minPaths):
        print("Min Paths")
        for node in range(self.V):
            print(node, "\t", minPaths[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
        
        minPaths = [0] * self.V
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        minPaths[src] = 1
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    minPaths[y] = minPaths[x]
                elif self.graph[x][y] > 0 and sptSet[y] == False and dist[y] == dist[x] + self.graph[x][y]:
                    minPaths[y] += minPaths[x]            
        self.printSolution(minPaths)
adjMatrix = []
with open("numpaths_07.csv", 'r') as file:
    csvreader = csv.reader(file)
    vertex = 0
    for row in csvreader:
        list = []
        for i in range(len(row)):
            if row[i] == "blank":
                list.append(0)
            else:
                list.append(int(row[i]))
        adjMatrix.append(list)
g = Graph(100)
g.graph = adjMatrix
g.dijkstra(0)

# PROBLEM 3
socks = []
threshold = 0.25
pairs = 0
with open("socks_07.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        try:
            socks.append(float(row[0]))
        except ValueError:
            continue
 
socks.sort()
print(socks)
i = 0
while i < len(socks)-1:
    if abs(socks[i] - socks[i+1]) <= threshold:
        print("pair", socks[i], socks[i+1])
        pairs = pairs + 1
        i = i + 2
        continue
    elif abs(socks[i] - socks[i+1]) > threshold:
        i = i + 1
        continue

print(pairs)

# PROBLEM 4

# lamps = []
# with open("example.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         if row[0] == "s_i":
#             continue
#         else:
#             lamp = (int(row[0]), int(row[1]), int(row[2]))
#             lamps.append(lamp)
# dp = []
# for i in range(len(lamps) + 1):
#     row = []
#     for j in range(10 + 1):
#         if i == 0:
#             row.append(2**31)
#         else:
#             row.append(0)
#     dp.append(row)

# for i in range(1, len(dp)):
#     for j in range(1, len(dp[0])):
#         if lamps[i-1][1] < j:
#             dp[i][j] = 2**31
#         if lamps[i-1][0] > j:
#             dp[i][j] = dp[i-1][j]
#         dp[i][j] = min(dp[i-1][j], lamps[i-1][2] + dp[i-1][lamps[i-1][0]-1])
# print(dp)
# print(dp[len(dp)-1][len(dp[0])-1])
