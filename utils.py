'''
  Util functions
'''

from game_features import *

def matrix_to_real ( i: int, j: int ) -> tuple[int]:
  return j*(SCREEN_WIDTH//CELLS_PER_ROW), i*(SCREEN_HEIGHT//CELLS_PER_ROW)