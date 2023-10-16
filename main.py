
from menu import Menu
from game import Game, end_game


if __name__ == '__main__':

  ''' Return True if the player wants to start the game '''
  if Menu():

    snake_game = Game()
    start = True
    while start:
      
      if snake_game.start(): # if return False, player wants to end the game
        start = False
      
      elif snake_game.game_over(): # if return False, player wants to end the game
        start = False
        
  end_game()
