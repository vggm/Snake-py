from random import randint
from sys import exit
import pygame as pg
from utils import *


VERTICAL   = ROW = 0
HORIZONTAL = COL = 1


class Snake():
  def __init__(self) -> None:

    self.body = [ position.copy() for position in SNAKE_START_CELL ] # snake body
    
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
    
    self.surface = pg.Surface(CELL_SIZE)
    self.surface.fill(APPLE_COLOR)
  
  '''
    Generate N foods in a cell of the map that there is not occupied by
    the snake.
    
    N = MAX_FOOD - len(self.foods_positions)
  '''
  def generate_food( self, snake_body: list[list[int]] ) -> bool:
    
    if len( snake_body ) > CELLS_PER_ROW ** 2 - MAX_FOOD:
      return False
    
    if ALEATORY_MAX_FOOD and len( self.foods_positions ) > 0:
      return True
    
    n_food = randint(1, MAX_FOOD) if ALEATORY_MAX_FOOD else MAX_FOOD
    
    while len(self.foods_positions) < n_food:
    
      found_cell = False
      while not found_cell:
        food_position = [randint(0, CELLS_PER_ROW-1), randint(0, CELLS_PER_ROW-1)]
        if food_position not in (snake_body + self.foods_positions):
          found_cell = True
          self.foods_positions.append(food_position)
    
    return True
  
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
    
    self.font = pg.font.Font( SCORE_FONT, SCORE_FONT_SIZE )
    self.score = self.font.render( f'Score: {self.points}', True, WHITE, None )
    self.score_rec = self.score.get_rect()
    self.score_rec.centery = SCORE_HEIGHT / 2
    self.score_rec.centerx = SCORE_WIDTH / 2
    
    self.board = pg.Surface( SCORE_SIZE )
    self.board.fill( BLACK )
    
  def add_score( self, points = SCORE_ADDITION ) -> None:
    self.points += points
  
  def draw( self, window: pg.Surface ) -> None:
    self.score = self.font.render( f'Score: {self.points}', True, WHITE, None )
    window.blit( self.board, SCORE_POSITION )
    window.blit( self.score, self.score_rec )


class Game():

  def __init__( self ) -> None:
    pg.init()
    pg.display.set_caption('Snake-py')
    
    self.window = pg.display.set_mode(SCREEN_SIZE)
    self.clock  = pg.time.Clock()
    self.score: Score
  
  
  '''
    Main Game
    
    return True game over
    return False if user wants to close the game
  '''
  def start( self ) -> bool:

    window = self.window
    self.score = Score()
    
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
    end_cause = False
  
    
    '''
      if [0] is positive go down else go down
      if [1] is positive goto the right else goto the left
    '''
    actual_speed = START_SPEED
    direction = [0,actual_speed]
    
    
    run = True
    while run:
      
      '''
        Draw surfaces
      '''
      window.fill(BACKGRAOUND_COLOR)
      
      snake.draw( window )
      foods.draw( window )
      self.score.draw( window )
      
      pg.display.update()
      self.clock.tick(8)
      
      '''
        Listening events
      '''
      for event in pg.event.get():
        if event.type == pg.QUIT:
          end_cause = True
          run = False
        elif event.type == pg.KEYDOWN:
          if event.key == pg.K_ESCAPE:
            end_cause = True
            run = False
          elif event.key == pg.K_UP:
            if snake.head[VERTICAL] - 1 != snake.body[1][VERTICAL]:
              direction = [-actual_speed,0]
            
          elif event.key == pg.K_DOWN:
            if snake.head[VERTICAL] + 1 != snake.body[1][VERTICAL]:
              direction = [actual_speed,0]
            
          elif event.key == pg.K_LEFT:
            if snake.head[HORIZONTAL] - 1 != snake.body[1][HORIZONTAL]:
              direction = [0,-actual_speed]
            
          elif event.key == pg.K_RIGHT:
            if snake.head[HORIZONTAL] + 1 != snake.body[1][HORIZONTAL]:
              direction = [0,actual_speed]
    

      '''
        Game Logic
      '''
      if food_eaten:
        tail_position = snake.tail.copy()
      
      for i in range(len(snake.body)-1, 0, -1):
        snake.body[i][ROW] = snake.body[i-1][ROW]
        snake.body[i][COL] = snake.body[i-1][COL]
      
      if food_eaten:
        snake.add( tail_position )
        snake.tail = snake.body[-1]
        food_eaten = False
      
      snake.head[ROW] += direction[VERTICAL]
      snake.head[COL] += direction[HORIZONTAL]
      
      '''
        Check head collision
      '''
      # collision with walls: game over if solid_wall is true, otherwise: tp to the other side
      if  CELLS_PER_ROW <= snake.head[ROW] or snake.head[ROW] < 0 or \
          CELLS_PER_ROW <= snake.head[COL] or snake.head[COL] < 0:
        
        if SOLID_WALL:
          run = False
        
        else:
          snake.head[ROW] %= CELLS_PER_ROW
          snake.head[COL] %= CELLS_PER_ROW
          
      # collision with his own body: game over
      if snake.head in snake.body[1:]:
        run = False
      
      # collision with food
      if snake.head in foods.foods_positions:
        food_eaten = True
        self.score.add_score()
        foods.remove( position=snake.head )
        if not foods.generate_food( snake.body ):
          run = False
    
    return end_cause
  
  
  '''
    Game Over Screen
    
    return True if the player wants to close the game
    return False if the player wants to play again
  '''
  def game_over( self ) -> bool:
    
    window = self.window
    
    font = pg.font.Font( GAME_OVER_FONT, GAME_OVER_FONT_SIZE )
    game_over_font = font.render( 'Game Over!!', True, RED, None )
    game_over_font_rec = game_over_font.get_rect()
    game_over_font_rec.centery = SCREEN_HEIGHT / 2 - 100
    game_over_font_rec.centerx = SCREEN_WIDTH / 2
    
    font = pg.font.Font( SCORE_FONT, SCORE_FONT_SIZE - 10 )
    score_font = font.render( f'Your Score is {self.score.points}', True, WHITE, None )
    score_font_rec = score_font.get_rect()
    score_font_rec.centery = SCREEN_HEIGHT / 2
    score_font_rec.centerx = SCREEN_WIDTH / 2 
    
    font = pg.font.Font( SCORE_FONT, SCORE_FONT_SIZE - 30 )
    restart_font = font.render( f'Press R to Restart!!', True, WHITE, None )
    restart_font_rec = restart_font.get_rect()
    restart_font_rec.centery = SCREEN_HEIGHT / 2 + 100
    restart_font_rec.centerx = SCREEN_WIDTH / 2 
    
    user_option = True
    showing_score = True
    while showing_score:
      window.fill(BLACK)
      
      window.blit( game_over_font, game_over_font_rec )
      window.blit( restart_font, restart_font_rec )
      window.blit( score_font, score_font_rec )
      
      pg.display.update()
      self.clock.tick(GAME_FPS)
      
      for event in pg.event.get():
          if event.type == pg.QUIT:
            showing_score = False
          elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
              showing_score = False
            
            if event.key == pg.K_r:
              user_option = False
              showing_score = False

    return user_option
  
  
  '''
    Finish the game
  '''
  def end(self) -> None:
    pg.quit()
    exit()


