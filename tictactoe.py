
import random, os

# parameters
dim = 2
numPlayers = 2
board = []
checkers=['X','O']
players=["John","Doe"]
turn=0
win = False
positions = dim**2

# functions
def printBoard():
  os.system("clear")
  print("  ",end="")
  for i in range(dim):
    print(i, end= " ")
  print()
  for r in range(dim):
    print(r, end = " ")
    for c in range(dim):
      print(board[r][c], end= " ")
    print()

def checkWin():
  # check horizontal win
  if board[chosenR].count(checkers[turn]) == dim:
    printBoard()
    print(players[turn],"congratulations")
    return True
  
  # check vertical win
  cnt = 0
  for i in range(dim):
    if board[i][chosenC]==checkers[turn]:
      cnt+=1
  if cnt == dim:
    printBoard()
    print(players[turn],"congratulations")
    return True
  
  # check diagonal I win
  cnt = 0
  for i in range(dim):
    if board[i][i]==checkers[turn]:
      cnt+=1
  if cnt == dim:
    printBoard()
    print(players[turn],"congratulations")
    return True
  
  # check diagonal II win
  cnt = 0
  for i in range(dim):
    if board[i][dim-1-i]==checkers[turn]:
      cnt+=1
  if cnt == dim:
    printBoard()
    print(players[turn],"congratulations")
    return True
  
  return False
  
# create the board
for r in range(dim):
  tmp = []
  for c in range(dim):
    tmp.append(".")
  board.append(tmp)
  
while win == False and positions > 0: # fixme: need to figure out the condition
  printBoard()
  choice = input(players[turn]+", please enter a row,col: ").split(",")
  chosenR = int(choice[0])
  chosenC = int(choice[1])
  if board[chosenR][chosenC] == '.':
    board[chosenR][chosenC]=checkers[turn]
    positions-=1
    win = checkWin()
  turn = (turn+1)%numPlayers  #to alternate between 0 and 1

if positions == 0 and win == False:
  printBoard()
  print ("It's a draw !!!!")
  
  
  
