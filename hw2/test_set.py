from hw2_set import *

if __name__=='__main__':
  s = OurSet()
  s.addList([1,3,6,9,4,4,8,2])
  print(s)
  s2 = OurSet()
  s2.addList([1,5,7,4])
  print(s.union(s2))
  print(s.intersection(s2))
  print(s)

