#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#global_variables.py
#Contains the important variables to be used across all files.

### PYGAME
import pygame

### GENERAL

SCREEN_DIMEN = [1000, 800]

# Choose the levels.
level_num = 1

# Program state
game_state = "menu"

# Keys reference
#keys are w,a,d,up,left,right
key_list = [False,False,False,False,False,False]

# Import external modules
import pygame

# Initalize pygame and clock.
pygame.init()

clock = pygame.time.Clock()

# Organize bg images into a dictionary for easier access.
icon = pygame.image.load('./assets/images/icon.png')
# Set the window icon.
pygame.display.set_icon(icon)
# Set the window title.
pygame.display.set_caption('The Official Fireboy and Watergirl Game - Copyright 2069')
pygame.display.set_caption("Joe's Dungeon Game")
# Set up the drawing window.
screen = pygame.display.set_mode([SCREEN_DIMEN[0], SCREEN_DIMEN[1]])


events = pygame












#global screen
# pineapple is a test variable to make sure global_variables.py is working properly.
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

obstacles = []
red_only = []
blue_only = []
pressure_plates = []
doors = []

# MAP LEGEND

# "." = open sapce
# "x" = map barrier --  CANNOT HAVE 1 BLOCK GAPS OR CAN JUMP THROUGH
# "E" = exit
# "R" = red only area
# "B" = blue only area
# "0" = player 0 start
# "1" = player 1 start
# "i" = decoration torch
# "_" = pressure plate
# "|" = vertical door (shift + \ NOT capital "i")

#testing level to test the features
levels = [
    [
    #      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
        [ "x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x" ], #0
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #1
        [ "x",".","x",".","x",".","x",".","x",".",".","x",".","x",".","x",".","x",".","x" ], #2
        [ "x",".",".",".",".",".",".",".",".","x","x",".",".",".",".",".",".",".",".","x" ], #3
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #4
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #5   x going across
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #6   y going down
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".","x","x","x","x","x","x","x" ], #7
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".","|",".",".",".",".",".","x" ], #8
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".","|",".",".",".",".",".","x" ], #9
        [ "x",".","x","x",".",".",".",".",".",".",".",".",".","x","x","x","x","x",".","x" ], #10
        [ "x",".",".",".",".",".",".",".",".","x","x",".",".",".",".",".",".",".",".","x" ], #11
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","_","x" ], #12
        [ "x",".",".",".",".",".",".","i",".",".",".",".","i",".",".",".",".",".","x","x" ], #13
        [ "x","E",".","0",".","B","B","x","x","x","x","x","x","R","R",".","1",".",".","x" ], #14
        [ "x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x" ]  #15
    ],
    [
    #      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
        [ "x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x" ], #0
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #1
        [ "x",".","x",".","x",".","x",".","x",".",".","x",".","x",".","x",".","x",".","x" ], #2
        [ "x",".",".",".",".",".",".",".",".","x","x",".",".",".",".",".",".",".",".","x" ], #3
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #4
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #5   x going across
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #6   y going down
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".","x","x","x","x","x","x","x" ], #7
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".","|",".",".",".",".",".","x" ], #8
        [ "x",".","0","1",".",".",".",".",".",".",".",".",".","|",".",".",".",".",".","x" ], #9
        [ "x","x","x","x","x",".",".",".",".",".",".",".",".","x","x","x","x","x",".","x" ], #10
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","x" ], #11
        [ "x",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","_","x" ], #12
        [ "x",".",".",".",".",".",".","i",".",".",".",".","i",".",".",".",".",".","x","x" ], #13
        [ "x","E",".",".",".",".",".","x","x","B","B","x","x","R","R",".",".",".",".","x" ], #14
        [ "x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x" ]  #15
    ]
]

#set current level being displayed
current_level = levels[0]
