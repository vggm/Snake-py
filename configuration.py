'''
  Game Settings
'''

from colors import Color
from enum import Enum


class WindowSize(Enum):
  
  SMALL  = (480,560)
  MEDIUM = (640,720)
  LARGE  = (960,1040)


class MenuConfiguration:
  def __init__(self) -> None:
    
    # MENU
    self.menu_height = 400
    self.menu_width = 400
    self.MENU_SIZE = ( self.menu_width, self.menu_height )
    
    self.MENU_BACKGROUND = Color.LIGHT_GREEN.value
    
    self.START_BUTTON_FONT = None
    
    self.button_height = 50
    self.button_width = 50
    self.BUTTON_SIZE = ( self.button_width, self.button_height )


class Configuration:
  def __init__(self) -> None:
    # GAME OPTIONS
    self.MAX_FOOD = 5
    self.ALEATORY_MAX_FOOD = True
    
    self.GAME_FPS = 10
    
    # SNAKE
    self.SNAKE_BODY_COLOR = Color.GREEN.value
    self.APPLE_COLOR = Color.RED.value

    self.SNAKE_START_CELL = [[7,3], [7,2]]

    self.START_SPEED = 1

    # if true, when the snake head hit the wall its game over
    # otherwise, the snake head will tp to the other side of the wall
    self.solid_wall = False 
    
    # SCORE
    self.SCORE_ADDITION = 1  
    
    # WINDOW
    self.window_width, self.window_height = WindowSize.MEDIUM.value
    
    # SCORE TOPBAR
    self.score_height = self.window_height - self.window_width
    self.score_width = self.window_width
    self.SCORE_SIZE = (self.score_width, self.score_height)
    self.SCORE_POSITION = (0,0)
    self.SCORE_BACKGROUND_COLOR = Color.BLACK.value
    
    # SCREEN
    self.screen_width = self.window_width
    self.screen_height = self.window_height
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

    # BACKGROUND
    self.BACKGRAOUND_COLOR = Color.LIGHT_GREEN.value
    
  def set_window_size( self, option: str ):
    resolution = WindowSize.LARGE.value
    
    if option == 'small':
      resolution = WindowSize.SMALL.value
    elif option == 'medium':
      resolution = WindowSize.MEDIUM.value      
    
    self.window_width, self.window_height = resolution
    
    self.score_height = self.window_height - self.window_width
    self.score_width = self.window_width
    self.SCORE_SIZE = (self.score_width, self.score_height)
    self.screen_width = self.window_width
    self.screen_height = self.window_height
    self.SCREEN_SIZE = (self.screen_width, self.screen_height)
    self.CELL_HEIGHT = (self.screen_height - self.score_height) // self.CELLS_PER_ROW
    self.CELL_WIDTH = self.screen_width // self.CELLS_PER_ROW
    self.CELL_SIZE = (self.CELL_WIDTH, self.CELL_HEIGHT)


configuration = Configuration()
menu_configuration = MenuConfiguration()