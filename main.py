#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#main.py
#Runs the main code for the game and uses functions from all files.

#Import Pygame
import pygame

#Import Other Files
#from level_design.py import *
#from global_variables.py import *
#from player_data.py import *

pygame.init()

#List Variables
global current_level

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

def check_events():

    #keys are w,a,d,up,left,right
    key_list = [False,False,False,False,False,False]

    #check all events that happened in this frame
    for event in pygame.event.get():
        #Get all the pressed keys
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a]: #if pressing a
            key_list[1] = True
        if pressed[pygame.K_d]: #if pressing d
            key_list[2] = True

        # Is there a key pressed down?
        # The difference between this and using pressed[] is this only gives an output once
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #if pressing w
                #make the player jump
                key_list[0] = True
        
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            pygame.quit()
        
    return key_list


class Sprite:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def main():
    Player0 = Sprite(100, 100, 100, 100)
    Player1 = Sprite(300, 0, 100, 100)

    Players = [Player0,Player1]

    m0,v0, = 1,10
    m1,v1 = 1,10

    isJump0,isJump1 = False,False

    # Run until the user asks to quit
    while True:

        screen.fill((0,0,0))

        #check for any events this frame
        keys = check_events()

        print(keys[0],keys[1])

        if keys[1] == True: #if pressing a
            Player0.x = Player0.x - 5 #change 5 to change speed
        elif keys[2] == True: #if pressing d
            Player0.x = Player0.x + 5 #change 5 to change speed
        
        ###########
        # JUMPING #
        ###########

        if keys[0] == True:
            isJump0 = True
        
        if keys[3] == True:
            isJump1 = True

        #if player0 is jumping
        if isJump0 == True:
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
            F0 = (1 / 2)*m0*(v0**2)
                
            # change the y value
            Player0.y -= F0
                
            # constantly reduce velocity
            v0 = v0-1 #chage 0.5 lower values to get longer jump
                
            # object reached its maximum height 
            if v0<0: 
                # negative sign is added to counter negative velocity 
                m0 =-1

            # object is where is began
            if v0 == -11:
                m0,v0 = 1,10
                isJump0 = False
        
        #if player 1 is jumping
        if isJump1 == True:
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
            F1 = (1 / 2)*m1*(v1**2)
                
            # change the y value
            Player1.y -= F1
                
            # constantly reduce velocity
            v1 = v1-0.5 #chage 0.5 lower values to get longer jump
                
            # object reached its maximum height 
            if v1<0: 
                # negative sign is added to counter negative velocity 
                m1 =-1

            # object is where is began
            if v1 == -11:
                m1,v1 = 1,10
                isJump1 = False
            
        ############
        # CONTROLS #
        ############

        

        #make each frame last 30 miliseconds
        pygame.time.delay(30) 

        #print(Player0.y)
        pygame.draw.rect(screen, (0, 0, 255), (Player0.x,Player0.y,Player0.w,Player0.h))
        pygame.display.flip()
        

#start the program
main()

# Done! Time to quit.
pygame.quit()