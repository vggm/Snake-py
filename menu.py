'''
  Menu View
'''

import pygame as pg
from pygame import Surface
from interactive_object import InteractiveObject, MultipleInteractiveObject
from configuration \
  import ( configuration as conf, 
           menu_configuration as mconf,
           WindowSize as win_size )
from utils import get_image, check_rect_collision
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
    return check_rect_collision( coord, self.start_rect )
  
  
class PortalWallButton( MultipleInteractiveObject ):
  
  def __portal_button_collision(self, coord: tuple[int]):
    return check_rect_collision( coord, self.portal_rect )
  
  def __wall_button_collision(self, coord: tuple[int]):
    return check_rect_collision( coord, self.wall_rect )
  
  def __init__( self, window: pg.Surface ) -> None:
    
    self.portal = get_image('sprites/mirror_sprite.png', mconf.BUTTON_SIZE)
    self.portal_rect = self.portal.get_rect()
    self.portal_rect.topleft = ( 10, 10 )
    
    self.wall = get_image('sprites/wall_sprite.png', mconf.BUTTON_SIZE)
    self.wall_rect = self.wall.get_rect()
    self.wall_rect.topleft = ( self.wall_rect.right + 10, 10 )
    
    self.background = pg.surface.Surface( mconf.BUTTON_SIZE )
    self.background.fill(Color.BLUE.value)
    self.background_rect = self.background.get_rect()
    
    self.wall_selected = True
    
    super().__init__( window )
    
  def draw(self) -> None:
    if self.wall_selected:
      self.background_rect.topleft = self.wall_rect.topleft
    else:
      self.background_rect.topleft = self.portal_rect.topleft
      
    self.window.blit(self.background, self.background_rect)  
    self.window.blit(self.portal, self.portal_rect)
    self.window.blit(self.wall, self.wall_rect)
    
  
  def check_collision(self, coord: tuple[int]) -> bool:
    return self.__portal_button_collision(coord) or self.__wall_button_collision(coord)
           
  def click_action(self, coord: tuple[int]) -> None:
    
    if self.__portal_button_collision(coord):
      self.wall_selected = False
    else:
      self.wall_selected = True
  
  def set_conf( self ) -> None:
    conf.solid_wall = self.wall_selected
    
    
class NumOfFood( MultipleInteractiveObject ):
  
  def __init__(self, window: Surface) -> None:
    
    self.buttons : list[tuple[pg.Surface, pg.Rect]] = []
    
    SPRITE = 0
    RECT = 1
    self.RANDOM_MODE = 5
    
    ''' Its 10 + mconf.button_height + 10 because it needs to be down from the first button that is in (10,10) '''
    topleft = [10, 10 + mconf.button_height + 20]
    
    ''' Create 5 buttons, Food could spawn from 1 to 5 as max '''
    for i in range(1,5+1):
      
      button = get_image(f'sprites/sprite_{i}.png', mconf.BUTTON_SIZE)
      button_rect = button.get_rect()
      button_rect.topleft = ( topleft[0] + (i-1)*(mconf.button_width + 10) , topleft[1] )
      
      self.buttons.append( (button, button_rect) )
    
    ''' Or aleatory '''
    aleatory_button = get_image('sprites/game_die.png', mconf.BUTTON_SIZE)
    aleatory_button_rect = aleatory_button.get_rect()
    last_button = self.buttons[-1][RECT]
    aleatory_button_rect.topleft = ( last_button.right + 10, topleft[1] )
    
    self.buttons.append( (aleatory_button, aleatory_button_rect) )
    
    self.background = pg.surface.Surface( mconf.BUTTON_SIZE )
    self.background.fill(Color.BLUE.value)
    self.background_rect = self.background.get_rect()
    
    self.selected = 0
    
    super().__init__(window)
    
    
  def click_action(self, coord: tuple[int]) -> None:
    for index, (_, rect) in enumerate(self.buttons):
      if check_rect_collision(coord, rect):
        self.selected = index
        return
  
  
  def draw(self) -> None:
    for i, (sprite, rect) in enumerate(self.buttons):
      if i == self.selected:
        self.background_rect.topleft = rect.topleft
        self.window.blit(self.background, self.background_rect)
      
      self.window.blit(sprite, rect)
      
  
  def check_collision(self, coord: tuple[int]) -> bool:
    return any( check_rect_collision( coord, rect ) 
                  for _, rect in self.buttons )
  
  def set_conf(self) -> None:
    if self.selected == self.RANDOM_MODE:
      conf.ALEATORY_MAX_FOOD = True
      return
    
    conf.ALEATORY_MAX_FOOD = False
    conf.MAX_FOOD = self.selected + 1


