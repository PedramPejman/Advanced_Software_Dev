class OurSet:
  """
  An implementation of a class representing a logical Set
  Including methods to add individual items and entire lists. 
  It is iterable (the underlying list is the object iterated).
  """
  
  def __init__(self):
    """Initializes an instance of OurSet."""
    self.list = []
  
  def add(self, item):
    """Adds item to self if it is not already in self."""
    if (item in self.list): return False
    self.list.append(item)

  def addList(self, list):
    """Adds all items in list to self. If any items were added, return True"""
    flag = False
    for i in list:
      if (i not in self.list):
        flag = True
        self.add(i)
    return flag

  def __str__(self):
    """Returns set in the form <el_1, el_2...el_n> """
    if (len(self.list)==0): return "<>"
    str = "<"
    for i in self.list:
      str = (str+"{0}").format(i) + ", "
    str = str[:-2] +  ">"
    return str

  def __len__(self):
    """Returns the number of elements in the set"""
    return len(self.list)

  def __iter__(self):
    """Returns an interator to the list"""
    return iter(self.list)

  def union(self, set2):
    """Returns an OurSet object that contains the union of the self and set2."""
    union = OurSet()
    for i in self:
      if (i not in union): union.add(i)
    for i in set2:
      if (i not in union): union.add(i)
    return union

  def intersection(self, set2):
    """Returns an OurSet object that contains the intersection of the self and set2."""
    intersect = OurSet()
    for i in self:
      if ((i in set2) and (i not in intersect)): intersect.add(i)
    return intersect

def main():
  s = OurSet()
  print(s)
  print(len(s))
  s.add("A")
  s.add("B")
  print(s)
  print(len(s))
  list1 = ["C", "D"]
  s.addList(list1)
  print(s)
  s2 = OurSet()
  s2.add("D")
  s2.add("C")
  s2.add("E")
  print(s2)
  print(s.union(s2))
  print(s.intersection(s2))
if __name__ == "__main__": main()
