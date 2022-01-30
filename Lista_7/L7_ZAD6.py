import sys
from L7_ZAD1_5 import Queue, BinHeap, Vertex, Graph

g = Graph()
for i in range(6):
    g.add_vertex(i)

g.add_edge(0, 1, 5)
print(g.vert_list)