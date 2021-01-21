#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#level_design.py
#Creates all the levels to be used for the game.

import pygame

from global_variables import *
from classes import *
from button import *

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
# "|" = door (shift + \ NOT capital "i")
# "/" = open door

# Draws a stone background on the screen to add some decoration and to make the game look nicer
def draw_stone_background():
    global screen
    screen.fill((0,0,0))
    brick_colour = (75,75,75)

    #uses a nested for loop to draw each brick in rows then stack the rows below eachother
    for y in range(0,800,30):
        for x in range(0,1000,60):
            if y % 60 == 30:
                # draws the first row of bricks at a normal x and y
                pygame.draw.rect(screen, brick_colour, (x, y, 56, 26))
            else:
                # draws the next row of bricks inbetween the previous bricks
                pygame.draw.rect(screen, brick_colour, (x-30, y, 56, 26))

# Draws a small torch
def draw_torch(x,y):
    """
    Draws a torch at a specific location on the screen to add some decoration to the level.

    Parameters
    ----------
    x : integer
        The x coordinate where the torch is going to be drawn from on the screen.
    y : integer
        The y coordinate where the torch is going to be drawn from on the screen.

    """

    # Colour palette to be used to make the torch.
    wood_colour = (60,40,0)
    centre_flame_colour = (200,90,0)
    outer_flame_colour = (200,150,0)

    # Draws the torch based on the x and y coordinates.
    pygame.draw.rect(screen, wood_colour, (x+22, y+20, 6, 15))
    pygame.draw.rect(screen, outer_flame_colour, (x+19, y+8, 12, 12))
    pygame.draw.rect(screen, centre_flame_colour, (x+21, y+12, 8, 8))

# Draws the exit on the screen.
def draw_exit(x,y):
    """
    Draws the exit for the players to go through and finish the level.

    Parameters
    ----------
    x : integer
        The x coordinate where the exit is going to be drawn from on the screen.
    y : integer
        The y coordinate where the exit is going to be drawn from on the screen.
    """

    # Colour palette to be used to make the exit.
    wood_colour = (60,40,0)
    black_colour = (0,0,0)

    # Draws the exit based on the x and y coordinates.
    pygame.draw.rect(screen, wood_colour, (x, y, 50, 50))
    pygame.draw.rect(screen, black_colour, (x+10, y+10, 30, 40))

# Resets the players locations to the designated locations in the level
def reset_players(current_level, Players):
    """
    Takes in the level, and finds the player start locations in the level. The program then sets each players x and y to those locations in the level and returns those player locations as a list.

    Parameters
    ----------
    current_level : matrix
        The level that the player start locations are going to be taken from.

    Returns
    -------
    Players : list
        A list containing the x and y coordinates for each player.

    """
    # Use a nested for loop to divide the level into individual values.
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):
            # Check if the value is "0"
            # "0" is the key for Player0 spawn
            if current_level[y][x] == "0":
                # If yes, create new x and y coordinates for Player0
                Players[0].x = x*50
                Players[0].y = y*50
            # Check if the value is "1"
            # "1" is the key for Player1 spawn
            if current_level[y][x] == "1":
                # If yes, create new x and y coordinates for Player1
                Players[1].x = x*50
                Players[1].y = y*50

    # Return finalized Players list
    return Players

# Locates the coordinates of the exit in the level and returns them.
def get_exit_location(current_level):
    """
    Takes in the level, and finds the exit locations in the level. Then returns the locations.

    Parameters
    ----------
    current_level : matrix
        The level that the exit locations is going to be found from.

    Returns
    -------
    exit : list
        A list of the coordinates of all exit locations in the level.

    """
    exit = []
    # Use a nested for loop to divide the level into individual values.
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):

            # Check if the value is "E"
            # "E" is the key for exit
            if current_level[y][x] == "E":
                exit = [x*50, y*50]

    # Return the list of exits
    return exit

# Takes in two values, and seraches the map for the first value. If that value is found, it will change it to the second one
def modify_level(old_value, new_value):
    """
    Replaces one value in a level with another value.

    Parameters
    ----------
    old_value : string
        The value that is going to be replaced.
    new_value : string
        The new value that is going to be put in.

    """
    global current_level

    # Use a nested for loop to divide the level into individual values.
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):
            # Find old_value in map and replace it with new_value
            if current_level[y][x] == old_value:
                current_level[y][x] = new_value

