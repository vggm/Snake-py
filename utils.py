'''
  Util functions
'''

from configuration import configuration as st

'''
  Convert coord of a matrix into coord of pixel in the window
'''
def matrix_to_real ( i: int, j: int ) -> tuple[int]:
  return j * ( st.screen_width // st.CELLS_PER_ROW ), \
         i * ( ( st.screen_height - st.score_height ) // st.CELLS_PER_ROW ) \
         + st.score_height

