
from game import Game


if __name__ == '__main__':
  # menu() todo
  snake_game = Game()
  start = True
  while start:
    
    if snake_game.start():
      start = False
    
    elif snake_game.game_over():
      start = False
      
  snake_game.end()
