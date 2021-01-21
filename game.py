from global_variables import *
from level_design import *

def check_events(events):

    global key_list
    #check all events that happened in this frame
    for event in events:

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


    #return a list of all significant keys (either True or False for each)
    return key_list



def main_game(events, level_num, Player0, Player1):
    global key_list
    #draws the stone brick background
    draw_stone_background()

    #check for any events this frame
    key_list = check_events(events)

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
    blocks = render_level(current_level, level_num)
    players = [Player0, Player1]

    #render the players in the map
    Player0.render((0,0,255),True, blocks, players)
    Player1.render((255,0,0),True, blocks, players)

    #render the buttons and doors
    for button in pressure_plates:
        button.render()
    for door in doors:
        door.render()

    if Player0.left_level and Player1.left_level: #if both are standing in exit
        print("Travelling to level",level_num + 1)
        Player0,Player1 = reset_players(current_level)
        return ['menu', level_num + 1]

    return ['game', level_num]
