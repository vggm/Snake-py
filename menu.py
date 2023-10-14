'''
  Menu View
'''

import pygame as pg
from configuration \
  import ( configuration as conf, 
           menu_configuration as mconf )
from utils import get_image
from colors import Color


class Start_Button():
  
  def __init__( self, window: pg.Surface ) -> None:
    
    self.window = window
    
    start_font_family = pg.font.Font( mconf.START_BUTTON_FONT, 50 )
    self.start_font = start_font_family.render('START GAME', False, Color.BLACK.value)
    
    self.start_rect = self.start_font.get_rect()
    self.start_rect.centerx = mconf.menu_width / 2
    self.start_rect.bottom = mconf.menu_height - 50
    
    print(self.start_rect.center)
  
  def draw(self) -> None:
    self.window.blit( self.start_font, self.start_rect )
  
  def check_collision( self, coord: tuple[int] ) -> bool:
    x, y = coord
    return self.start_rect.left <= x < self.start_rect.right and \
      self.start_rect.top <= y < self.start_rect.bottom
  
  
class Portal_Wall_Button():
  
  def __init__( self, window: pg.Surface ) -> None:
    portal = get_image('sprites/portal_sprite.png')
    
  def draw() -> None:
    pass
  
  def check_collision(self) -> bool:
    return False
  
  
'''
  Return False if game end
    Otherwise, start the game
'''
def Menu():
  
  pg.init()
  pg.display.set_caption('Snake-py')
  
  window = pg.display.set_mode(mconf.MENU_SIZE)
  
  '''
    Menu Buttons
  '''
  start_button = Start_Button( window )
  
  
  start_menu = True
  end_cause = True
  
  while start_menu:
    
    window.fill(mconf.MENU_BACKGROUND)
    
    start_button.draw() # Start Button
    
    pg.display.update()
      
    for event in pg.event.get():
      if event.type == pg.QUIT:
        start_menu = False
        end_cause = False
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          start_menu = False
          end_cause = False
      elif event.type == pg.MOUSEBUTTONUP: # Mouse click
        mouse_pos = pg.mouse.get_pos()
        if start_button.check_collision(mouse_pos):
          start_menu = False
    
  return end_cause
    