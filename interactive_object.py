
from abc import ABC, abstractmethod
from pygame import Surface

class InteractiveObject( ABC ):
  
  def __init__( self, window: Surface ) -> None:
    self.window = window
    super().__init__()
  
  ''' Draw the surface into the window passed through the constructor '''
  @abstractmethod
  def draw( self ) -> None:
    pass
  
  ''' Return True if the coord in parameter collision with this object '''
  @abstractmethod
  def check_collision( self, coord: tuple[int] ) -> int:
    pass
  
  ''' 
    Some InteractiveObjects has the function that set a config for the game,
      this method set that conf
  '''
  @abstractmethod
  def set_conf( self ) -> None:
    pass