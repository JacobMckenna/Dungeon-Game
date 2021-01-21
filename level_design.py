#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#level_design.py
#Creates all the levels to be used for the game.

#from global_variables.py import *


#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#level_design.py
#Creates all the levels to be used for the game.
import pygame

from global_variables import *
from classes import *
from button import *
#from main import *

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


#display = pygame.display.set_mode((800,800))
#pygame.display.set_caption("Map Testing")
#line above might not be needed

#Map for level one of the game.
#So far this map is mainly going to be used for testing purposes


def get_testing_level():
      return testing_level

# draws the stone brick background for the entire screen
def draw_stone_background():
    global screen
    screen.fill((0,0,0))
    brick_colour = (75,75,75)

    for y in range(0,800,30):
        for x in range(0,1000,60):
            if y % 60 == 30:
                pygame.draw.rect(screen, brick_colour, (x, y, 56, 26))
            else:
                pygame.draw.rect(screen, brick_colour, (x-30, y, 56, 26))

# draws a small torch
def draw_torch(x,y):
    #colour palette
    wood_colour = (60,40,0)
    centre_flame_colour = (200,90,0)
    outer_flame_colour = (200,150,0)

    #draws the parts of the torch
    pygame.draw.rect(screen, wood_colour, (x+22, y+20, 6, 15))
    pygame.draw.rect(screen, outer_flame_colour, (x+19, y+8, 12, 12))
    pygame.draw.rect(screen, centre_flame_colour, (x+21, y+12, 8, 8))

# draws the exit door
def draw_exit(x,y):
    #colour palette
    wood_colour = (60,40,0)
    black_colour = (0,0,0)

    #draws the parts of the exit
    pygame.draw.rect(screen, wood_colour, (x, y, 50, 50))
    pygame.draw.rect(screen, black_colour, (x+10, y+10, 30, 40))

#USE THIS ONE
def reset_players(current_level):
    global Players
    #for every column
    for y in range(len(current_level)):
        #for every value in the column
        for x in range(len(current_level[0])):
            # "0" is the key for Player0 spawn
            if current_level[y][x] == "0":
                Players[0].x = x*50
                Players[0].y = y*50
            # "1" is the key for Player1 spawn
            if current_level[y][x] == "1":
                Players[1].x = x*50
                Players[1].y = y*50
    return Players

#returns the coordinates of the door to exit the map
def get_exit_location(current_level):
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):

            if current_level[y][x] == "E":
                exit = (x*50, y*50)
    return exit

# takes in two values, seraches the map for the first value and if found will change to the second one
def modify_level(old_value, new_value):
    global current_level

    for y in range(len(current_level)):
        for x in range(len(current_level[0])):
            if current_level[y][x] == old_value:
                current_level[y][x] = new_value

#renders the list of blocks with an colour inputed
def render_block_list(list_to_render, R, G, B, height=0):
    for block in list_to_render:
        block.y += height
        block.h -= height
        block.render((R, G, B))


#Displays the chosen level to the user
def render_level(level, level_num):
    global current_level
    global obstacles
    global red_only
    global blue_only
    global pressure_plates
    global doors

    #reset sprite lists
    obstacles = []
    red_only = []
    blue_only = []
    pressure_plates = []
    doors = []

    #render each block
    if level != current_level:
        for y in range(len(current_level)):
            #for every value in the column
            for x in range(len(current_level[0])):
                # "0" is the key for Player0 spawn
                if current_level[y][x] == "0":
                    Players[0].x = x*50
                    Players[0].y = y*50
                # "1" is the key for Player1 spawn
                if current_level[y][x] == "1":
                    Players[1].x = x*50
                    Players[1].y = y*50
        # reset_players(level)
    current_level = level

    #check each spot in the level
    for y in range(len(level)):
        for x in range(len(level[0])):

            #add walls to obstacles list
            if level[y][x] == "x":
                obstacles.append(Sprite(x*50,y*50,50,50))

            #render the exit
            elif level[y][x] == "E":
                draw_exit(x*50,y*50)

            #render torches
            elif level[y][x] == "i":
                draw_torch(x*50,y*50)

            #add red/blue only blocks to their respective lists
            elif level[y][x] == "R":
                red_only.append(Sprite(x*50,y*50,50,50))
            elif level[y][x] == "B":
                blue_only.append(Sprite(x*50,y*50,50,50))

            #add pressure plates to their respective lists
            elif level[y][x] == "_":
                pressure_plates.append(Pressure_Plate((x*50,y*50 + 40,50,20)))

            #add closed doors to the door and obstacle list
            elif level[y][x] == "|":
                obstacles.append(Sprite(x*50,y*50,50,50))
                doors.append(Door((x*50,y*50,50,50)))

            #add opened doors to the door list
            elif level[y][x] == "/":
                doors.append(Door((x*50,y*50,50,50)))

    #render the blocks in each list
    render_block_list(obstacles, 150, 150, 150)
    render_block_list(red_only, 200, 50, 50, 10)
    render_block_list(blue_only, 50, 50, 200, 10)

    # Button(text, type, click, can_hover, x, y, w, h, colour, bg, font)
    btn_score = Button(f"Lvl:{level_num}", "", "", False, 440, 5, 120, 40, (200, 200, 200), (50, 50, 50), 34)
    btn_score.render()

    return obstacles, red_only, blue_only, pressure_plates, doors
