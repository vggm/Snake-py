'''
  Menu View
'''

import pygame as pg
from interactive_object import InteractiveObject
from configuration \
  import ( configuration as conf, 
           menu_configuration as mconf )
from utils import get_image
from colors import Color


class StartButton( InteractiveObject ):
  
  def __init__( self, window: pg.Surface ) -> None:
    
    start_font_family = pg.font.Font( mconf.START_BUTTON_FONT, 50 )
    self.start_font = start_font_family.render('START GAME', False, Color.BLACK.value)
    
    self.start_rect = self.start_font.get_rect()
    self.start_rect.centerx = mconf.menu_width / 2
    self.start_rect.bottom = mconf.menu_height - 50
    
    super().__init__( window )

  def draw(self) -> None:
    self.window.blit( self.start_font, self.start_rect )
  
  def check_collision( self, coord: tuple[int] ) -> bool:
    x, y = coord
    return self.start_rect.left <= x < self.start_rect.right and \
           self.start_rect.top <= y < self.start_rect.bottom
  
  
class PortalWallButton( InteractiveObject ):
  
  def __init__( self, window: pg.Surface ) -> None:
    
    self.portal = get_image('sprites/portal_sprite.png', mconf.BUTTON_SIZE)
    self.portal_rect = self.portal.get_rect()
    self.portal_rect.topleft = [10,10]
    
    self.selected = False
    
    super().__init__( window )
    
  def draw(self) -> None:
    self.window.blit(self.portal, self.portal_rect)
  
  def check_collision(self, coord: tuple[int]) -> bool:
    x, y = coord
    return self.portal_rect.left <= x < self.portal_rect.right and \
           self.portal_rect.top <= y < self.portal_rect.bottom
  
  def set_conf( self ) -> None:
    conf.solid_wall = self.selected
  
  
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
  start_button = StartButton( window )
  portal_button = PortalWallButton( window )
  
  
  start_menu = True
  end_cause = True
  
  while start_menu:
    
    window.fill(mconf.MENU_BACKGROUND)
    
    start_button.draw()
    portal_button.draw()
    
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
        elif portal_button.check_collision(mouse_pos):
          portal_button.selected = not portal_button.selected
    
  return end_cause
    