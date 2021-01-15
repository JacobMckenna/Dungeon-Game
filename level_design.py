#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#level_design.py
#Creates all the levels to be used for the game.

#from global_variables.py import *

# "*" = open sapce
# "x" = map barrier

#display = pygame.display.set_mode((800,800))
#pygame.display.set_caption("Map Testing") 
#line above might not be needed

#Map for level one of the game.
#So far this map is mainly going to be used for testing purposes
testing_level = [
  [ "x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x" ], #1
  [ "x","*","*","*","*","*","*","*","*","*","*","*","*","*","*","x" ], #2
  [ "x","*","*","*","*","*","*","*","*","*","*","*","*","*","*","x" ], #3
  [ "x","*","*","*","*","*","*","*","*","x","*","*","*","*","*","x" ], #4
  [ "x","*","*","*","*","*","*","*","*","*","*","*","*","*","*","x" ], #5
  [ "x","*","*","*","*","*","*","*","*","*","*","*","*","*","*","x" ], #6   x going across
  [ "x","*","*","*","*","x","*","*","*","*","*","x","x","*","*","x" ], #7   y going down
  [ "x","*","*","*","*","*","*","*","*","*","*","*","*","*","*","x" ], #8
  [ "x","*","*","*","*","*","*","*","*","*","*","*","*","*","*","x" ], #9
  [ "x","*","*","*","*","*","*","*","*","*","*","*","*","*","*","x" ], #10
  [ "x","*","*","*","*","*","*","*","*","*","*","*","*","*","*","x" ], #11
  [ "x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x" ]  #12
]

current_level = testing_level

#Displays the chosen level to the user
def display_level(level,screen):
  global current_level 
  current_level = level
  for y in range(len(level)):
    for x in range(len(level[0])):

      if level[y][x] == "*":
        pygame.draw.rect(screen, (255, 255, 255), (x*50,y*50,50,50))
      if level[y][x] == "x":
        pygame.draw.rect(screen, (0, 0, 0), (x*50,y*50,50,50))

#Checks if object is colliding
#def detect_collision(attributes):
#  global current_level
#
#  for y in range(len(current_level)):
#    for x in range(len(current_level[0])):
#      if current_level[y][x] == "x":
#        #if (x*50)+(y*50) >= attributes[0]:
#        print("hi")
