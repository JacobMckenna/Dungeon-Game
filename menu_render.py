
# Import local modules.
from button import *
from global_variables import *
import json


# Check if the user's mouse is hovered on a button.
def check_mouse(pygame, screen, page, music, level, btn_list, mouse_point):
    """
    Checks if the user's mouse is hovered on a button then determines the type of button then adjusts page/music/level appropriately.

    Parameters
    ----------
    pygame : module
        Pygame module used to draw the objects.
    screen : pygame surface
        Window where objects are drawn on.
    page : string
        Current page in the menu the user is looking at.
    music : string
        Current song that is playing.
    level : string
        Current selected level.
    btn_list : list
        List of buttons to loop through to check if hovered/clicked.
    mouse_point : tuple
        Coordinates (x, y) of mouse relative to the window.

    Returns
    -------
    list
        Returns the updated page, music, and level selection.

    """

    # Initalize the variable to avoid error.
    changed = [page, music, level]

    # Loop through buttons on the screen.
    for btn in btn_list:

        # Check if the mouse is on top of the button.
        if btn.collidepoint(mouse_point):

            # Change attribute to hover (for colour change).
            btn.hovered = True

            # Handle the action of the button and store the updated settings.
            changed = btn.clicked(page, music, level)

        # Mouse is not on the current button.
        else:
            btn.hovered = False

    return changed


# Get level info from json file.
def json_levels(unlocked = False):
    """
    Get level completion info from JSON file. Convert the data to dicitonary and return.

    Parameters
    ----------
    unlocked : boolean
        Whether a user unlocked a new level.

    Returns
    -------
    dict
        Information for levels unlocked.

    """

    # Open json file and store the contents as a dictionary.
    with open('./assets/json/levels.json') as file:
        data = json.load(file)

    # If users leveled up.
    if unlocked:

        # Check first locked level then change the level to unlocked.
        for key, value in data.items():
            if value['completed'] == False:
                data[key]['completed'] = True
                break

        # Write changes to json file.
        with open('levels.json', 'w') as file:
            json.dump(data, file, indent = 2)

        # Update level selection.
        level_btns()

    return data


def music_btns(music_dict):
    """
    Calculate the x and y coordinates of the each music button and add to the list to draw later.

    Parameters
    ----------
    music_dict : dict
        Dictionary of the music that contains the song's name and file path.

    Returns
    -------
    None
    """

    # Get the names of the songs in a list using list comprehension.
    music_list = [key for key in music_dict]

    # By how much the buttons are pushed to the right.
    # Half of screen and subtract half of the width of the buttons and spaces between them to center them.
    x_offset = SCREEN_DIMEN[0] / 2 - (len(music_list) * 150 - 20) / 2
    # How far the buttons are from the top.
    y_offset = 170

    # Loop through the buttons to create them.
    for ind in range(len(music_list)):

        # Buttons are placed along the x axis.
        x_add = x_offset +  150 * ind
        y_add = y_offset

        # Add the button to the button list.
        song = music_list[ind]
        btn_music = Button(song.capitalize(), "music", song, True, x_add, y_add, 130, 40, (25, 25, 25), (200, 200, 200), 24)

        page_btns['settings'].append(btn_music)





# Generates the choose level buttons with their correct positions.
def level_btns():
    """
    Creates objects of class Button that relate to level selection then appends to list.

    Returns
    -------
    None
    """

    # Returns nested lists from a list given with split length.
    def split_list(lis, n):
        # Store the rows to display to the screen.
        table = []

        # Get every 3rd index.
        for i in range(0, len(lis), n):
            # Store the next n levels of the current index.
            row = lis[i : i+n]
            table.append(row)

        return table


    # Get levels completed info as a dictionary.
    data = json_levels()

    # Make a list out of the data using list comprehension.
    data_lis = [level for level in data]

    # Delete buttons that were created
    del page_btns['settings'][13:len(data_lis)]

    # Split data to x columns and y rows.
    columns = split_list(data_lis, 2)
    rows = split_list(columns, 3)


    # Start generating buttons.

    # Find the x and y offsets from the screen.
    x_offset = SCREEN_DIMEN[0] / 2 - (len(columns[0]) * 320 - 40) / 2
    y_offset = 300

    # Keep track of levels in the loop.
    lvl_count = 0

    # Loop through each row.
    for y in range(len(rows[0])):
        # Loop through each button in the row.
        for x in range(len(rows[0][y])):

            lvl_count += 1

            # If the level is unlocked, make bg white and button selectable.
            if data[str(lvl_count)]['completed'] == True:
                state = "Choose"
                bg = (200, 200, 200)
                hover = True
                type = 'level'

            # If the level is locked, make bg grey and button not selectable.
            elif data[str(lvl_count)]['completed'] == False:
                state = "Locked"
                bg = (150, 150, 150)
                hover = False
                type = ''

            x_add = x_offset + 320 * x
            y_add = y_offset + 110 * y

            # Text in the button.
            num = lvl_count

            btn_lvl = Button(f'{num} - {state}', type, lvl_count, hover, x_add, y_add, 280, 80, (25, 25, 25), bg, 30)
            page_btns['settings'].append(btn_lvl)


