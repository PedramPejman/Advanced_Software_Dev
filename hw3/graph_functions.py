__author__ = 'Pedram'
from graph import Graph

def is_complete(graph):
    if not isinstance(graph, Graph): raise TypeError("argument should be of type Graph")
    if len(graph) == 0 or len(graph) == 1: return True
    length = len(graph)
    for node in graph:
        if len(graph.get_adjlist(node)) != length-1: return False
    return True

def nodes_by_degree(graph):
    if not isinstance(graph, Graph): raise TypeError("argument should be of type Graph")
    ret = []
    for node in graph:
        ret.append((node, len(graph.get_adjlist(node))))
    ret = sorted(ret, key=lambda tup:tup[1], reverse=True)
    return ret

def main():
    g = Graph({'A':['B','D'],'B':['A', 'D'],'D':['A', ]})
    g = Graph({'A':[]})
    print(is_complete(g))
    print(nodes_by_degree(g))
if __name__ == "__main__": main()


