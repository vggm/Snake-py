
from menu import Menu
from game import Game, end_game


if __name__ == '__main__':

  if Menu():

    snake_game = Game()
    start = True
    while start:
      
      if snake_game.start():
        start = False
      
      elif snake_game.game_over():
        start = False
        
  end_game()
