from hw2_set import OurSet
__author__ = 'Pedram'

def test_add_element_notin():
    set = OurSet()
    set.addList([1])
    set.add(2)
    assert str(set) == "<1, 2>"

def test_add_element_in():
    set = OurSet()
    set.addList([1, 2])
    assert False == set.add(2)

def test_add_list():
    set1 = OurSet()
    set1.addList([2,3])
    ret = set1.addList([1,2,3,5])
    assert (ret == True) and (str(set1) == "<2, 3, 1, 5>")

def test_add_list_empty():
    set1 = OurSet()
    set1.addList([2,3])
    ret = set1.addList([])
    assert (ret == False) and (str(set1) == "<2, 3>")

def test_len():
    set1 = OurSet()
    set1.addList([1,2,3])
    assert len(set1) == 3

def test_len_empty():
    set1 = OurSet()
    assert len(set1) == 0





