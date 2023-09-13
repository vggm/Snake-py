import pygame as pg
from sys import exit
from utils import *

VERTICAL = ROW = 0
HORIZONTAL = COL = 1


class Snake():
  def __init__(self) -> None:
    self.body = [*SNAKE_START_CELL] # snake body
    
    self.head = self.body[0]
    self.tail = self.body[-1]

    self.surface = pg.Surface(CELL_SIZE)
    self.surface.fill(SNAKE_BODY_COLOR)
  
  def add( self, position: list[int] ) -> None:
    self.body.append( position )
  
  def draw( self, window: pg.Surface ) ->  None:
    for row, col in self.body:
      window.blit(
        self.surface, matrix_to_real(row, col)
      )


class Foods():
  def __init__(self) -> None:
    self.foods_positions = []
    
    self.max_num_of_food = MAX_FOOD
    
    self.surface = pg.Surface(CELL_SIZE)
    self.surface.fill(APPLE_COLOR)
  
  '''
    Generate a food in a cell of the map that there is not occupied by
    the snake
  '''
  def generate_food( self, snake_body: list[list[int]] ) -> None:
    
    while len(self.foods_positions) < self.max_num_of_food:
    
      found_cell = False
      while not found_cell:
        food_position = [randint(0, CELLS_PER_ROW-1), randint(0, CELLS_PER_ROW-1)]
        if food_position not in snake_body:
          found_cell = True
          self.foods_positions.append(food_position)
  
  def remove( self, position: list[int] ) -> None:
    self.foods_positions.remove( position )
  
  def draw( self, window: pg.Surface ) -> None:
    for row, col in self.foods_positions:
      window.blit(
        self.surface, matrix_to_real(row, col)
      )

class Score():
  def __init__(self) -> None:
    self.points = 0
    self.addition = SCORE_ADDITION
    
    self.font = pg.font.Font( size=FONT_SIZE )
    
  def add_score( self, points = SCORE_ADDITION ) -> None:
    self.points += points
  
  def draw( self, window: pg.Surface ) -> None:
    score_font = self.font.render( f'Score: {self.points}', True, WHITE, None )
    score_rec = score_font.get_rect()
    score_rec.centery = SCORE_HEIGHT / 2
    score_rec.centerx = SCORE_WIDTH / 2
    
    window.blit( score_font, score_rec )


'''
  Finish the game
'''
def end_game() -> None:
  pg.quit()
  exit()

'''
  Main Game
  
  return 1 if user wants to close the game
'''
def start_game() -> int:
  pg.init()
  pg.display.set_caption('Snake-py')
  
  clock = pg.time.Clock()
  window = pg.display.set_mode(SCREEN_SIZE)
  
  score_board = pg.Surface( SCORE_SIZE )
  score_board.fill( BLACK )

  '''
    Generate snake and foods
  '''
  snake = Snake()
  
  foods = Foods()
  foods.generate_food( snake.body )
  
  '''
    Global states
  '''
  food_eaten = False
  status_code = 0
  score = Score()
  
  '''
    if [0] is positive go down else go down
    if [1] is positive goto the right else goto the left
  '''
  actual_velocity = START_VELOCITY
  direction = [0,actual_velocity]
  
  
  run = True
  while run:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        status_code = 1
        run = False
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          status_code = 1
          run = False
        elif event.key == pg.K_UP:
          if snake.head[VERTICAL] - 1 != snake.body[1][VERTICAL]:
            direction = [-actual_velocity,0]
          
        elif event.key == pg.K_DOWN:
          if snake.head[VERTICAL] + 1 != snake.body[1][VERTICAL]:
            direction = [actual_velocity,0]
          
        elif event.key == pg.K_LEFT:
          if snake.head[HORIZONTAL] - 1 != snake.body[1][HORIZONTAL]:
            direction = [0,-actual_velocity]
          
        elif event.key == pg.K_RIGHT:
          if snake.head[HORIZONTAL] + 1 != snake.body[1][HORIZONTAL]:
            direction = [0,actual_velocity]
    
    if food_eaten:
      tail_position = snake.tail.copy()
    
    for i in range(len(snake.body)-1, 0, -1):
      snake.body[i][ROW] = snake.body[i-1][ROW]
      snake.body[i][COL] = snake.body[i-1][COL]
    
    if food_eaten:
      snake.add( tail_position )
      score.add_score()
      snake.tail = snake.body[-1]
      food_eaten = False
    
    snake.head[ROW] += direction[VERTICAL]
    snake.head[COL] += direction[HORIZONTAL]
    
    '''
      Check head collision
    '''
    # collision with his own body: game over
    if snake.head in snake.body[1:]:
      status_code = 2
      run = False
    
    # collision with a food
    if snake.head in foods.foods_positions:
      food_eaten = True
      foods.remove( snake.head )
      foods.generate_food( snake.body )
    
    '''
      Draw surfaces
    '''
    window.fill(BACKGRAOUND_COLOR)
    window.blit( score_board, (0,0) )
    
    snake.draw( window )
    foods.draw( window )
    score.draw( window )
    
    pg.display.update()
    clock.tick(5)
  
  return status_code