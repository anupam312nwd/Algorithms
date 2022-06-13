#!/usr/bin/env python


def get_in_coming_degree(graph):
    in_coming_degree = {node: 0 for node in graph}
    for node in graph:
        for nbr in graph[node]:
            in_coming_degree[nbr] += 1
    return in_coming_degree


def remove_node_from_graph(graph, node, in_coming_degree):
    for nbr in graph[node]:
        in_coming_degree[nbr] -= 1
    graph.pop(node)


def get_no_in_degree_set(in_coming_degree):
    return set([node for node in in_coming_degree if in_coming_degree[node] == 0])


def kahn_topological_sort():
    """
    time-complexity: O(V+E)
    """
    graph = get_graph()
    topological_order = []
    in_coming_degree = get_in_coming_degree(graph)
    no_in_degree_set = get_no_in_degree_set(in_coming_degree)
    while no_in_degree_set:
        for node in no_in_degree_set:
            in_coming_degree.pop(node)  # --------------------------------- O(1)
            topological_order.append(node)  # ----------------------------- O(1)
            remove_node_from_graph(graph, node, in_coming_degree)  # ------ O(nbrs)
            no_in_degree_set = get_no_in_degree_set(in_coming_degree)  # -- O(V)
    if not no_in_degree_set and graph:
        return "A topological sort does not exist!"
    return topological_order


def get_small_graph():
    graph = dict()
    # graph["a"] = ["b", "c"]
    graph["a"] = ["c"]
    # graph["b"] = ["d"]
    graph["b"] = ["a", "d"]
    graph["c"] = ["b", "d"]
    graph["d"] = []
    return graph


def get_graph():
    graph = dict()
    graph["0"] = ["2", "6", "3"]
    graph["1"] = ["4"]
    graph["2"] = ["6"]
    graph["3"] = ["1", "4"]
    graph["4"] = ["5", "8"]
    graph["5"] = []
    graph["6"] = ["7", "11"]
    graph["7"] = ["4", "12"]
    graph["8"] = []
    graph["9"] = ["2", "10"]
    graph["10"] = ["6"]
    graph["11"] = ["12"]
    graph["12"] = ["8"]
    graph["13"] = []
    return graph


if __name__ == "__main__":
    result = kahn_topological_sort()
    print(result)
    # graph = get_graph()
    # print(get_no_in_degree_set(graph, set()))
