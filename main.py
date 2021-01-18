#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#main.py
#Runs the main code for the game and uses functions from all files.

#Import Pygame
import pygame
#import global_variables
#import level_design

#Import Other Files
from global_variables import *
from classes import *
from level_design import *

#global_variables.init()
#pygame.init()

#test cases
test = Sprite(100,48,39,19)
print(test.y)
print(pineapple)
#clock = pygame.time.Clock()

#List Variables
#global current_level
obstacles = []

# Set up the drawing window
screen = pygame.display.set_mode([1000, 800])


def check_events(key_list):

    #check all events that happened in this frame
    for event in pygame.event.get():

        # was a key just pressed down?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #if pressed w
                #make the player jump
                key_list[0] = True
            if event.key == pygame.K_a: #if pressed a
                key_list[1] = True
            if event.key == pygame.K_d: #if pressed d
                key_list[2] = True
            if event.key == pygame.K_UP: #if pressed up
                #make the player jump
                key_list[3] = True
            if event.key == pygame.K_LEFT: #if pressed left
                key_list[4] = True
            if event.key == pygame.K_RIGHT: #if pressed right
                key_list[5] = True

        # was a key just let go?
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: #if just stopped pressing w
                #stops jumping
                key_list[0] = False
            if event.key == pygame.K_a: #if just stopped pressing a
                key_list[1] = False
            if event.key == pygame.K_d: #if just stopped pressing d
                key_list[2] = False
            if event.key == pygame.K_UP: #if just stopped pressing up
                #stops jumping
                key_list[3] = False
            if event.key == pygame.K_LEFT: #if just stopped pressing left
                key_list[4] = False
            if event.key == pygame.K_RIGHT: #if just stopped pressing right
                key_list[5] = False
        
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            #quit the program
            pygame.quit()
    
    #return a list of all significant keys (either True or False for each)
    return key_list

# Main
def main():
    global obstacles
    global current_level # current_level is the level that will constantly be displayed
    global Players
    global pressure_plates

    #i dont think this is needed anymore
    current_level = get_testing_level()

    Players = create_player_sprite(current_level) # returns a list of [Player0,Player1]
    
    #changes player0 and player1 to nicer variables
    Player0 = Players[0]
    Player1 = Players[1]

    #keys are w,a,d,up,left,right
    key_list = [False,False,False,False,False,False]

    # Run until the user asks to quit
    while True:

        #draws the stone brick background
        draw_stone_background()

        #check for any events this frame
        key_list = check_events(key_list)
        
        ###########
        # JUMPING #
        ###########
        
        #if pressing "w"
        if key_list[0] == True and Player0.can_jump == True:
            #make player 0 jump
            Player0.jump()
        else: #apply gravity
            Player0.moveY = Player0.moveY + 5
        
        #if pressing "up"
        if key_list[3] == True and Player1.can_jump == True:
            #make player 1 jump
            Player1.jump()
        else: #apply gravity
            Player1.moveY = Player1.moveY + 5
        
        ############
        # CONTROLS #
        ############

        if key_list[1] == True: #if pressing a
            Player0.moveX = Player0.moveX - 5 #move left
        elif key_list[2] == True: #if pressing d
            Player0.moveX = Player0.moveX + 5 #move right
        
        if key_list[4] == True: #if pressing left
            Player1.moveX = Player1.moveX - 5 #move left
        elif key_list[5] == True: #if pressing right
            Player1.moveX = Player1.moveX + 5 #move right
        
        #display the current level
        render_level(current_level)

        #render the players in the map
        Player0.render((0,0,255),True)
        Player1.render((255,0,0),True)

        #render the buttons and doors
        for button in pressure_plates:
            button.render()
        for door in doors:
            door.render()

        #refresh display
        pygame.display.flip()

        #make each frame stay for 50 miliseconds
        clock.tick(50)

main()

pygame.quit()