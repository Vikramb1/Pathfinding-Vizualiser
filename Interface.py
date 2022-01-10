import pygame, sys
from time import sleep
import math
import time
import A_Star_Search
import DFS
import Djikstra
import GBFS
import BFS
import Bidirectional_BFS
import Prims_Algorithm

pygame.init()
pygame.font.init()

(width, height) = (600, 600)
screen = pygame.display.set_mode((200 + width, height))
pygame.display.flip()
clock = pygame.time.Clock()

background_colour = (128,0,128)
white = (255,255,255)
black = (0,0,0)
blue = (30,255,255)
other = (123,23,54)
other2 = (3,230,172)
other3 = (239,3,255)
color = (222, 49, 99)
g = (106, 15, 142)

pygame.display.set_caption('Pathfinding Visualizer')

cols,rows = 40, 40
maze = [[0 for p in range(40)] for i in range(40)]

def showText():
  rect = pygame.Rect(600,1,199,599)
  pygame.draw.rect(screen, white, rect)
  font = pygame.font.SysFont('Comic Sans MS', 15)
  types = ['A* search', 'Dijkstra\'s Algorithm', 'Greedy BFS', 'BFS', 'DFS', 'Bidirectional BFS']
  offset = 50
  for n in types:
    text = font.render(n, True, black)
    screen.blit(text, (630,offset))
    offset += 50
  text = font.render('Generate Maze', True, black)
  screen.blit(text, (630,400))
  text = font.render('Reset Board', True, black)
  screen.blit(text, (630,500))
  
# def fade(endcolor,rect):  
#   for i in range(0,endcolor):
#     pygame.draw.rect(screen,(other3[0],i,other3[1]),rect)
#     pygame.display.flip()
  
def drawSearch(vals, lists):
  blockSize = width//cols
  i = 0
  print(len(lists))
  for t in lists:
    for j in t:
      if j != start and j != end:
        rect = pygame.Rect(j[0]*blockSize,j[1]*blockSize,width//cols-1,width//cols-1)
        #fade(other[2],rect)
        pygame.draw.rect(screen,(other3[0],i,other3[2]),rect)
        pygame.display.flip()
        pygame.time.delay(2)
    i += 220/len(lists)
    pygame.display.flip()

def drawPath(path):
  blockSize = width//cols
  for k in path:
    if k != end:
      rect = pygame.Rect(k[0]*blockSize,k[1]*blockSize,width//cols-1,width//cols-1)
      pygame.draw.rect(screen,blue,rect)
      pygame.display.flip()
      pygame.time.delay(10)   

def drawGrid(start, end, maze):
  blockSize = width//cols
  for x in range(0, width, blockSize):
      for y in range(0, height, blockSize):
        rect = pygame.Rect(x, y, blockSize-1, blockSize-1) 
        a = x//blockSize
        b = y//blockSize
        if maze[a][b] == 1:
          pygame.draw.rect(screen,black,rect)
        else:
          pygame.draw.rect(screen, white, rect)
  if start != None:
    rect = pygame.Rect(start[0]*15, start[1]*15, blockSize-1, blockSize-1)
    pygame.draw.rect(screen, color, rect)
  if end != None:
    rect = pygame.Rect(end[0]*15, end[1]*15, blockSize-1, blockSize-1)
    pygame.draw.rect(screen, g, rect)

def showWalls(li):
  blockSize = width//cols
  for t in li:
    rect = pygame.Rect(t[0]*15, t[1]*15, blockSize-1, blockSize-1)
    pygame.draw.rect(screen, black, rect)

def chooseAlgo(algorithm):
  algos = {'A*': A_Star_Search.astar(start,end,maze),'Dijkstra': Djikstra.djikstra(start,end,maze),'GBFS': GBFS.gbfs(start,end,maze),'BFS': BFS.bfs(start,end,maze),'DFS': DFS.dfs(start,end,maze),'Bi_BFS':Bidirectional_BFS.bbfs(start,end,maze)}
  result = algos[algorithm]
  path = result[0]
  result = result[1:][0]
  return path,result

def updateMaze(maze, walls):
  maze = [[0 for p in range(40)] for i in range(40)]
  for t in walls:
    maze[t[0]][t[1]] = 1
  return maze

running = True
algorithm = None
start = None
end = None
ty = 0
walls = []
run = False
while running:
  for event in pygame.event.get():
    showText()
    maze = updateMaze(maze, walls)
    drawGrid(start,end,maze)
    showWalls(walls)
    if run and start != None and end != None and algorithm != None:
      chosen = chooseAlgo(algorithm)
      drawSearch(chosen[0],chosen[1])
      drawPath(chosen[0])
      time.sleep(2)
      run = False
      algorithm = None
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_RETURN:  
         run = True
    if pygame.mouse.get_pressed(3)[2]:
      ty += 1
      ty = ty%3
    if pygame.mouse.get_pressed(3)[0]:
      pos = pygame.mouse.get_pos()
      row, col = pos[0]//15,pos[1]//15
      if 0 <= row < 40 and 0 <= col < 40:
        if ty == 0:
          if (row,col) != end:
              start = (row,col)
        elif ty == 1:
          if (row,col) != start:
            end = (row,col)
        else:
          try:
            walls.remove((row,col))
            maze[row][col] = 0
          except:
            walls.append((row,col))
            maze[row][col] = 1
      else:
        if 610 <= pos[0] <= 790 and 30 <= pos[1] <= 70: 
          algorithm = 'A*'
        elif 610 <= pos[0] <= 790 and 80 <= pos[1] <= 120:
          algorithm = 'Dijkstra'
        elif 610 <= pos[0] <= 790 and 130 <= pos[1] <= 170:
          algorithm = 'GBFS'
        elif 610 <= pos[0] <= 790 and 180 <= pos[1] <= 220:
          algorithm = 'BFS'
        elif 610 <= pos[0] <= 790 and 260 <= pos[1] <= 270:
          algorithm = 'DFS'
        elif 610 <= pos[0] <= 790 and 280 <= pos[1] <= 320:
          algorithm = 'Bi_BFS'
        elif 610 <= pos[0] <= 790 and 380 <= pos[1] <= 420:
          walls = []
          walls = Prims_Algorithm.prims()
        elif 610 <= pos[0] <= 790 and 480 <= pos[1] <= 520:
          start = None
          end = None
          walls = []
        ty = 0

    pygame.display.update()


