'''
  Util functions
'''

from configuration import configuration as conf
import pygame as pg

'''
  Convert coord of a matrix into coord of pixel in the window
'''
def matrix_to_real ( i: int, j: int ) -> tuple[int]:
  return j * ( conf.screen_width // conf.CELLS_PER_ROW ), \
         i * ( ( conf.screen_height - conf.score_height ) // conf.CELLS_PER_ROW ) \
         + conf.score_height


def get_image(url) -> pg.Surface:
  img = pg.image.load(url)
  return pg.transform.scale(img, conf.CELL_SIZE)
      