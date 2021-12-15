#!python3

def knight(square):
  """
  input:
  str square: the coordinate of the square that the knight is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the knight can move to:
  """
  
  return None


def main():
  myList = knight('g7')
  myList.sort()
  assert myList == ['e6', 'e8', 'f5', 'h5']
  myList = knight('d4')
  myList.sort()
  assert myList = ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']

if __name__ == "__main__":
  main()