# Function to center the names on the credits page.
def credits_btn():
    """
    Center the names in the x and y axis on the credits page.

    Returns
    -------
    None
    """

    # List of names to render to the screen.
    credits_list = ["Jacob McKenna", "Joel Harder", "Omar Mabrouk"]

    # Center the buttons.
    # Half of screen and subtract half of the width of the buttons and spaces between them to center them.
    x_offset = SCREEN_DIMEN[0] / 2 - (len(credits_list) * 260 - 10) / 2
    y_offset = SCREEN_DIMEN[1] / 2 - 30

    # Loop through the names in the credits.
    for ind in range(len(credits_list)):

        # Name of author in this loop.
        name = credits_list[ind]

        # Push buttons to the right to account for button widths.
        x_add = x_offset +  260 * ind
        y_add = y_offset

        # Create an object from class Button.
        btn_credit = Button(name, "", "", False, x_add, y_add, 250, 60, (0, 100, 0), (200, 200, 200), 40)

        # Append object to list to render.
        page_btns['credits'].append(btn_credit)



# Render the background and buttons to the screen.
def render_btns(pygame, screen, bg_img, btn_list):
    """
    Render/draw the background and the buttons to the given screen.

    Parameters
    ----------
    pygame : module
        Pygame game module.
    screen : pygame surface
        Window that objects are drawn to.
    bg_img : string
        File path to the background image.
    btn_list : list
        List of buttons for the current page.

    Returns
    -------
    None
    """

    # Fill background colour.
    screen.fill((0,0,0))
    # Add bg image.
    screen.blit(bg_img, (0,0))

    # Loop throuh buttons to draw them.
    for btn in btn_list:
        # Draw button to screen.
        btn.render()



# Stores button attributes for each page.
# Arguments: Button(text, type, click, can_hover, x, y, w, h, colour, bg, font)
page_btns = {

# Page: Intro.
"intro": [
    Button("Start ", "page", "settings", True, 325, 600, 350, 100, (25, 25, 25), (200, 200, 200), 72)
    ],

# Page: Settings.
"settings": [
    # Title
    Button("Settings", "", "", False, 370, 10, 260, 80, (225, 225, 225), (30, 30, 30), 64),

    # Music
    Button("Choose", "", "", False, 390, 110, 75, 40, (240, 240, 240), (177, 19, 0), 50),
    Button("music:", "", "", False, 530, 110, 75, 40, (240, 240, 240), (33,106,179),  50),
    # Music buttons are added with the music_btns() function in start.py.

    # Levels
    Button("Choose", "", "", False, 390, 230, 75, 40, (240, 240, 240), (177, 19, 0), 50),
    Button("level:", "", "", False, 530, 230, 75, 40, (240, 240, 240), (33,106,179),  50),
    # Level buttons are added with the level_btns() function in start.py.

    # Bottom
    Button("Play Game", "main", "", True, 400, 675, 200, 60, (25, 25, 25), (200, 200, 200), 40),
    Button("Help", "page", "help", True, 630, 675, 125, 60, (25, 25, 25), (200, 200, 200), 38),
    Button("Credits", "page", "credits", True, 240, 675, 125, 60, (25, 25, 25), (200, 200, 200), 38),
    Button("Back", "page", "intro", True, 460, 750, 80, 30, (25, 25, 25), (200, 200, 200), 24)
    ],

# Page: Help.
"help": [
    # Title
    Button("Help", "", "", False, 370, 10, 260, 70, (225, 225, 225), (30, 30, 30), 64),

    # Fireboy controls.
    Button("Fireboy", "", "", False, 150, 140, 200, 55, (200, 200, 200), (177, 19, 0), 60),
    Button("w - jump", "", "", False, 150, 220, 200, 55, (200, 200, 200), (177, 19, 0), 40),
    Button("a - left", "", "", False, 150, 280, 200, 55, (200, 200, 200), (177, 19, 0), 40),
    Button("d - right", "", "", False, 150, 340, 200, 55, (200, 200, 200), (177, 19, 0), 40),
    Button("Don't touch water", "", "", False, 150, 420, 200, 55, (200, 200, 200), (177, 19, 0), 40),
    Button("Reach the exit", "", "", False, 150, 500, 200, 55, (200, 200, 200), (177, 19, 0), 40),

    # Watergirl
    Button("Watergirl", "", "", False, 650, 140, 200, 55, (200, 200, 200), (33,106,179), 60),
    Button("up arrow - jump", "", "", False, 650, 220, 200, 55, (200, 200, 200), (33,106,179), 40),
    Button("left arrow - left", "", "", False, 650, 280, 200, 55, (200, 200, 200), (33,106,179), 40),
    Button("right arrow - right", "", "", False, 650, 340, 200, 55, (200, 200, 200), (33,106,179), 40),
    Button("Don't touch fire", "", "", False, 650, 420, 200, 55, (200, 200, 200), (33,106,179), 40),
    Button("Reach the exit", "", "", False, 650, 500, 200, 55, (200, 200, 200), (33,106,179), 40),

    # Bottom
    Button("Back", "page", "settings", True, 400, 675, 200, 60, (25, 25, 25), (200, 200, 200), 50)
    ],

# Page: Credits.
"credits": [
    # Title
    Button("Credits", "", "", False, 370, 10, 260, 70, (225, 225, 225), (30, 30, 30), 44),

    # Credit buttons are added with the credit_btns() function in start.py.

    # Bottom
    Button("Back", "page", "settings", True, 400, 675, 200, 60, (25, 25, 25), (200, 200, 200), 50),
    ]
}