class WindowSizeOptions( MultipleInteractiveObject ):
  def __init__(self, window: Surface) -> None:
    
    ''' 
      Its 2*(10 + mconf.button_height) + 10 because it needs to be down from the second button 
        that is in (10,20 + mconf.button_height + 10) 
    '''
    topleft = [10, 2*(20 + mconf.button_height) + 10]
    
    self.buttons : list[tuple[pg.Surface, pg.Rect]] = []
    
    self.sprite_names = [ str(attribute).split('.')[1].lower() for attribute in list(win_size) ]
    
    for i, sprite_name in enumerate(self.sprite_names):
      
      button = get_image(f'sprites/{sprite_name}_sprite.png', mconf.BUTTON_SIZE)
      rect = button.get_rect()
      rect.topleft = [ topleft[0] + (i)*(mconf.button_width + 10) , topleft[1] ]
      
      self.buttons.append( ( button, rect ) )
    
    self.background = pg.surface.Surface( mconf.BUTTON_SIZE )
    self.background.fill(Color.BLUE.value)
    self.background_rect = self.background.get_rect()
    
    self.selected = 0    
    
    super().__init__(window)
  
  def check_collision(self, coord: tuple[int]) -> bool:
    return any( check_rect_collision( coord, rect ) 
                  for _, rect in self.buttons )
  
  def click_action(self, coord: tuple[int]) -> None:
    for index, (_, rect) in enumerate(self.buttons):
      if check_rect_collision(coord, rect):
        self.selected = index
        return
  
  def set_conf(self) -> None:
    option_selected = self.sprite_names[self.selected]
    conf.set_window_size( option_selected )
    
  def draw(self) -> None:
    for i, (sprite, rect) in enumerate(self.buttons):
      if i == self.selected:
        self.background_rect.topleft = rect.topleft
        self.window.blit(self.background, self.background_rect)
      
      self.window.blit(sprite, rect)
  
  
'''
  Return False if game end
    Otherwise, start the game
'''
def Menu():
  
  pg.init()
  pg.display.set_caption('Snake-py')
  clock = pg.time.Clock()
  
  window = pg.display.set_mode(mconf.MENU_SIZE)
  
  '''
    Menu Buttons
  '''
  start_button = StartButton( window )
  portal_wall_button = PortalWallButton( window )
  num_of_food = NumOfFood( window )
  window_size_options = WindowSizeOptions( window )
  
  
  start_menu = True
  end_cause = True
  
  while start_menu:
    
    window.fill(mconf.MENU_BACKGROUND)
    
    start_button.draw()
    portal_wall_button.draw()
    num_of_food.draw()
    window_size_options.draw()
    
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
        
        if start_button.check_collision(mouse_pos): # click on start button
          portal_wall_button.set_conf()
          num_of_food.set_conf()
          window_size_options.set_conf()
          start_menu = False
          
        elif portal_wall_button.check_collision(mouse_pos): # click on portal or wall button
          portal_wall_button.click_action(mouse_pos)
          
        elif num_of_food.check_collision(mouse_pos): # click on max num of food
          num_of_food.click_action(mouse_pos)
          
        elif window_size_options.check_collision(mouse_pos): # click on window size
          window_size_options.click_action(mouse_pos)
    
    clock.tick(60)
    
  return end_cause
    