'''
  Util functions
'''

from game_features import *

'''
  Convert coord of a matrix into coord of pixel in the window
'''
def matrix_to_real ( i: int, j: int ) -> tuple[int]:
  return j*(SCREEN_WIDTH//CELLS_PER_ROW), i*((SCREEN_HEIGHT-SCORE_HEIGHT)//CELLS_PER_ROW) + SCORE_HEIGHT

