#!python3

def rook(square):
  """
  input:
  str square: the coordinate of the square that the rook is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the rook can move to:
  """
  
  return None


def main():
  myList = rook('f3')
  myList.sort()
  assert myList == ['a3', 'b3', 'c3', 'd3', 'e3', 'f1', 'f2', 'f4', 'f5', 'f6', 'f7', 'f8', 'g3', 'h3']
  myList = rook('g7')
  myList.sort()
  assert myList == ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g8', 'h7']

if __name__ == "__main__":
  main()
