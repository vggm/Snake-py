'''
  Util functions
'''

from game_features import *
from random import randint

'''
  Convert coord of a matrix into coord of pixel in the window
'''
def matrix_to_real ( i: int, j: int ) -> tuple[int]:
  return j*(SCREEN_WIDTH//CELLS_PER_ROW), i*(SCREEN_HEIGHT//CELLS_PER_ROW)

'''
  Spawn a food in a cell of the map that there is not occupied by
  the snake
'''
def spawn_food( food_cell: list[int], snake: list[list[int]] ) -> None:
  found_cell = False
  while not found_cell:
    food_cell[:] = [randint(0, CELLS_PER_ROW-1), randint(0, CELLS_PER_ROW-1)]
    if food_cell not in snake:
      found_cell = True