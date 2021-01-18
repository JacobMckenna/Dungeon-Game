#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#global_variables.py
#Contains the important variables to be used across all files.
import pygame

#global screen
global obstacles,red_only,blue_only,Players,doors
global pineapple
global pressure_plates
global testing_level,current_level
global screen
pineapple = "yes"
#List of variables to be used across all files.

#reset sprite lists
obstacles = []
red_only = []
blue_only = []
pressure_plates = []
doors = []

pygame.init()
screen = pygame.display.set_mode([1000, 800])
clock = pygame.time.Clock()