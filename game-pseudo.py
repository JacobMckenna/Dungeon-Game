Import global_variables

FUNCTION check_events(events)
    Loop through the events
        Check if the event type is keydown
        True:
            Check if key pressed is inside list of available keys
            True:
                set index of current key in list to True
        Check if the event type is keyup
        True:
            Check if key up is inside list of available keys
            True:
                set index of current key in list to False

    Return key_list


Main game function
FUNCTION main_game():

    Draw the background
    draw_background()

    Set key_list to the return of check_events(events)

    Check which key the user pressed:

    'w' and player can jump (from attribute):
        Player1.jump()
    Else:
        subtract y by fixed number to simulate gravity

    'up arrow' and player can jump (from attribute):
        Player2.jump()
    Else:
        subtract y by fixed number to simulate gravity

    'a':
        Subtract a fixed number from x coordinate
    'd':
        Add a fixed number to x coordinate
    'left key':
        Subtract a fixed number from x coordinate
    'right key':
        Add a fixed number to x coordinate

    Render the blocks (obstacles, door, etc.)
    set blocks to return of render_level

    Render players to screen
    Player1.render()
    Player2.render()

    Render pressure plates
    Loop through each plate in list
        plate.render()

    Render doors
    Loop through each door in list
        door.render()

    Check if both players reached the exit
    True:
        reset_players()
        Reset keys to not pressed
        set values in key_list to False using list comprehension
        Return ['menu', level]

    Return ['game', level]
