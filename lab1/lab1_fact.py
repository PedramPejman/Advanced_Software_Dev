
def factorial1 (n):
  if n<0: 
    raise ValueError("cannot be negative")
  count = 1
  for i in range(1,n+1):
    count *= i
  return count

def factorial2 (n):
  if n<0: 
    raise ValueError("cannot be negative")
  count = 1
  fact_list = [1]
  for i in range(1,n+1):
    count *= i
    fact_list.append(count)
  return fact_list

def test_fact1():
  assert factorial1(0) == 1
  assert factorial1(1) == 1
  assert factorial1(5) == 120
  assert factorial2(0) == [1] 
  assert factorial2(1) == [1, 1]
  assert factorial2(5) == [1, 1, 2, 6, 24, 120]
  try:
    factorial1(-10)
    assert False
  except ValueError:
    assert True
  
  try:
    factorial2(-10)
    assert False
  except ValueError:
    assert True


if __name__ == "__main__":
  test_fact1()
