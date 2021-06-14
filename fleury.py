from graph import Grafo
from graph import Node
from graph import input_graph
import random

class NodeFleury(Node):
    def __init__(self, name):
        super().__init__(name)
        self.free_edges = []
    
    def add_edge(self, edge):
        self.free_edges.append(edge)

    def remove_edge(self, edge):
        if edge in self.free_edges:
            self.free_edges.remove(edge)

    def total_edges(self):
        return len(self.free_edges)

class Cicle:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        st = '[ '
        for node in self.nodes:
            st = f'{st} {node.name},'
        st = f'{st[:-1]} ]'
        return st


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def remove_edge_node(self):
        self.node1.remove_edge(self)
        self.node2.remove_edge(self)

    def __str__(self):
        return f'{self.node1.name} <-> {self.node2.name}'


class GrafoFleury(Grafo):
    def __init__(self):
        super().__init__()
        self.edges = []

    def same_node(self, node1, node2):
        return node1 == node2

    def connect_same_node(self, node, weight):
        node.add_neighbour(node, weight)
        node.degree += 1

    def connect_nodes(self, node1, node2, weight = 0):
        temp_edge = Edge(node1, node2, weight)
        self.edges.append(temp_edge)
        if self.same_node(node1, node2):
            self.connect_same_node(node1, weight)
        else:
            node1.add_neighbour(node2, weight)
            node2.add_neighbour(node1, weight)
            node1.add_edge(temp_edge)
        
        node2.add_edge(temp_edge)

def get_inital_node(graph):
    nodes_clone = graph.nodes[:]
    random.shuffle(nodes_clone)
    for node in nodes_clone:
        if node.total_edges() != 0:
            return node
    return

def next_node(edge, node1):
    if edge.node1 == node1:
        return edge.node2
    return edge.node1

def get_random_edge(node):
    try:
        random.shuffle(node.free_edges)
        return node.free_edges.pop()
    except:
        return

def round(node):
    cicle = Cicle()
    while True:
        rnd_edge = get_random_edge(node)
        if not rnd_edge:
            cicle.add_node(node)
            return cicle
        cicle.add_node(node)
        node = next_node(rnd_edge, node)
        rnd_edge.remove_edge_node()

def can_cicle(graph):
    for node in graph.nodes:
        if (node.degree % 2) != 0:
            return False
    return True

def fleury(graph):
    if not can_cicle(graph):
        print("This graph cant support an euclidean cicle.")
        return
    cicles = []
    while True:
        initial_node = get_inital_node(graph)
        if not initial_node:
            break
        cicles.append(round(initial_node))
    for cicle in cicles:
        print(cicle)

def run():
    gp = GrafoFleury()
    input_graph(gp, NodeFleury)
    gp.show_nodes()
    print()
    fleury(gp)
    pass

if __name__ == '__main__':
    run()