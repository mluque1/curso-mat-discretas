from graph import Grafo
from graph import Node
from graph import input_graph
import copy

class KrukalNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.act_tree = []

class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __str__(self):
        return f'{self.node1.name} <-> {self.node2.name}: {self.weight}'

def get_weight(edge_list):
    return sum([edge.weight for edge in edge_list])

def mark_nodes(edge):
    node1 = edge.node1
    node2 = edge.node2
    kru_tree_node1 = node1.act_tree
    kru_tree_node2 = node2.act_tree

    final_list = [node1] + [node2] + kru_tree_node1 + kru_tree_node2

    for final_node in final_list:
        new_list = []
        for nodes in final_list:
            if nodes != final_node:
                new_list.append(nodes)
        final_node.act_tree = new_list


def form_cicle(edge):
    internal_tree_list = edge.node1.act_tree
    proof_node = edge.node2
    return proof_node in internal_tree_list
    

def search_lightest_edge(edge_ls):
    lightest_edge = Edge(KrukalNode('8'), KrukalNode('7'), float('inf'))
    for actual_edge in edge_ls:
        if actual_edge.weight < lightest_edge.weight:
            lightest_edge = actual_edge
    return lightest_edge

def in_list(edge_ls, node1, node2, weight):
    for edge in edge_ls:
        if edge.node1 == node1 and edge.node2 == node2 and edge.weight == weight:
            return True
        if edge.node1 == node2 and edge.node2 == node1 and edge.weight == weight:
            return True
    return False

def get_edge_list(gph):
    edge_list = []
    for node in gph.nodes:
        for neigh, weight in node.neighbour.items():
            if not in_list(edge_list, node, neigh, weight):
                temp_edge = Edge(node, neigh, weight)
                edge_list.append(temp_edge)
    return edge_list

def kruskal(gph):
    edge_list = get_edge_list(gph)
    kruskal_list = []
    while len(kruskal_list) != (len(gph.nodes) - 1):
        lightest_edge = search_lightest_edge(edge_list)
        edge_list.remove(lightest_edge)
        if not form_cicle(lightest_edge):
            kruskal_list.append(lightest_edge)
            mark_nodes(lightest_edge)
    s = '['
    for kl in kruskal_list:
        s = f'{s} {kl},'
    s = f'{s[:-1]} ]'
    print(s)
    print(get_weight(kruskal_list))

def run():
    g = Grafo()
    input_graph(g, type_node=KrukalNode)
    kruskal(g)

if __name__ == '__main__':
    run()