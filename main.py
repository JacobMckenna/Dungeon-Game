#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#main.py
#Runs the main code for the game and uses functions from all files.

#Import Pygame
import pygame

#Import Other Files
#import level_design
#from global_variables.py import *
#from player_data.py import *

pygame.init()

clock = pygame.time.Clock()

#List Variables
#global current_level

# Set up the drawing window
screen = pygame.display.set_mode([1000, 800])

def check_events(key_list):

    #check all events that happened in this frame
    for event in pygame.event.get():

        # Was a key just pressed down
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

        # Was a key just let go
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
            pygame.quit()
        
    return key_list


class Sprite:
    def __init__(self, x, y, w, h,moveX = 0,moveY = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.moveX = moveX
        self.moveY = moveY

    #Detects if any sprite it touching the "obstacles" aka walls/floors
    def detectCollisions(self):
        global obstacles
        for i in obstacles:
            #if top left of self is colliding
            if(i.x + i.w >= self.x >= i.x and i.y + i.h >= self.y >= i.y):
                
                #if your top left if farther left than their top right (minus your movement)
                if self.x <= i.x + (i.w - abs(self.moveX + 1)): #if touching on the top of self
                    self.y = i.y + i.h

                elif self.y <= i.y + (i.h - abs(self.moveY + 1)): #if touching on the left of self
                    self.x = i.x + i.w

            #if top right of self is colliding
            elif(i.x + i.w >= self.x + self.w >= i.x and i.y + i.h >= self.y >= i.y):

                if self.x >= i.x - (self.w - abs(self.moveX + 1)):
                    self.y = i.y + i.h

                elif self.y <= i.y + (i.h - abs(self.moveY + 1)):
                    self.x = i.x - self.w

            #if bottom left of self is colliding
            elif(i.x + i.w >= self.x >= i.x and i.y + i.h >= self.y + self.h >= i.y):

                if self.x <= i.x + (i.w - abs(self.moveX + 1)): #touches more on bottom
                    self.y = i.y - self.h
                
                elif self.y <= i.y + (self.h - abs(self.moveY + 1)): #touches more on left
                    self.x = i.x + i.w
                
            #if bottom right of self is colliding
            elif(i.x + i.w >= self.x + self.w >= i.x and i.y + i.h >= self.y + self.h >= i.y):
                
                if self.x >= i.x - (self.w - abs(self.moveX + 1)): #touching more on the bottom
                    self.y = i.y - self.h
                    #print(1, self.x,self.y)
                
                elif self.y <= i.y + (self.h - abs(self.moveY + 1)): #touching more on the right
                    self.x = i.x - self.w
                    #print(2, self.x,self.y)

    #JOEL REMEMBER TO ADD COMMENTS TO THIS FUNCTION ITS IMPORTANT
    def render(self,colour = (0, 0, 255),collision_pos = 0):
        #if collision_pos == 0:
        self.x = self.x + self.moveX
        self.y = self.y + self.moveY
        pygame.draw.rect(screen, colour, (self.x,self.y,self.w,self.h))
        self.moveX = 0
        self.moveY = 0
        
        #elif collision_pos == 1:
        #    pygame.draw.rect(screen, colour, (self.x,self.y,self.w,self.h))

def main():
    Player0 = Sprite(50, 750, 40, 60)
    Player1 = Sprite(900, 750, 40, 60)

    Players = [Player0,Player1]

    #keys are w,a,d,up,left,right
    key_list = [False,False,False,False,False,False]

    m0,v0, = 1,12
    m1,v1 = 1,12

    isJump0,isJump1 = False,False

    # Run until the user asks to quit
    while True:

        screen.fill((0,0,0))

        #check for any events this frame
        key_list = check_events(key_list)
        
        ###########
        # JUMPING #
        ###########

        if key_list[0] == True:
            isJump0 = True
        
        if key_list[3] == True:
            isJump1 = True

        #if player0 is jumping
        if isJump0 == True:
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
            F0 = (1 / 2)*m0*(v0**2)
                
            # change the y value
            Player0.moveY -= F0
                
            # constantly reduce velocity
            v0 = v0-1
                
            # object reached its maximum height 
            if v0 < 0: 
                # negative sign is added to counter negative velocity 
                m0 =-1

            # object is where is began
            if v0 == -13:
                m0,v0 = 1,12
                isJump0 = False
        else: #apply gravity
            Player0.moveY = Player0.moveY + 5
        
        #if player 1 is jumping
        if isJump1 == True:
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
            F1 = (1 / 2)*m1*(v1**2)
                
            # change the y value
            Player1.moveY -= F1
                
            # constantly reduce velocity
            v1 = v1-1
                
            # object reached its maximum height 
            if v1<0: 
                # negative sign is added to counter negative velocity 
                m1 =-1

            # object is where is began
            if v1 == -13:
                m1,v1 = 1,12
                isJump1 = False
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

        Player0.detectCollisions()
        Player0.render((0,0,255))

        Player1.detectCollisions()
        Player1.render((255,0,0))

        for block in obstacles:
            block.render((100, 100, 100))

        #pygame.draw.rect(screen, (0, 0, 255), (Player0.x,Player0.y,Player0.w,Player0.h))
        pygame.display.flip()

        clock.tick(50)
        
#First four objects are walls not visible on the map
obstacles = [Sprite(-100,0,125,800),
    Sprite(-100,-100,1200,125),
    Sprite(975,0,125,800),
    Sprite(-100,775,1200,125),
    Sprite(200,750,200,50)]

#start the program
main()

# Done! Time to quit.
pygame.quit()
