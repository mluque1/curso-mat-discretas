import collections
import re

class Node:

    def __init__(self, name):
        self.name = name
        self.neighbour = {}
        self.degree = 0
    
    def add_neighbour(self, node, weight):
        self.neighbour[node] = weight
        self.degree += 1

    def __str__(self):
        nb_names = '['
        for key, value in self.neighbour.items():
            nb_names = nb_names + f' {key.name}: {value},'
        nb_names = nb_names[:-1] + ' ]'
        if(len(self.neighbour) == 0):
            nb_names = '[ ]'
        return f'Node {self.name}. Degree: {self.degree}. Neighbours({len(self.neighbour)}): {nb_names}'

class Grafo:
    def __init__(self):
        self.nodes = []
    
    def add_by_matriz(self, matriz, node_names = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')):
        #Check Real Matriz
        if(not self.is_matriz(matriz)):
            print("Not a value Matriz")
            return
        node_number = len(matriz)
        for i in range(node_number):
            self.new_node(node_names[i])

        for i in range(node_number):
            for j in range(node_number):
                weight = matriz[i][j]
                if(i < j and weight != 0): #Ignores the half of the matriz, the diagonal and the numbers with no weight.
                    row_node = self.nodes[i]
                    column_node = self.nodes[j]
                    self.connect_nodes(row_node, column_node, weight)
                if(i == j and weight != 0):                    
                    node = self.nodes(i)
                    node.add_neighbour(node, weight)
                    node.degree += 1

    def add_by_text(self, text):
        '''
        Use multiple lines with the format:\n
        {Node_Name_A}<space>{Node_Name_B}<space>{Weigth}.\n
        Separeted by an enter \"\\n\"
        '''
        try:
            split_text = text.split('\n')
            for line in split_text:
                self.add_by_line(line)
        except:
            print(f"Something worng with the text: {text}")

    def add_by_line(self, line):
        '''
        Actual format string:\n
        {Node_Name_A}<space>{Node_Name_B}<space>{Weigth}\n
        DON'T repeat the names in the format. Take the name as
        unique id.
        '''
        try:
            split_command = line.split(' ')
            name_node_1 = split_command[0]
            name_node_2 = split_command[1]
            weight = int(split_command[2])
            #Get or Create the nodes
            if(self.have_node_by_name(name_node_1)):
                node1 = self.return_node_by_name(name_node_1)
            else:
                node1 = Node(name_node_1)
                self.nodes.append(node1)
            if(self.have_node_by_name(name_node_2)):
                node2 = self.return_node_by_name(name_node_2)
            else:
                node2 = Node(name_node_2)
                self.nodes.append(node2)
            
            #Connect nodes
            self.connect_nodes(node1, node2, weight)
        except:
            print(f"Something worng with the command: {line}")

    def connect_nodes(self, node1, node2, weight = 0):
        node1.add_neighbour(node2, weight)
        node2.add_neighbour(node1, weight)

    def add_node(self, new_node):
        self.nodes.append(new_node)

    def new_node(self, name):
        temp_node = Node(name)
        self.nodes.append(temp_node)

    def have_node_by_name(self, name_search):
        node_names = [x.name for x in self.nodes]
        return name_search in node_names

    def return_node_by_name(self, name_search):
        for index, value in enumerate(self.nodes):
            if(value.name == name_search):
                return self.nodes[index]

    def show_nodes(self):
        for nodes in self.nodes:
            print(nodes)

    def is_matriz(self, matriz):
        try:
            lenghts_row_counter = dict(collections.Counter([len(row) for row in matriz]))
            if len(lenghts_row_counter) != 1 or len(matriz) != len(matriz[0]):
                print("Not a good rows")
                return False
            return True
        except:
            return False

def input_graph(grafo):
    option = '-'
    print('Command format:')
    print('{Node_Name_A}<space>{Node_Name_B}<space>{Weigth}')
    while True:
        option = input('Insert command (Press Enter to finish): ')
        if option == '':
            break
        grafo.add_by_line(option)





def run():
    test = [[0, 4, 0, 6, 4, 0, 0, 0, 0],
            [4, 0, 3, 0, 7, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 5, 0, 0, 0],
            [6, 0, 0, 0, 5, 0, 8, 0, 0],
            [4, 7, 0, 5, 0, 2, 0, 2, 4],
            [0, 0, 5, 0, 2, 0, 0, 0, 4],
            [0, 0, 0, 8, 0, 0, 0, 6, 0],
            [0, 0, 0, 0, 2, 0, 6, 0, 5],
            [0, 0, 0, 0, 4, 4, 0, 5, 0]]
    grp = Grafo() 
    grp.add_by_matriz(matriz=test)
    grp.show_nodes()

if __name__ == '__main__':
    if True:
        grp = Grafo()
        grp.add_by_line('a b 1')
        grp.add_by_line('a c 7')
        grp.add_by_line('a d 5')
        grp.add_by_line('a e 2')
        grp.show_nodes()
    else:
        grp2 = Grafo()
        input_graph(grp2)
        grp2.show_nodes()
    #run()