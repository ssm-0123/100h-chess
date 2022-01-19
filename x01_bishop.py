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


def bishop(square):
  """
  input:
  str square: the coordinate of the square that the bishop is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the bishop can move to:
  """
  coord = makecoord()
  for a in coord:
    for b in a:
      if b == square :
        ver = coord.index(a)
        hor = a.index(b)

  answer = []
  vera = ver
  hora = hor
  while True:
    ver = ver+1
    hor = hor+1
    if ver >= 8 or hor >= 8:
      break
    answer.append(coord[ver][hor])
  while True:
    ver = ver-1
    hor = hor-1
    if ver <= -1  or hor <= -1:
      break
    if coord[ver][hor] not in answer:
      answer.append(coord[ver][hor])
  
  while True:
    vera = vera+1
    hora = hora-1
    if vera >= 8 or hora <= -1:
      break
    if coord[vera][hora] not in answer:
      answer.append(coord[vera][hora])
  while True:
    vera = vera-1
    hora = hora+1
    if vera <= -1 or hora >= 8:
      break
    if coord[vera][hora] not in answer:
      answer.append(coord[vera][hora])
  answer.remove(square)
  answer.sort()
  print(answer)

bishop("f3")




"""
def main():
  myList = bishop('f3')
  myList.sort()
  assert myList == ['a8', 'b7', 'c6', 'd1', 'd5', 'e2', 'e4', 'g2', 'g4', 'h1', 'h5']
  myList = bishop('g7')
  myList.sort()
  assert myList = ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'f8', 'h6', 'h8']

if __name__ == "__main__":
  main()
"""