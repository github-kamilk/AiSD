from L7_ZAD1_5 import Graph


def build_graph(bucket1, bucket2):
    g = Graph()
    for i in range(bucket1 + 1):
        for j in range(bucket2 + 1):
            g.add_vertex((i, j))

    for vertex in list(g.vert_list.keys()):
        if vertex[0] == 0:
            g.add_edge(vertex, (bucket1, vertex[1]))
            if vertex[1] <= bucket1:
                g.add_edge(vertex, (vertex[1], 0))
            else:
                g.add_edge(vertex, (bucket1, vertex[1] - bucket1))
        else:
            g.add_edge(vertex, (0, vertex[1]))
            g.add_edge(vertex, (bucket1, vertex[1]))
            if vertex[0] + vertex[1] <= bucket2:
                g.add_edge(vertex, (0, vertex[0] + vertex[1]))
            else:
                g.add_edge(vertex, (vertex[0] + vertex[1] - bucket2, bucket2))
            if vertex[0] + vertex[1] <= bucket1:
                g.add_edge(vertex, (vertex[0] + vertex[1], 0))
            else:
                g.add_edge(vertex, (bucket1, vertex[1] + vertex[0] - bucket1))
        if vertex[1] == 0:
            g.add_edge(vertex, (vertex[0], bucket2))
            g.add_edge(vertex, (0, vertex[0]))
        else:
            g.add_edge(vertex, (vertex[0], 0))
            g.add_edge(vertex, (vertex[0], bucket2))
            if vertex[0] + vertex[1] <= bucket2:
                g.add_edge(vertex, (0, vertex[0] + vertex[1]))
            else:
                g.add_edge(vertex, (vertex[0] + vertex[1] - bucket2, bucket2))
            if vertex[0] + vertex[1] <= bucket1:
                g.add_edge(vertex, (vertex[0] + vertex[1], 0))
            else:
                g.add_edge(vertex, (bucket1, vertex[1] + vertex[0] - bucket1))
    return g


def get_path(graph, start, finish):
    fastest_ways = graph.find_fastest(start)
    if finish in graph:
        if fastest_ways[finish] is None:
            return None
        else:
            return fastest_ways[finish]


def solve(x, y, goal):
    bucket1 = min(x, y)
    bucket2 = max(x, y)

    if bucket2 < goal:
        return print("Can not solve.")

    graph = build_graph(bucket1, bucket2)
    paths = []
    for i in range(bucket2 + 1):
        paths.append(get_path(graph, (0, 0), (i, goal)))
        paths.append(get_path(graph, (0, 0), (goal, i)))
    paths = [i for i in paths if i is not None]

    if not paths:
        return print("Can not solve.")

    minimum = paths[0][1]
    for i in range(len(paths)):
        if paths[i][1] < minimum:
            minimum = paths[i][1]
            minimum_pos = i
    print(paths[minimum_pos])
    print(graph.generate_digraph())


if __name__ == "__main__":
    bucket1 = 3
    bucket2 = 3
    goal = 1
    solve(bucket1, bucket2, goal)
