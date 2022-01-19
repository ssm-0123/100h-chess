#!python3

def makecoord():
  a = ['a','b','c','d','e','f','g','h']
  coord = []
  for i in range(1,9):
    templist = []
    for aa in a:
      templist.append(aa+str(i))
    coord.append(templist)
  return coord



def rook(square):
  """
  input:
  str square: the coordinate of the square that the rook is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the rook can move to:
  """
  coord = makecoord()
  for a in coord:
    for b in a:
      if b == square :
        ver = coord.index(a)
        hor = a.index(b)

  answer = []
  for i in range(0,8):
    answer.append(coord[ver][i])
    answer.append(coord[i][hor])
  answer.remove(square)
  answer.remove(square)
  answer.sort()
  return answer

def main():
  myList = rook('f3')
  myList.sort()
  assert myList == ['a3', 'b3', 'c3', 'd3', 'e3', 'f1', 'f2', 'f4', 'f5', 'f6', 'f7', 'f8', 'g3', 'h3']
  myList = rook('g7')
  myList.sort()
  assert myList == ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g8', 'h7']

if __name__ == "__main__":
  main()
