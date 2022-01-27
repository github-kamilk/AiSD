import sys

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'  # new: color of node
        self.dist = sys.maxsize  # new: distance from beginning (will be used later)
        self.pred = None  # new: predecessor
        self.disc = 0  # new: discovery time
        self.fin = 0  # new: end-of-processing time

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def set_color(self, color):
        self.color = color

    def set_distance(self, d):
        self.dist = d

    def set_pred(self, p):
        self.pred = p

    def set_discovery(self, dtime):
        self.disc = dtime

    def set_finish(self, ftime):
        self.fin = ftime

    def get_finish(self):
        return self.fin

    def get_discovery(self):
        return self.disc

    def get_pred(self):
        return self.pred

    def get_distance(self):
        return self.dist

    def get_color(self):
        return self.color

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.set_color('white')
            aVertex.set_pred(-1)
        for aVertex in self:
            if aVertex.get_color() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == 'white':
                next_vertex.set_pred(start_vertex)
                self.dfsvisit(next_vertex)
        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish(self.time)


def bfs(start):
    start.set_distance(0)  # distance 0 indicates it is a start node
    start.set_pred(None)  # no predecessor at start
    vert_queue = Queue()
    vert_queue.enqueue(start)  # add start to processing queue
    while (vert_queue.size() > 0):
        current_vert = vert_queue.dequeue()  # pop next node to process -> current node
        for nbr in current_vert.get_connections():  # check all neighbors of the current node
            if (nbr.get_color() == 'white'):  # if the neighbor is white
                nbr.set_color('gray')  # change its color to grey
                nbr.set_distance(current_vert.get_distance() + 1)  # set its distance
                nbr.set_pred(current_vert)  # current node is its predecessor
                vert_queue.enqueue(nbr)  # add it to the queue
        current_vert.set_color('black')  # change current node to black after vi


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
