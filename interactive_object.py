
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
  def check_collision( self, coord: tuple[int] ) -> bool:
    pass
  

class MultipleInteractiveObject(InteractiveObject):
  def __init__(self, window: Surface) -> None:
    super().__init__(window)
  
  ''' 
    Some InteractiveObjects has the function that set a config for the game,
      this method set that conf
  '''
  @abstractmethod
  def set_conf( self ) -> None:
    pass

  '''
    Click on a multiple option, has to do internal operations to know what option
      the user wants 
  '''
  @abstractmethod
  def click_action( self, coord: tuple[int] ) -> None:
    pass