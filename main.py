import random
print('Tictactoe')
def game() :
  answer = input('1 player or 2 (type 1 or 2)\n')
  if answer == str(1):
    possiblespaces=['top left','top middle','top right','middle right', 'center', 'middle left','bottom']
    print('it works')
  elif answer == str(2):
    print('hello')
  else:
    print('pick one or two please')
    game()
game()