#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Created Jan 7, 2021
#player_data.py
#Contains information specific to the players in the game.


from global_variables import *

img_player1 = pygame.image.load('./assets/images/player1.png')
img_player2 = pygame.image.load('./assets/images/player2.png')

#class used for creating obstacles and players
class Sprite:
    def __init__(self, x, y, w, h, player = 0):
        self.x = x #x coordinate
        self.y = y #y coordinate
        self.w = w #width
        self.h = h #height
        self.moveX = 0 #how far to move x this frame
        self.moveY = 0 #how far to move y this frame

        #jumping related values:
        self.mass = 4
        self.velocity = 5
        self.jumping = False #the player is not starting jumping
        self.can_jump = True #the player is able to jump

        # whether object is a player
        self.player = player

    def get_rect(self):
        #returns a pygame Rect of the sprite
        return pygame.Rect(int(self.x), int(self.y), int(self.w), int(self.h))

    #Detects if any sprite it touching the "obstacles" aka walls/floors
    def detectCollisions(self, blocks, Players):

        #get all the global lists that this function requires
        # global red_only,blue_only,Players,current_level,doors
        obstacles = blocks[0]
        red_only = blocks[1]
        blue_only = blocks[2]
        pressure_plates = blocks[3]
        doors = blocks[4]

        #loop through all walls/floors
        for i in obstacles:
            #if top left of self is colliding
            if(i.x + i.w >= self.x >= i.x and i.y + i.h >= self.y >= i.y):

                #if your left side is farther left than their right side (minus X movement)
                if self.x <= i.x + (i.w - 6):#- abs(self.moveX)): #touches more on the top
                    self.y = i.y + i.h

                #if your top side is above their bottom side (minus Y movement)
                elif self.y <= i.y + (i.h ):#- abs(self.moveY)): #touches more on the left
                    self.x = i.x + i.w

            #if top right of self is colliding
            elif(i.x + i.w >= self.x + self.w >= i.x and i.y + i.h >= self.y >= i.y):

                #if your right side is farther right than their left side
                if self.x >= i.x - (self.w - 6):#- abs(self.moveX)): #touches more on the top
                    self.y = i.y + i.h

                #if your top side is above their bottom side
                elif self.y <= i.y + (i.h ):#- abs(self.moveY)): #touches more on the right
                    self.x = i.x - self.w

            #if bottom left of self is colliding
            elif(i.x + i.w >= self.x >= i.x and i.y + i.h >= self.y + self.h >= i.y):

                #if your left side is farther left than their right side
                if self.x <= i.x + (i.w - abs(self.moveY)):#- abs(self.moveX)): #touches more on bottom
                    self.y = i.y - self.h
                    self.can_jump = True
                    self.jumping = False

                #if your bottom side is below their top side
                elif self.y <= i.y - (self.h ):#- abs(self.moveY)): #touches more on left
                    self.x = i.x + i.w

            #if bottom right of self is colliding
            elif(i.x + i.w >= self.x + self.w >= i.x and i.y + i.h >= self.y + self.h >= i.y):

                #if your right side is farther right than their left side
                if self.x >= i.x - (self.w - abs(self.moveY)):#- abs(self.moveX)): #touches more on the bottom
                    self.y = i.y - self.h
                    self.can_jump = True
                    self.jumping = False

                #if your bottom side is below their top side
                elif self.y <= i.y + (self.h ):#- abs(self.moveY)): #touches more on the right
                    self.x = i.x - self.w

        #go through all the red only squares
        for red in red_only:
            #if it is colliding with a red rectagle
            if self.get_rect().colliderect(red.get_rect()):
                #if it is the blue player
                if self == Players[0]:
                    print("Restarting Level...")
                    #restart the level

                    # reset_players(current_level)
                    for y in range(len(current_level)):
                        #for every value in the column
                        for x in range(len(current_level[0])):
                            # "0" is the key for Player0 spawn
                            if current_level[y][x] == "0":
                                Players[0].x = x*50
                                Players[0].y = y*50
        # print(current_level)

        #go through all the blue only squares
        for blue in blue_only:
            #if it is colliding with a blue rectagle
            if self.get_rect().colliderect(blue.get_rect()):
                #if it is the red player
                if self == Players[1]:
                    print("Restarting Level...")
                    #restart the level

                    # reset_players(current_level)
                    for y in range(len(current_level)):
                        #for every value in the column
                        for x in range(len(current_level[0])):
                            # "1" is the key for Player1 spawn
                            if current_level[y][x] == "1":
                                Players[1].x = x*50
                                Players[1].y = y*50

        #go through every pressure plate
        for button in pressure_plates:
            #if touching a button
            if self.get_rect().colliderect(button.rect):
                #print("Touching a Button")
                button.active = True

                for door in doors:
                    #set door to open
                    door.open = True


    def render(self, colour = (0, 0, 255),collisions = False, blocks = (), players = []):

        #if collisions are enabled (only on players)
        if collisions:
            #check for any collisions
            self.detectCollisions(blocks, players)

        #move the x and y the amount calculated over this frame
        self.x = self.x + self.moveX
        self.y = self.y + self.moveY

        if self.player == 0:
            #draws a rectagle with dimentions of self
            pygame.draw.rect(screen, colour, self.get_rect())
        if self.player == 1:
            # Draws image of player 1 on the screen.
            screen.blit(img_player1, (self.x, self.y))
        elif self.player == 2:
            screen.blit(img_player2, (self.x, self.y))

        #reset movement to 0 for next frame
        self.moveX = 0
        self.moveY = 0

    def jump(self):
        # Force = 1 / 2 * mass * velocity ^ 2
        F  = (1 / 2)* self.mass * (self.velocity**2)

        # change the y value
        self.moveY -= F

        # constantly reduce velocity (therefore making it an arc shaped jump)
        self.velocity = self.velocity-1

        # object reached its maximum height
        if self.velocity < 0:
            # negative sign is added to counter negative velocity
            self.mass = -0.1

        # object is where is began
        if self.velocity == -6:
            #reset mass and velocity now that the jump is finished
            self.mass,self.velocity = 4,5
            self.jumping = False #sprite is no longer jumping
            self.can_jump = False #sprite can not jump right away


