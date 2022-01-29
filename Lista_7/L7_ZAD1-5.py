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


class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.atributes = [0]
        self.current_size = 0

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                tmp = self.heap_list[index // 2]
                tmp2 = self.atributes[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.atributes[index // 2] = self.atributes[index]
                self.heap_list[index] = tmp
                self.atributes[index] = tmp2
            index = index // 2

    def insert(self, k):
        self.heap_list.append(k[0])
        self.atributes.append(k[1])
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def find_min(self):
        return (self.heap_list[1], self.atributes[1])

    def perc_down(self, index):
        while (index * 2) <= self.current_size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                tmp = self.heap_list[index]
                tmp2 = self.atributes[index]
                self.heap_list[index] = self.heap_list[mc]
                self.atributes[index] = self.atributes[mc]
                self.heap_list[mc] = tmp
                self.atributes[mc] = tmp2
            index = mc

    def min_child(self, index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        retatr = self.atributes[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.atributes[1] = self.atributes[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.atributes.pop()
        self.perc_down(1)
        return (retval, retatr)

    def build_heap(self, alist):
        index = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0]
        self.atributes = [0]
        for i in alist:
            self.heap_list.append(i[0])
            self.atributes.append(i[1])
        while index > 0:
            self.perc_down(index)
            index -= 1

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size == 0

    def decrease_key(self, element, new_key):
        idx = self.atributes.index(element)
        self.heap_list[idx] = new_key
        data = []
        for i in range(1, len(self.heap_list)):
            data.append((self.heap_list[i], self.atributes[i]))
        self.build_heap(data)

    def __str__(self):
        return str([(self.heap_list[i], self.atributes[i]) for i in range(1, self.current_size)])


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

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

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0
        self.time = 0

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

    def add_edge(self, f, t, cost=1):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_edges(self):
        edges = []
        for v in self:
            for w in v.get_connections():
                edges.append((v.get_id(), w.get_id()))
        return edges

    def get_vertices(self):
        return self.vert_list.keys()

    def generate_digraph(self):
        str = 'digraph G { '
        for v in self:
            for w in v.get_connections():
                new_vertex = '"%s" -> "%s"; ' % (v.get_id(), w.get_id())
                str += new_vertex
        str += '}'
        return str

    def get_cost(self, vert1, vert2):
        if self.vert_list[vert2] in self.vert_list[vert1].connected_to:
            return self.vert_list[vert1].connected_to[self.vert_list[vert2]]
        else:
            raise ValueError('Vertices are not connected!')

    def path_cost(self, vert_list):
        cost = 0
        if len(vert_list) > 1:
            for i in range(1, len(vert_list)):
                cost += self.get_cost(vert_list[i - 1], vert_list[i])
        return cost

    def bfs(self, start):
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

    def dijkstra(self, start):
        pq = BinHeap()
        start.set_distance(0)
        pq.build_heap([(v.get_distance(), v) for v in self])
        while not pq.is_empty():
            current_vert = pq.del_min()[1]
            for next_vert in current_vert.get_connections():
                new_dist = current_vert.get_distance() + current_vert.get_weight(next_vert)
                if new_dist < next_vert.get_distance():
                    next_vert.set_distance(new_dist)
                    next_vert.set_pred(current_vert)
                    pq.decrease_key(next_vert, new_dist)

    def traverse(self, vert):
        result = []
        x = vert
        while x.get_pred():
            result.append(x.get_id())
            x = x.get_pred()
        result.append(x.get_id())
        return result

    def find_fastest(self, start):
        self.dijkstra(self.get_vertex(start))
        routes = {k: None for k in self.vert_list.keys()}
        for i in list(self.vert_list.keys()):
            if i != start:
                result = self.traverse(self.get_vertex(i))
                result = tuple(result[::-1])
                cost = self.path_cost(result)
                if start in result:
                    routes[i] = (result, cost)
            else:
                routes[i] = ((i,), 0)

        for v in self:
            v.set_distance(sys.maxsize)
        return routes

    def dfs(self):
        for aVertex in self:
            aVertex.set_color('white')
            aVertex.set_pred(-1)
        for aVertex in self:
            if aVertex.get_color() == 'white':
                self.dfsvisit(aVertex)

    def sort_topological(self):
        is_linear = True
        times = [(i, self.vert_list[i].get_finish()) for i in self.vert_list.keys()]
        times.sort(reverse=True, key=lambda x: x[1])
        result = []
        for i in times:
            result.append(i[0])

        for i in range(1, len(result)):
            for j in result[:i]:
                if j in [p.id for p in list(self.vert_list[result[i]].connected_to)]:
                    is_linear = False

        if is_linear:
            return result
        else:
            raise ValueError('Graph is not linear!')

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

    def __iter__(self):
        return iter(self.vert_list.values())

    def __contains__(self, n):
        return n in self.vert_list


if __name__ == "__main__":
    g = Graph()
    # for i in range(6):
    #     g.add_vertex(i)
    #
    # g.add_edge(0, 1, 5)
    # g.add_edge(0, 5, 2)
    # g.add_edge(1, 2, 4)
    # g.add_edge(2, 3, 9)
    # g.add_edge(3, 4, 7)
    # g.add_edge(3, 5, 3)
    # g.add_edge(4, 0, 1)
    # g.add_edge(5, 4, 8)
    # g.add_edge(5, 2, 1)

    for i in range(9):
        g.add_vertex(i)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 6, 7)
    g.add_edge(4, 8, 7)
    g.add_edge(5, 6, 3)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 1)

    # print("Task 2")
    # print(g.generate_digraph())
    # print("Task 4")
    # g.dfs()
    # print(g.sort_topological())
    print("Task 5")
    print(g.find_fastest(3))
    print(g.find_fastest(1))
