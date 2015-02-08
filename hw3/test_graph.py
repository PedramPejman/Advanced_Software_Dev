__author__ = 'pp5nv'
import unittest
from graph import Graph

class testGraph(unittest.TestCase):

    def setUp(self):
        self.g = Graph({'A':['B','D'],'B':['A'],'D':['A']})
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_is_adjacent_IA1(self):
        self.assertFalse(self.g.is_adjacent('A','Z'),"node2 not in graph")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_is_adjacent_IA2(self):
        self.assertFalse(self.g.is_adjacent('Y','B'),"node1 not in graph")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_is_adjacent_IA3(self):
        self.assertTrue(self.g.is_adjacent('A','B'),"nodes are adjacent")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_get_adjacent_GA1(self):
        self.assertEqual(self.g.get_adjlist('Z'),None,"node2 not in graph")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_get_adjacent_GA2(self):
        self.assertEqual(self.g.get_adjlist('A'),['B','D'],"node2 not in graph")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_link_nodes_LN1(self):
        self.assertFalse(self.g.link_nodes('A','B'),"Nodes are already adjacent")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_link_nodes_LN2(self):
        self.assertFalse(self.g.link_nodes('A', 'Z'), "Node2 is not in the graph")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_link_nodes_LN3(self):
        self.assertFalse(self.g.link_nodes('A','A'), "Node1 and Node2 are the same node")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_link_nodes_LN4(self):
        ret = self.g.link_nodes('B','D')
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A','D'],'D':['A','B']}), "graph was not modified the right way")
        self.assertTrue(ret, "Node1 and Node2 should be connected now" )

    def test_unlink_nodes_UN1(self):
        ret = self.g.unlink_nodes('A','D')
        self.assertTrue(ret, "should have returned True")
        self.assertEqual(str(self.g), str({'A':['B'],'B':['A'],'D':[]}), "Did not change graph as expected")

    def test_unlink_nodes_UN2(self):
        self.assertFalse(self.g.unlink_nodes('A','Z'), "One node not in graph")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_unlink_nodes_UN3(self):
        self.assertFalse(self.g.unlink_nodes('A','A'), "The 2 nodes are the same")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_unlink_nodes_UN4(self):
        self.assertFalse(self.g.unlink_nodes('B','D'), "The 2 nodes are not linked")
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_del_node_DN1(self):
        self.assertFalse(self.g.del_node('Z'),'Node not in graph')
        self.assertEqual(str(self.g),str({'A':['B','D'],'B':['A'],'D':['A']}),'Graph should not have been changed')

    def test_del_node_DN2(self):
        ret = self.g.del_node('B')
        self.assertTrue(ret, "Did not return true")
        self.assertEqual(str(self.g),str({'A':['D'],'D':['A']}))

    def test_add_node_AN1(self):
        ret = self.g.add_node('A')
        self.assertFalse(ret, "Should have returend false")
        self.assertEqual(str(self.g), str({'A':['B','D'],'B':['A'],'D':['A']}), "Graph should not have been changed")

    def test_add_node_AN2(self):
        ret = self.g.add_node('Z')
        self.assertTrue(ret, "Should have returend true")
        self.assertEqual(str(self.g), str({'A':['B','D'],'B':['A'],'D':['A'], 'Z':[]}), "Graph should not have been changed")

    def test_len_LN(self):
        self.assertEqual(len(self.g),3, "Length should be equal to 3")

    def test_num_nodes_NN(self):
        self.assertEqual(self.g.num_nodes(), 3, "Length should be equal to 3")

    def test_continas_CNT1(self):
        self.assertTrue('A' in self.g, "A is in the graph")

    def test_contains_CNT2(self):
        self.assertFalse('Z' in self.g, "Z is not in the graph")