# moved here from level_design because it didnt know what sprite was
# DONT USE THIS ONE, USE THE ONE BELOW
# get the location of the player starting position (SPRITE).
def create_player_sprite(current_level):
    for y in range(len(current_level)):
        for x in range(len(current_level[0])):

            if current_level[y][x] == "0":
                Player0 = Sprite(x*50, y*50, 40, 50, 1) #player width and height data is stored here
            if current_level[y][x] == "1":
                Player1 = Sprite(x*50, y*50, 40, 50, 2)
    Players = [Player0,Player1]
    return Players





class Pressure_Plate:
    def __init__(self,rect):
        self.rect = rect
        #self.id = id #unused variable
        self.active = False

    def render(self):
        colour = ()
        #print(self.active)

        #if it is pressed down in this frame
        if self.active:
            #make it green
            colour = (0,100,0)
        else:
            #make it red
            colour = (100,0,0)

        #draw a rectagle where the pressure plate's rect is (red if off, green if on)
        pygame.draw.rect(screen, colour, self.rect)






class Door:
    def __init__(self,rect):
        self.rect = rect #a python rect (x,y,width,hight)
        self.open = False #the door starts closed

    def render(self):
        global current_level

        #if the door is closed
        if self.open == False:
            #draw a rectagle where the door is
            pygame.draw.rect(screen, (255,255,255), self.rect)

            modify_level("/","|") #replace all "/" (open door) with "|" (closed door)
        else: #if the door is open
            modify_level("|","/")#replace all "|" (open door) with "/" (closed door)
