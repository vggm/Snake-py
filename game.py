import pygame as pg
from sys import exit
from utils import *

VERTICAL = ROW = 0
HORIZONTAL = COL = 1

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
  
  snake = [*SNAKE_START_CELL] # snake body
  snake_head = snake[0]
  snake_tail = snake[-1]
  
  snake_surface = pg.Surface(CELL_SIZE)
  snake_surface.fill(SNAKE_BODY_COLOR)
  
  food = []
  spawn_food( food, snake )
  
  food_surface = pg.Surface(CELL_SIZE)
  food_surface.fill(APPLE_COLOR)
  
  '''
    if [0] is positive go down else go down
    if [1] is positive goto the right else goto the left
  '''
  actual_velocity = 1
  direction = [0,actual_velocity]
  
  food_eaten = False
  
  status_code = 0
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
          if direction[VERTICAL] == 0:
            direction = [-actual_velocity,0]
          
        elif event.key == pg.K_DOWN:
          if direction[VERTICAL] == 0:
            direction = [actual_velocity,0]
          
        elif event.key == pg.K_LEFT:
          if direction[HORIZONTAL] == 0:
            direction = [0,-actual_velocity]
          
        elif event.key == pg.K_RIGHT:
          if direction[HORIZONTAL] == 0:
            direction = [0,actual_velocity]
    
    if food_eaten:
      last_part = snake_tail.copy()
    
    for i in range(len(snake)-1, 0, -1):
      snake[i][ROW] = snake[i-1][ROW]
      snake[i][COL] = snake[i-1][COL]
    
    if food_eaten:
      snake.append( last_part )
      snake_tail = snake[-1]
      food_eaten = False
    
    snake_head[ROW] += direction[VERTICAL]
    snake_head[COL] += direction[HORIZONTAL]
    
    if snake_head == food:
      food_eaten = True
      spawn_food( food, snake )
    
    window.fill(BACKGRAOUND_COLOR)
    for body_i, body_j in snake:
      window.blit(
        snake_surface, matrix_to_real(body_i, body_j)
      )
    
    window.blit(
      food_surface, matrix_to_real(food[ROW], food[COL])
    )
    
    pg.display.update()
    clock.tick(8)
  
  return status_code