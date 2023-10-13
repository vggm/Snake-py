'''
  Game Settings
'''

from colors import Color

class Configuration():
  def __init__(self) -> None:
    # GAME OPTIONS
    self.MAX_FOOD = 5
    self.ALEATORY_MAX_FOOD = True
    
    self.GAME_FPS = 8

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
    self.SCORE_BACKGROUND_COLOR = Color.BLACK.value
    
    # SCREEN
    self.screen_width = 640
    self.screen_height = 640 + self.score_height
    self.SCREEN_SIZE = (self.screen_width, self.screen_height)
    
    # CELLS
    self.CELLS_PER_ROW = 16
    self.CELL_HEIGHT = (self.screen_height - self.score_height) // self.CELLS_PER_ROW
    self.CELL_WIDTH = self.screen_width // self.CELLS_PER_ROW
    self.CELL_SIZE = (self.CELL_WIDTH, self.CELL_HEIGHT)
    
    # FONT
    self.SCORE_FONT = None # PATH TO CUSTOM FONT FAMILY
    self.SCORE_FONT_SIZE = self.score_height - 20

    self.GAME_OVER_FONT = None # PATH TO CUSTOM FONT FAMILY
    self.GAME_OVER_FONT_SIZE = 100
    
    # SNAKE
    self.SNAKE_BODY_COLOR = Color.GREEN.value
    self.APPLE_COLOR = Color.RED.value

    self.SNAKE_START_CELL = [[7,3], [7,2]]

    self.START_SPEED = 1

    # BACKGROUND
    self.BACKGRAOUND_COLOR = Color.LIGHT_GREEN.value


configuration = Configuration()