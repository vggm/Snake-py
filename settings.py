'''
  Game Settings
'''

from game_features import *

class Settings():
  def __init__(self) -> None:
    # GAME OPTIONS
    self.max_food = 5
    self.aleatory_num_food = True

    # if true, when the snake head hit the wall its game over
    # otherwise, the snake head will tp to the other side of the wall
    self.solid_wall = False 
    
    # SCORE
    self.SCORE_ADDITION = 1  
    
    # SCORE MENU
    self.score_height = 80
    self.score_width = 640
    self.SCORE_SIZE = (self.score_width, self.score_height)
    self.SCORE_POSITION = (0,0)
    self.SCORE_BACKGROUND_COLOR = BLACK
    
    # SCREEN
    self.screen_width = 640
    self.screen_height = 640 + self.score_height
    self.SCREEN_SIZE = (self.score_width, self.score_height)
    
    # CELLS
    self.CELLS_PER_ROW = 16
    self.CELL_HEIGHT = (self.screen_height - self.score_height) // self.CELLS_PER_ROW
    self.CELL_WIDTH = self.screen_width // self.CELLS_PER_ROW
    self.CELL_SIZE = (self.CELL_WIDTH, self.CELL_HEIGHT)


settings = Settings()