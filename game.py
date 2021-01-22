#Jacob Mckenna, Joel Harder, Omar El Mabrouk
#Due Jan 22, 2021
#game.py
#Handles any key presses and drawing to the screen.

# Import local modules.
from global_variables import *
from level_design import *


def check_events(events):
    """
    Loops through the events and determines their type.

    Parameters
    ----------
    events : list
        Holds all the pygame events that occurred since last frame.

    Returns
    -------
    key_list : list
        List of pressed/not pressed keys.

    """

    global key_list

    # Loop through all the events since last frame.
    for event in events:

        # If a key was just pressed down.
        if event.type == pygame.KEYDOWN:
            # Check which key was pressed.

            if event.key == pygame.K_w: #w
                # Make player 1 jump.
                key_list[0] = True
            if event.key == pygame.K_a: #a
                # Make player 1 move left.
                key_list[1] = True
            if event.key == pygame.K_d: #d
                # Make player 1 move right.
                key_list[2] = True
            if event.key == pygame.K_UP: #up
                # Make player 2 jump.
                key_list[3] = True
            if event.key == pygame.K_LEFT: #left
                # Make player 2 move left.
                key_list[4] = True
            if event.key == pygame.K_RIGHT: #right
                # Make player 2 move right.
                key_list[5] = True

        # If a key was just let go.
        if event.type == pygame.KEYUP:
            # Check which key was let go.

            if event.key == pygame.K_w: #w
                # Make player 1 stop jumping.
                key_list[0] = False
            if event.key == pygame.K_a: #a
                # Make player 1 stop moving left.
                key_list[1] = False
            if event.key == pygame.K_d: #d
                # Make player 1 stop moving right.
                key_list[2] = False
            if event.key == pygame.K_UP: #up
                # Make player 2 stop jumping.
                key_list[3] = False
            if event.key == pygame.K_LEFT: #left
                # Make player 2 top moving left.
                key_list[4] = False
            if event.key == pygame.K_RIGHT: #right
                # Make player 2 stop moving right.
                key_list[5] = False


    # Return a list of all significant keys (either True or False for each)
    return key_list



def main_game(events, level_num, Player0, Player1):
    """
    Calls the smaller functions to handle various parts of the game.

    Parameters
    ----------
    events : list
        Holds all the pygame events that occurred since last frame.
    level_num : int
        Number representing the current level the user is on.
    Player0 : Sprite object
        Represents player 1.
    Player1 : Sprite object
        Represents player 2.

    Returns
    -------
    List
        Returns state of the game (in progress or finished) and level unlocked.

    """

    global key_list

    # Draws the stone brick background.
    draw_stone_background()

    # Check for any events this frame.
    key_list = check_events(events)

    ###########
    # JUMPING #
    ###########

    # If user is pressing "w".
    if key_list[0] == True and Player0.can_jump == True:
        # Make player 0 jump.
        Player0.jump()
    # Not pressing w, apply gravity.
    else:
        Player0.moveY = Player0.moveY + 5

    # If user is pressing "up".
    if key_list[3] == True and Player1.can_jump == True:
        # Make player 1 jump
        Player1.jump()
    # Not pressing w, apply gravity.
    else:
        Player1.moveY = Player1.moveY + 5

    ############
    # CONTROLS #
    ############

    # Apply movement depending on the key pressed.

    # Player 0
    if key_list[1] == True: #pressing a
        Player0.moveX = Player0.moveX - 5 #move left
    elif key_list[2] == True: #pressing d
        Player0.moveX = Player0.moveX + 5 #move right

    # Player 1
    if key_list[4] == True: #pressing left
        Player1.moveX = Player1.moveX - 5 #move left
    elif key_list[5] == True: #pressing right
        Player1.moveX = Player1.moveX + 5 #move right

    # Render the obstacles to the screen.
    blocks = render_level(current_level, level_num)

    # Put player objects in a list for easier access.
    players = [Player0, Player1]

    # Render the players in the map.
    Player0.render((0,0,255),True, blocks, players)
    Player1.render((255,0,0),True, blocks, players)

    # Render the buttons and doors
    for plate in blocks[3]:
        plate.render()
    for door in blocks[4]:
        door.render()

    # Check if both players are standing on the exit.
    if Player0.left_level and Player1.left_level:
        # Reset players' positions and state.
        reset_players(current_level, [Player0, Player1])
        Player0.left_level, Player1.left_level = False, False

        # Reset key list.
        for i in range(0,len(key_list)):
            key_list[i] = False

        # Return that user finished the level, send back.
        return ['menu', level_num + 1]

    # Return that the user is still in the game.
    return ['game', level_num]