# Renders a given list of blocks on the screen with a given colour
def render_block_list(list_to_render, R, G, B, height=0):
    """
    Renders the all the blocks in a given list with its RGB colour.

    Parameters
    ----------
    list_to_render : matrix
        The list of blocked that are going to be rendered on the screen.
    R : integer
        An integer that represents the red in an RGB colour value.
    G : integer
        An integer that represents the green in an RGB colour value.
    B : integer
        An integer that represents the blue in an RGB colour value.
    height : integer
        Additional or less height to the block being rendered. Defaults to 0 so that it is a square.
    """
    # Render every block in the list
    for block in list_to_render:
        # Add or remove any addition height requested
        block.y += height
        block.h -= height

        # Render the block with its RGB colour value.
        block.render((R, G, B))


# Renders the choosen level on the screen.
def render_level(level, level_num):
    """
    Renders all the objects and players in the current level to be displayed on the screen.

    Parameters
    ----------
    level : matrix
        The level that is going to be rendered on the screen.
    level_num : integer
        The number of the current level being displayed.

    Returns
    -------
    obstacles : list
        A list of all the obstacles rendered in the level that the player collides with.
    red_only : list
        A list of all the blocks in the level that only the red player is able to walk through.
    blue_only : list
        A list of all the blocks in the level that only the blue player is able to walk through.
    pressure_plates : list
        A list of all the pressure plates in the level that will open the doors if a player is standing on it.
    doors : list
        A list of all the doors that will be opened in the level if a player is standing on a pressure plate.

    """

    # Decalare global variables used in the function.
    global current_level
    global obstacles
    global red_only
    global blue_only
    global pressure_plates
    global doors

    # Create block lists.
    obstacles = []
    red_only = []
    blue_only = []
    pressure_plates = []
    doors = []

    # Reset player locations if the level being displayed has changed.
    if level != current_level:
        reset_players(level)
    #    for y in range(len(current_level)):
    #        #for every value in the column
    #        for x in range(len(current_level[0])):
    #            # "0" is the key for Player0 spawn
    #            if current_level[y][x] == "0":
    #                Players[0].x = x*50
    #                Players[0].y = y*50
    #            # "1" is the key for Player1 spawn
    #            if current_level[y][x] == "1":
    #                Players[1].x = x*50
    #                Players[1].y = y*50
    current_level = level

    # Add each part of the map to its respective lists with their locaitons.
    # Use a nested for loop to divide the level into individual values.
    for y in range(len(level)):
        for x in range(len(level[0])):

            # Add walls to obstacles list.
            if level[y][x] == "x":
                obstacles.append(Sprite(x*50,y*50,50,50))

            # Render the exit.
            elif level[y][x] == "E":
                draw_exit(x*50,y*50)

            # Render torches.
            elif level[y][x] == "i":
                draw_torch(x*50,y*50)

            # Add red/blue only blocks to their respective lists.
            elif level[y][x] == "R":
                red_only.append(Sprite(x*50,y*50,50,50))
            elif level[y][x] == "B":
                blue_only.append(Sprite(x*50,y*50,50,50))

            # Add pressure plates to their respective lists.
            elif level[y][x] == "_":
                pressure_plates.append(Pressure_Plate((x*50,y*50 + 40,50,20)))

            # Add closed doors to the door and obstacle list.
            elif level[y][x] == "|":
                obstacles.append(Sprite(x*50,y*50,50,50))
                doors.append(Door((x*50,y*50,50,50)))

            # Add opened doors to the door list.
            elif level[y][x] == "/":
                doors.append(Door((x*50,y*50,50,50)))

    # Render the blocks in each list.
    render_block_list(obstacles, 150, 150, 150)
    render_block_list(red_only, 200, 50, 50, 25)
    render_block_list(blue_only, 50, 50, 200, 25)

    # Button(text, type, click, can_hover, x, y, w, h, colour, bg, font)
    btn_score = Button(f"Lvl:{level_num}", "", "", False, 440, 5, 120, 40, (200, 200, 200), (50, 50, 50), 34)
    btn_score.render()

    # Return the block lists.
    return obstacles, red_only, blue_only, pressure_plates, doors
