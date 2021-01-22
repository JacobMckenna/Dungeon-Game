Import global variables

Make a dictionary of file paths for background images of pages intro, settings, help, credits

Make a dictionary of file paths for music of songs coffindance, polka, avengers, none

Set starting music to 'coffin'

Make a dictionary of button lists for pages of intro, settings, help, credits

Set starting page to 'intro'

Call functions that automatically create some buttons
music_btns()
level_btns()
credits_btns()

Main menu function
FUNCTION main_menu():

    Call function to render the list of buttons to the screen
    render_btns(page[current page index])

    Check if the mouse is placed on a button
    set new_info to the return of check_mouse(mouse position)

    Loop through the pygame events

        Check if the mouse was clicked
        Clicked:
            Check if new_info contains 'Game'
            True:
                Return to main() in main.py updated game state (game)

            Change updated info from new_info
            set current_page to new_info[page]
            set new_level to new_info[level]

            Check if new music is different than current
            Is different:
                set current_music to new_info[music]

                Check if new_info[music] is equal to 'none'
                True:
                    pause all pygame music
                False:
                    play the new song from the music dictionary
        Player is still in menu
        Return menu, new_level
