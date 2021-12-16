def queen(square):
  """
  input:
  str square: the coordinate of the square that the queen is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the queen can move to:
  """
  
  return None


def main():
  myList = queen('f3')
  myList.sort()
  assert myList == ['a3', 'a8', 'b3', 'b7', 'c3', 'c6', 'd1', 'd3', 'd5', 'e2', 'e3', 'e4', 'f1', 'f2', 'f4', 'f5', 'f6', 'f7', 'f8', 'g2', 'g3', 'g4', 'h1', 'h3', 'h5']
  myList = queen('g7')
  myList.sort()
  assert myList == ['a1', 'a7', 'b2', 'b7', 'c3', 'c7', 'd4', 'd7', 'e5', 'e7', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g8', 'h6', 'h7', 'h8']

if __name__ == "__main__":
  main()
