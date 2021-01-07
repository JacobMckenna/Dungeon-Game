#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#main.py
#Runs the main code for the game and uses functions from all files.

#Import Pygame
import pygame

#Import Other Files
from level_design.py import *
from global_variables.py import *
from player_data.py import *

pygame.init()

#List Variables
global current_level

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

# Run until the user asks to quit
while True:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    display_level(testing_level,screen)
    pygame.draw.rect(screen, (0, 0, 255), (player1_attributes))
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
