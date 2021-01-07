#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#player_data.py
#Contains information specific to the players in the game.


from global_variables.py import *

#location format: (x,y) and size: (x,y)
player1_size_X,player1_size_Y = 30,75
player1_location_X,player1_location_Y = 400,100

player1_attributes = [ player1_location_X+player1_size_X , player1_location_Y+player1_size_Y , player1_size_X , player1_size_Y ]