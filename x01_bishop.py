#!python3

def bishop(square):
  """
  input:
  str square: the coordinate of the square that the bishop is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the bishop can move to:
  """
  
  return None


def main():
  myList = bishop('f3')
  myList.sort()
  assert myList == ['a8', 'b7', 'c6', 'd1', 'd5', 'e2', 'e4', 'g2', 'g4', 'h1', 'h5']
  myList = bishop('g7')
  myList.sort()
  assert myList = ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'f8', 'h6', 'h8']

if __name__ == "__main__":
  main()
