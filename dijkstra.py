from graph import Grafo
from graph import Node
from graph import input_graph

class Dikjstra_Node(Node):
    def __init__(self, name):
        super().__init__(name)
        self.dij_weight = float('inf')
        self.dij_secuence= ''

def add_new_weights(node):
    for near_node, weight in node.neighbour.items():
        new_weight = node.dij_weight + weight
        if near_node.dij_weight > new_weight:
            near_node.dij_weight = new_weight
            near_node.dij_secuence = f'{node.dij_secuence} -> {near_node.name}'
    
def search_lightest(alones):
    lightest = Dikjstra_Node('')
    for node in alones:
        if(node.dij_weight < lightest.dij_weight):
            lightest = node
    return lightest

def dikjstra(grafo, node_name_1, node_name_2):
    if not grafo.have_node_by_name(node_name_1) or not grafo.have_node_by_name(node_name_2):
        print("Nodes name not valid.")
        return
    not_visited = []
    for node in grafo.nodes:
        not_visited.append(node)
    init_node = grafo.return_node_by_name(node_name_1)
    init_node.dij_weight = 0
    init_node.dij_secuence = node_name_1
    end_node = grafo.return_node_by_name(node_name_2)
    while(True):
        actual_node = search_lightest(not_visited)
        if actual_node == end_node:
            break
        add_new_weights(actual_node)
        not_visited.remove(actual_node)

    print(f'Route: {end_node.dij_secuence}')
    print(f'Final Weight: {end_node.dij_weight}')

def run():
    gph = Grafo()
    gph.add_by_line('a b 4', type_node=Dikjstra_Node)
    gph.add_by_line('a c 3', type_node=Dikjstra_Node)
    gph.add_by_line('a e 7', type_node=Dikjstra_Node)
    gph.add_by_line('b c 6', type_node=Dikjstra_Node)
    gph.add_by_line('b d 5', type_node=Dikjstra_Node)
    gph.add_by_line('c d 11', type_node=Dikjstra_Node)
    gph.add_by_line('c e 8', type_node=Dikjstra_Node)
    gph.add_by_line('d e 2', type_node=Dikjstra_Node)
    gph.add_by_line('d f 2', type_node=Dikjstra_Node)
    gph.add_by_line('d g 10', type_node=Dikjstra_Node)
    gph.add_by_line('e g 5', type_node=Dikjstra_Node)
    gph.add_by_line('f g 3', type_node=Dikjstra_Node)
    dikjstra(gph, 'a', 'f')

if __name__ == '__main__':
    #run()
    g = Grafo()
    input_graph(g, type_node=Dikjstra_Node)
    dikjstra(g, 'a', 'e')