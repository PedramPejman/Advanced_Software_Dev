
def main():
  """Function testing functions in this file."""
  list1 = [2, 3, 5]
  list2 = [3, 10, 10, 5]  
  list3 = [1, 3, 2, 2, 3, 1, 1, 2]
  print(common_items(list1, list2))
  print(notcommon_items(list1, list2))
  print(count_list_items(list3))

def maxmin(llist):
  """function returning a tuple of the form (max, min)"""
  if len(llist)==0 : return None
  min = llist[0]
  max = llist[0]
  for i in llist:
    if i < min: min = i
    if i > max: max = i
  return (max, min)

def common_items(list1, list2):
  """Function returning a list of common items in 2 lists"""
  if ((len(list1)==0)or(len(list2)==0)): return None
  templist = []
  for i in list1:
    if (i in list2) and (i not in templist ) : templist.append(i)
  return templist

def notcommon_items(list1, list2):
  """Function returning a list of elements in one list but not the other list."""
  if (len(list1)==0): return list2
  if (len(list2)==0): return list1
  templist = []
  for i in list1:
    if (i not in list2) and (i not in templist) : templist.append(i)
  for i in list2:
    if (i not in list1) and (i not in templist) : templist.append(i)
  return templist

def count_list_items(llist):
  """Returns the number of items in the list."""
  if (len(llist) == 0): return {}
  dict = {}
  for i in llist:
    if i in dict: dict[i] = dict[i]+1
    else: dict[i] = 1
  return dict



if __name__ == "__main__" : main();
