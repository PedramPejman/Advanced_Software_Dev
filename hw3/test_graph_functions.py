__author__ = 'Pedram'
import nose
from graph import Graph
from graph_functions import *

def test_complete_C1():
    g = Graph({'A':['B','D'],'B':['A'],'D':['A']})
    assert is_complete(g) == False

def test_complete_C2():
    g = Graph({'A':['B','D'],'B':['A','D'],'D':['A','B']})
    assert is_complete(g) == True

def test_complete_C3():
    g = Graph({'A':['B'],'B':['A']})
    assert is_complete(g) == True

def test_complete_C4():
    g = Graph({})
    assert is_complete(g) == True

def test_complete_C5():
    g = Graph({'A':[]})
    assert is_complete(g) == True

def test_complete_C6():
    g = []
    try:
        a = is_complete(g)
        assert False
    except TypeError:
        assert True


def test_degree_ND1():
    g = Graph({'A':[],'B':['D'],'D':['B']})
    ret = nodes_by_degree(g)
    assert str(ret) == str([('D',1), ('B',1), ('A',0)]) or str(ret) == str([('B',1), ('D',1), ('A',0)])

def test_degree_ND2():
    g = Graph({})
    ret = nodes_by_degree(g)
    assert str(ret) == str([])

def test_degree_ND3():
    g = Graph({'A':[]})
    ret = nodes_by_degree(g)
    assert str(ret) == str([('A',0)])

def test_degree_ND4():
    g = Graph({'A':['B','D'],'B':['A','D'],'D':['A','B']})
    ret = nodes_by_degree(g)
    lsit = [('A',2),('B',2),('D',2)]
    assert len(ret) == 3
    for item in lsit:
        assert item in ret

def test_degree_ND5():
    g = []
    try:
        a = nodes_by_degree(g)
        assert False
    except TypeError:
        assert True