from L7_ZAD1_5 import Graph


def game_over(location, missionaries, cannibals):
    if location[0] == 0:
        if ((location[1] == 0 and location[2] == 1) or location[1] != 0) and location[1] <= cannibals:
            return False
        else:
            return True
    elif location[0] == missionaries:
        return False
    else:
        if location[0] < location[1] or missionaries - location[0] < cannibals - location[1]:
            return True
        else:
            return False


def calculate_position(location, move):
    if location[2] == 0:
        return location[0] + move[0], location[1] + move[1], 1
    elif location[2] == 1:
        return location[0] + move[0], location[1] + move[1], 0
    else:
        raise ValueError


def move_legal(start, end):
    if start[2] == 0:
        if start[0] >= end[0] and start[1] >= end[1]:
            return True
        else:
            return False
    else:
        if start[0] <= end[0] and start[1] <= end[1]:
            return True
        else:
            return False


def create_graph(missionaries, cannibals):
    max_size = missionaries
    moves_list = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]
    g = Graph()
    for i in range(max_size + 1):
        for j in range(max_size + 1):
            for k in range(2):
                if not game_over((i, j, k), missionaries, cannibals) and i <= missionaries and j <= cannibals:
                    g.add_vertex((i, j, k))
    possible_vertex = list(g.vert_list.keys())[:-1]

    for vertex in possible_vertex:
        for moves in moves_list:
            if vertex[2] == 0:
                moves = (moves[0] * (-1), moves[1] * (-1))
            new_position = calculate_position(vertex, moves)
            if new_position in possible_vertex and move_legal(vertex, new_position):
                g.add_edge(vertex, new_position)
    return g


def get_path(graph, start, finish):
    fastest_ways = graph.find_fastest(start)
    if fastest_ways[finish] == None:
        return "Can not solve."
    else:
        return fastest_ways[finish]


def solve(missionaries, cannibals):
    if cannibals > missionaries:
        print("Missionaries were eaten.")
    else:
        graph = create_graph(missionaries, cannibals)
        print(get_path(graph, (missionaries, cannibals, 0), (0, 0, 1)))
        print(graph.generate_digraph())


if __name__ == "__main__":
    missionaries = 4
    cannibals = 3
    solve(missionaries, cannibals)
