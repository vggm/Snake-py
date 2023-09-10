import pygame as pg
from sys import exit
from utils import *
from random import randint

if __name__ == '__main__':
  pg.init()
  pg.display.set_caption('Snake-py')
  
  clock = pg.time.Clock()
  window = pg.display.set_mode(SCREEN_SIZE)
  
  snake = [[7,3]] # snake body
  snake_head = snake[0]
  
  snake_surface = pg.Surface(CELL_SIZE)
  snake_surface.fill(GREEN)
  
  food = [randint(0, CELLS_PER_ROW-1), randint(0, CELLS_PER_ROW-1)]
  
  food_surface = pg.Surface(CELL_SIZE)
  food_surface.fill(RED)
  
  direction = [0,0.1]
  
  start = True
  while start:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        start = False
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          start = False
        elif event.key == pg.K_UP:
          direction = [-0.1,0]
          
        elif event.key == pg.K_DOWN:
          direction = [0.1,0]
          
        elif event.key == pg.K_LEFT:
          direction = [0,-0.1]
          
        elif event.key == pg.K_RIGHT:
          direction = [0,0.1]
    
    
    snake_head[0] += direction[0]
    snake_head[1] += direction[1]
    
    
    window.fill(BACKGRAOUND_COLOR)
    for body_i, body_j in snake:
      window.blit(
        snake_surface, matrix_to_real(body_i, body_j)
      )
    
    window.blit(
      food_surface, matrix_to_real(food[0], food[1])
    )
    
    pg.display.update()
    clock.tick(60)
  
  pg.quit()
  exit()