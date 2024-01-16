#!/usr/bin/env python

from collections import deque


def get_in_degree_dict(graph):
    in_degree_dict = {node: 0 for node in graph}
    for node in graph:
        for nbr in graph[node]:
            in_degree_dict[nbr] += 1
    return in_degree_dict


def kahn_topological_sort_wiki(graph):
    in_degree_dict = get_in_degree_dict(graph)
    no_in_degree_que = deque([v for v in in_degree_dict if in_degree_dict[v] == 0])
    top_sort = []

    while no_in_degree_que:
        node = no_in_degree_que.popleft()
        top_sort.append(node)
        for nbr in graph[node]:
            in_degree_dict[nbr] -= 1
            if in_degree_dict[nbr] == 0:
                no_in_degree_que.append(nbr)
        graph.pop(node)
        in_degree_dict.pop(node)
    if graph:
        return "A topological sort does not exist!"
    return top_sort


def get_small_graph():
    graph = dict()
    # graph["a"] = ["b", "c"]
    graph["a"] = ["c"]
    # graph["b"] = ["d"]
    graph["b"] = ["a", "d"]
    graph["c"] = ["b", "d"]
    graph["d"] = []
    return graph


def get_graph_w_cycle():
    graph = dict()
    graph["a"] = "b"
    graph["b"] = "c"
    graph["c"] = "a"
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
    # G = nx.DiGraph(graph)
    # nx.draw_networkx(G, edgecolors="k", node_color="w", arrows=True, arrowsize=20)
    # plt.savefig("topological_sort.png")
    return graph


if __name__ == "__main__":
    graph = get_graph()
    graph = get_graph_w_cycle()
    graph = get_small_graph()
    result = kahn_topological_sort_wiki(graph)
    print(f"result: {result}")
    # result =  ['0', '9', '13', '3', '2', '10', '1', '6', '7', '11', '4', '12', '5', '8']
    # graph = get_graph()
    # print(get_no_in_degree_set(graph, set()))
