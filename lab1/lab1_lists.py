
def maxmin(llist):
  if len(llist)==0 : return None
  min = llist[0]
  max = llist[0]
  for i in llist:
    if i < min: min = i
    if i > max: max = i
  return (max, min)

def commonItems(list1, list2):
  if ((len(list1)==0)or(len(list2)==0)): return None
  templist = []
  for i in list1:
    if (i in list2) and (i not in templist ) : templist.append(i)
  return templist


if __name__ == "__main__":
  list1 = ['Q','Z','A', 'D', 'D']
  list2 = ['B', 'QQ', 'C', 'iDD' ]
  print(maxmin(list1))
  print(commonItems(list1, list2))
