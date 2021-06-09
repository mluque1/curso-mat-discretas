from graph import Grafo
from graph import Node
import random

def find_lowest_local_conection(actual_nodes, node):
    '''
    Find the lowest local conection between the node and their neighbour. 
    And ignores the conections between nodes in the actual tree.
    '''
    min_weight = float('inf')
    min_node = Node('')
    for key, value in node.neighbour.items():
        if(value < min_weight and key not in actual_nodes):
            min_weight = value
            min_node = key
    return min_node, min_weight

def find_lowest_conection(actual_nodes):
    '''
    Find in my actual tree the lowest conection in the nodes between the lowest local conection.
    '''
    min_weight = float('inf')
    min_act_node = Node('')
    min_new_node = Node('')
    for node in actual_nodes:
        n, w = find_lowest_local_conection(actual_nodes, node)
        if(w < min_weight):
            min_weight = w
            min_act_node = node
            min_new_node = n
    return min_act_node, min_new_node, min_weight
        

def prim(grafo):
    initial_node = random.choice(grafo.nodes)
    act_nodes = [initial_node]
    min_tree = []
    act_weight = 0
    print(initial_node)
    while(len(act_nodes) != len(grafo.nodes)):
        actual_node, new_node, min_weight = find_lowest_conection(actual_nodes=act_nodes)
        act_weight += min_weight
        min_tree.append(f'{actual_node.name} - {new_node.name}: {min_weight}')
        act_nodes.append(new_node)
    print(min_tree)
    print(act_weight)

def run():
    test = [[0, 4, 0, 6, 4, 0, 0, 0, 0],
            [4, 0, 3, 0, 7, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 5, 0, 0, 0],
            [6, 0, 0, 0, 5, 0, 8, 0, 0],
            [4, 7, 0, 5, 0, 2, 0, 2, 4],
            [0, 0, 5, 0, 2, 0, 0, 0, 1],
            [0, 0, 0, 8, 0, 0, 0, 6, 0],
            [0, 0, 0, 0, 2, 0, 6, 0, 5],
            [0, 0, 0, 0, 4, 1, 0, 5, 0]]
    grph = Grafo()
    grph.add_by_matriz(matriz=test)
    #grph.show_nodes()
    prim(grph)
    pass

if __name__ == '__main__':
    run()