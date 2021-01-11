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

m,v = 1,5

def jump(player_number):
    global m,v
    
    while True:
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
        F = ((1 / 2)*m*(v**2))*2
            
        # change in the y co-ordinate 
        if player_number == 0:
            Player0.y -= F
            
        # decreasing velocity while going up and become negative while coming down 
        v = v-1
            
        # object reached its maximum height 
        if v<0: 
            # negative sign is added to counter negative velocity 
            m =-1

        # objected reaches its original state
        if v == -6:
            m,v = 1,5
            main(False)
        else:
            main(True)


def check_events():
    #check all events that happened in this frame
    for event in pygame.event.get():
        #pressed = pygame.key.get_pressed()
        #if pressed[pygame.K_w]:
        #    Player0.y = Player0.y + 1

        # Is there a key pressed down?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #if pressing w
                #make the player jump
                jump(0)
        
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            pygame.quit()


class Sprite:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

Player0 = Sprite(100, 100, 100, 100)

Players = [Player0]

def main(jumping):
    # Run until the user asks to quit
    while True:

        screen.fill((0,0,0))

        #check for any events this frame
        check_events()

        #display_level(testing_level,screen)

        if jumping:
            jump(0)

        #print(Player0.y)
        pygame.draw.rect(screen, (0, 0, 255), (Player0.x,Player0.y,Player0.w,Player0.h))
        pygame.display.flip()
        

#start the program
main(False)

# Done! Time to quit.
pygame.quit()