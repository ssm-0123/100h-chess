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

def knight(square):
  """
  input:
  str square: the coordinate of the square that the knight is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the knight can move to:
  """
  coord = makecoord()
  for a in coord:
    for b in a:
      if b == square :
        ver = coord.index(a)
        hor = a.index(b)

  answer = []
  if ver + 2 <= 7 and hor - 1 >= 0:
    answer.append(coord[ver+2][hor-1])
  if ver + 2 <= 7 and hor + 1 <= 7:
    answer.append(coord[ver+2][hor+1])

  if ver - 2 >= 0 and hor - 1 >= 0:
    answer.append(coord[ver-2][hor-1])
  if ver - 2 >= 0 and hor + 1 <= 7:
    answer.append(coord[ver-2][hor+1])

  if ver + 1 >= 7 and hor + 2 <= 7:
    answer.append(coord[ver+1][hor+2])
  if ver - 1 <= 0 and hor + 2 <= 7:
    answer.append(coord[ver-1][hor+2])

  if ver + 1 >= 7 and hor - 2 >= 0:
    answer.append(coord[ver+1][hor-2])
  if ver - 1 >= 0 and hor - 2 >= 0:
    answer.append(coord[ver-1][hor-2])
  
  answer.sort()
  return answer

print(knight('g7'))


"""
def main():
  myList = knight('g7')
  myList.sort()
  assert myList == ['e6', 'e8', 'f5', 'h5']
  myList = knight('d4')
  myList.sort()
  assert myList = ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']

if __name__ == "__main__":
  main()
"""