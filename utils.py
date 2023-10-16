'''
  Util functions
'''

from configuration \
  import configuration as conf, \
         menu_configuration as mconf
import pygame as pg

'''
  Convert coord of a matrix into coord of pixel in the window
'''
def matrix_to_real ( i: int, j: int ) -> tuple[int]:
  return j * ( conf.screen_width // conf.CELLS_PER_ROW ), \
         i * ( ( conf.screen_height - conf.score_height ) // conf.CELLS_PER_ROW ) \
         + conf.score_height

'''
  Return a Surface from a sprite's path
'''
def get_image( url: str, img_size = conf.CELL_SIZE ) -> pg.Surface:
  img = pg.image.load(url)
  return pg.transform.scale(img, img_size)


'''
  Return True if the coord passed hit the rect passed
'''
def check_rect_collision( coord: tuple[int], rect: pg.Rect ) -> bool:
  x, y = coord
  return rect.left <= x < rect.right and \
         rect.top <= y < rect.bottom
      