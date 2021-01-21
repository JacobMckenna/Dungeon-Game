Import everythig from global_variables file
Import pygame and initialize it
Import json module


FUNCTION check_mouse(page, music, level, btn_list, mouse_point): Given the mouse positions and a button list, checks if a mouse is inside a button's coordinates, then update page, music, or level.

    Parameters:
    pygame (since not global), screen, music, level, btn_list, mouse_point

    Loop through the button list to check each one
    For every button in btn_list:
        Check if the mouse is inside the button
        If mouse_point is inside coordinates of button:
            Change hovered attribute of button
            self.hovered = True
            Call method clicked() of object button and store the value returned
        If mouse did not hover over the button
            Change hovered attribute of button
            self.hovered = False

    Return the changed variable from the return of method clicked() (tuple)

FUNCTION json_levels(unlocked): Convert level info from JSON to dict
Parameter: unlocked - Whether user unlocked a level.

    Open json file and read the contents -> in a variable
    data = jsonFile

    Check if the user unlocked a new level
    If unlocked is True:
        Change the first 'locked' to 'unlocked'
        Loop through data:
            If level[info] is 'locked':
                level[info] = unlocked

        Write changes to json file
        Open json file and write to it data
        jsonFile.write(data)

    Change the buttons of the 'settings' page
    level_btns()

    Return dictionary containing levels unlocked
    Return data



FUNCTION music_btns(music_dict): Calculate the positions of the music buttons on the settings page
Parameters: music_dict - list of music buttons to generate

    Convert the dictionary to a list
    music_list = list comprehension of dict_dict

    Center the music buttons in the x axis
    x_offset = total_x - (width of all the buttons) / 2
    y_offset = a fixed number, below the title

    Create the buttons
    Loop through music_list:
        Each button will be pushed more to the x besides offset
        add_x = x_offset + fixed number * number of songs passed
        add_y = y_offset

        Add button to list
        index = get index of music_list current music in loop
        button = Button('music', song, etc.)
        music_page.append(button)



FUNCTION level_btns(): Generates the buttons to the level_num
    Get level info in dict format from created function
    data = json_levels()

    Convert dictionary to list
    data_lis = list comprehension of data

    Loop through each row:
        Loop through each button in the row as button:
        If the button is unlocked:
            Make background white and selectable
        If the button is locked:
            Make background grey and not selectable

        add_x = x_offset
        add_y = y_offset



FUNCTION credits_btn():
    credits_list = ['Jacob', 'Joel', 'Omar']

    Center the names in the x and y axis
    x_offset = total_x - (width of all names) / 2
    y_offset = total_y - (height of a name) / 2

    Loop through the credits list:
        index = get index of current name

        Add the extra x push for each name
        add_x = x_offset + fixed number * number of songs passed
        add_y = y_offset

        Add button to list
        index = get index of current name from credits_list
        button = Button('music', song, etc.)
        settings_page.append(button)

        Add button to the page
        button = Button(level, x_add, y_add, etc.)



FUNCTION render_btns(screen, bg_img, btn_list): Draws the bg and buttons to the window.
    Draw the backgounr image to the screen
    screen.draw(bg_img)
    Loop each button and draw to screen:
    For button in btn_list:
        screen.draw(button)
