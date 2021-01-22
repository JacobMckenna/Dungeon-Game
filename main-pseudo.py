
Create FUNCTION main()

    Make objects of the two players (watergirl/fireboy)
    Player1, Player1 = create_player_sprite

    Loop infinitely until user closed window, then break out of loop
        Loop through pygame events
        Check if the event is to quit pygame
        Close window:
            quit pygame
            break out of loop

        Check if the user is in the menu or game
        If in menu:
            Call menu function to handle all the menu functions
            game_state, level = main_menu()
        If in game:
            Call game function to handle all the game functions
            game_state, level = main_menu()
            Check if a new level is reached:
            Level changed:
                Change global level to the new level returned
                Unlock a new level from JSON file
        Not menu or game:
            Not supposed to happen
            quit pygame
            break out of loop

        Update window displayed to the user

        Set how many times to update the sreen to a fixed number
