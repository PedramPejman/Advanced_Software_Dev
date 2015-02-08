__author__ = 'pp5nv'


def main():
    g =  Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } )
    print(g)

class Graph:
    dictionary = {}
    def __init__(self, dict={}):
        self.dictionary = dict
    def __str__(self):
        return str(self.dictionary)
    def __contains__(self, item):
        return item in self.dictionary.keys()
    def __iter__(self):
        return iter(self.dictionary)
    def num_nodes(self):
        return len(self.dictionary)
    def __len__(self):
        return self.num_nodes()
    def get_adjlist(self, item):
        if item not in self.dictionary: return None
        return self.dictionary[item]
    def is_adjacent(self, item1, item2):
        if item1 not in self.dictionary.keys(): return False
        return item2 in self.dictionary[item1]
    def add_node(self, node):
        if node in self.dictionary.keys(): return False
        self.dictionary[node] = []
        return True
    def link_nodes(self, node1, node2):
        if node1 == node2: return False
        if node1 not in self.dictionary or node2 not in self.dictionary: return False
        if node2 in self.dictionary[node1]: return False
        self.dictionary[node1].append(node2)
        self.dictionary[node2].append(node1)
        return True
    def unlink_nodes(self, node1, node2):
        if node1 == node2: return False
        if node1 not in self.dictionary or node2 not in self.dictionary: return False
        if node2 not in self.dictionary[node1]: return False
        self.dictionary[node1].remove(node2)
        self.dictionary[node2].remove(node1)
        return True
    def del_node(self, node):
        if node not in self.dictionary: return False
        for item in self.dictionary[node]:
            self.dictionary[item].remove(node)
        self.dictionary.pop(node, None)
        return True



if __name__ == "__main__": main()