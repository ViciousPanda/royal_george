from random import randint
import os
import sys

"""
A computergame based on the boardgame Seasbattle
"""

# assets

empty = ""

logo = """
.::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.
.:::::  _    _  __  __   _____   _____  ...:::::::::::::::.  _  :::::.
.::::: | |  | ||  \/  | / ____| |  __ \   ......:::::...... | | :::::.
.::::: | |__| || \  / || (___   | |__) | ___   _   _   __ _ | | :::::.
.::::: |  __  || |\/| | \___ \  |  _  / / _ \ | | | | / _` || | :::::.
.::::: | |  | || |  | | ____) | | | \ \| (_) || |_| || (_| || | :::::.
.::::: |_|__|_||_|  |_||_____/  |_|  \_\\___/  \__, | \__,_||_| :::::.
.::::: :/ ____|   .........::::::::::........   __/ |   :::::::::::::.
.::::: | |  __   ___   ___   _ __  __ _   ___  |___/   ::::::::::::::.
.::::: | | |_ | / _ \ / _ \ | '__|/ _` | / _ \  :::::::::::::::::::::.
.::::: | |__| ||  __/| (_) || |  | (_| ||  __/  :::::::::::::::::::::.
.:::::: \_____| \___| \___/ |_|   \__, | \___|  :::::::::::::::::::::.
.:::::::::.....................::  __/ |  :::::::::::::::::::::::::::.
::::::::::::::::::::::::::::::::: |___/   :::::::::::::::::::::::::::.
:::::::::::::::::::::::::::::::::.......::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::.:::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::.::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::-::::::=-:::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::=*%#::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::=%%@#::::+#%*::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::=:=%=-::=+##*::-:::::::::::::::::::::::::::
::::::::::::::::::::==-::::+%%%#=::=*#%%*+*=::::::::::::::::::::::::::
:::::::::::::::::::::==:::=%%%%%=:=#%%%%**#=::::::::::::::::::::::::::
::::::::::::::::::-*%@%=::+=+@@#=:===#%***#*::::::::::::::::::::::::::
::::::::::::::::::=@@@%+::=+*##**==++*#*#%%%=+::::::::::::::::::::::::
::::::::::::::::::-%%%%%=-+**++**+=**++**%%%%+::::::::::::::::::::::::
:::::::::::::::::::::+#@%**%*++**==**++*%%***+::::::::::::::::::::::::
:::::::::::::::::::::+%@@@@@@@%#%*===***%%+*##-:::::::::::::::::::::::
=====================-===#@@@@@@@@@@@@@@@@@@@@*===-===================
%%%%%%##%%%#%%###%##****#**@@@@@@@@%%%%%#%%@%**++******##**###%%%%#%%%
@@%@@@@@@%%%@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@%@@@@
%@@@@@@%@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

victory = """
.........::...........................................................
......-@***%@@*:......................................................
.....*#*#%**+@@@@%%@@@@@@@@#@@@@@%@%@%%#@@@@%%#@+.....................
....=@@#*#@@*-%@%##%@@******@#**%*#%@@@%#**@#****@@@..................
....@@#**@@@@-=#@#*++@%******%+**+=-=@**#%@@@=---:@@%:................
...:@@***@@@@*.*@%: .@*      .%      @##@%%@# %*.:=@@@................
...:@@@@@@@@@*.*@*=-=@*  .:::=@+***##@@@@@@@@%@%%%#@@%................
....@@@@@@@@@-=#@@**%@@****#@@#**%@@@@%@@@@@@@%@@@@@%%%=..............
....=@@**#@@*.#@%%@@@@@@@@@@@%@@@@@@@@#@@@%%####%%%#%%%%:.............
.....#@%@@%*=%@@@@@@%%@@@@@%@@@@@@@@@@#@@@%#%%#%%####%##@@@@@#. ......
......=@%%%%#@%-......%@@@@@@@@@@@%%@@#@@@@@@@@@@%###%###%@%%#*%*%....
.........=+:..........%@@@@@@@@@@%%#@@#@@@%%%%%%@@@@@@%#%@#@#@%#%@%...
.....................@@@@@@@@@@@@#%#@@#@@@@@@@@%%#%%%@@@@@*%@%%##@@-..
....................%@@@@@@@@@%%##%#@@#@@@**@*%@@*@@%@@@@%@#@%@@%@@-..
....................%@@%@@@@@%%#%###@@#@@#*@%@%##@@@%:..:@@@@@%#%@%...
....................%@@@@@@@%%%%%##*@@#@%#@*@%#%##@@@.....@@@@@@%@:...
....................:@@@@@@@@@@%%##%@@#@@%%@@%@#*#@@@......-*@@%=.....
......................%@@@@@=.....:+@@%@%@@@@@@@%#@%@.................
........................................@@@@@@@@@@@%:.................
.........................................%@@@@@@@%@-..................
............................................=%@@@-....................
"""

loss = """
----------------------------------------------------------------------
-----------------------------------------------------+=---------------
--------------------------------------------------=-+#=---------------
----------------------------------------------------=%++=-------------
-------------------------------------------------=*++=----------------
-----------------------------------------+*####%@@@%*==---------------
-------------------------------------------+%@#*%##-=-----------------
--------------------------------------------==%#==+=------------------
----==-=-----------------------------------=+%#=-==-------------------
-----=+#+=---------------------------------+#++=--==------------------
-------=###=-----------------------------=%%======--------------------
-------=++*@@*=----------------------=%@@@@%@@@%+=*%**=---------------
-------====##@@%+---------------------+@@@@@@%+=---=------------------
----------==+@@@%@@#+==--------------=#@**@*%#------------------------
-----------==##@@@@@@@@#=-----------=@%%++%=++------------------------
-------------*=*%@@@@@@@@@*==------*@%+%======------------------------
-------------=--+@@@%%@@@@@@@*-=--#@**+%==--=-------------------------
----------------=%@@@%*+*%@@@@@@+@@+===*=+-=--------------------------
----------------=+%@@@@@%###%@@@@@@#======----------------------------
------------------#@@@@%%%%%%%%%@@@@@@*===----------------------------
------------------=@@@@@@@@@%%%%%%%@@@@@@#==--------------------------
-------------------=%@@@@@@@@@@@%%%%%%@@@@@@+=------------------------
--------------------+@@@@@@@@@@@@@%@@@@@@@@@@@%*=---------------------
-----------------=====%@@@@@@@@@@@@@@@@@@@@@@@@@@@+=------------------
---==+++++++***##%###%#*#%%@@@@@@@@@@%#**#####%@@@@@%+----------------
---=+#*******##########%######*#**######******#%%%%%#%#=--------------
-------======+*#******#***###*****#############%%%#####---------------
----------=+****++++*+***+***************+************+=--------------
------------============------=======------=========------------------
"""

# game instructions and intro

intro_text = "You are the Chief Gunner at the H.M.S. Royal George. You are to give orders to your gunners in the form of coordinates. Good luck on the battles ahead!"
level_1_text = "Februari 1757. Oh no, you thought you were fine in port, but a pirate sloop is attacking. It isn't hard to miss."
level_2_text = "September 1757. At the Raid on Rochefort you are about to be boarded by a French Caravel which is 2 squares long"
level_3_text = "20 November 1759. In the Battle of Quiberon Bay it is up to HMS Royal George as the flagship of the fleet to prevent a landing on our homeland. Ahead there is a French galleon, which is 3 squares long"
level_4_text = ""
victory_text = "28 August 1782. Well done Ser, your cannons and skilled interventions have keps us alive! After a well deserved rest at the Spithead port in Gibraltar we will set off on a final voyage home..."


# press q to exit game
def quit_game(user_input):
    user_input = str(user_input).lower()
    if user_input == "q":
        Draw.cls(self)
        GameState.game = False
        print("quit program")
        sys.exit(0)


# draw Draws to screen and ask for input
class Draw:
    usr_input = ""

    def __init__(self, intro_image="", intro_text="", hit_text="", cannons=0, need_input=False):
        self.intro_image = intro_image
        self.intro_text = intro_text
        self.hit_text = hit_text
        self.cannons = cannons
        self.need_input = need_input

    def __repr__(self):
        return '[Draw %r, %r, %r, %r, %r]' % (self.intro_image, self.intro_text, self.hit_text, self.cannons, self.need_input)

    def draw_screen(self):
        self.cls()
        # image or map
        print(self.intro_image)

        # introduction text
        print(self.text_layout(self.intro_text) + '\n')

        # hit indicator
        print(self.text_layout(self.hit_text) + '\n')

        # cannonball tracker
        if self.cannons > 0:
            print(self.text_layout("you have {} shots left".format(self.cannons)))

        '''
        Debug cheats
        if self.cannons > 0:
            print('\n' + str(enemy.coords) + '\n')
        '''

        # ask for feedback
        self.user_input()

    def user_input(self):
        if not self.need_input:
            print("Press enter to continue...")
            input()
        else:
            Draw.usr_input = input("X, Y: ")

    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")

    def text_layout(self, old_text):
        count = 0
        new_text = ""
        for c in old_text:
            if count > 60 and c.isspace():
                new_text += "\n"
                count = 0
            else:
                new_text += c
                count += 1
        return new_text


# generate the map for the current level
class Map_gen:

    def __init__(self):
        self.rendered_map = ""

    def __str__(self):
        return self.rendered_map

    def draw_map(self, grid_size):
        self.grid_size = grid_size
        self.rendered_map = ""
        self.rendered_map += ('\n' + " Y" + '\n')
        self.rendered_map += (" " * 3)
        self.rendered_map += ("-" * 4 * self.grid_size + "-" + '\n')
        for i in range(1, self.grid_size + 1):
            # 1 to i on the Y axis
            self.rendered_map += (" " + str(i) + " |")
            for j in range(1, self.grid_size + 1):
                self.rendered_map += (" ~" + " |")
            self.rendered_map += ("\n" + " " * 3)
            for k in range(1, self.grid_size + 1):
                self.rendered_map += ("-" * 4)
            self.rendered_map += ("-" + '\n')
        self.rendered_map += (" " * 3)
        for i in range(1, self.grid_size + 1):
            self.rendered_map += ("  " + str(i) + " ")
        self.rendered_map += ("   X" + '\n')
        return self.rendered_map
    
    def fill_map(self, grid_size, hit_coords, miss_coords):
        


# generate enemies
class Ship:
    def __init__(self, ship_size, grid_size, ship_quantity=1):
        self.grid_size = grid_size
        self.ship_size = ship_size
        self.ship_quantity = ship_quantity
        self.coords = self.generate_coords()

    def __repr__(self):
        return '[Ship %r, %r, %r, %r]' % (self.grid_size, self.ship_size, self.ship_quantity, self.coords)

    def generate_coords(self):
        generated_coords = []
        # populate first coords
        r_x = randint(1, ((self.grid_size + 1) - self.ship_size))
        r_y = randint(1, self.grid_size)

        for i in range(0, self.ship_size):
            paired = (r_x, r_y)
            generated_coords.append(paired)
            r_x += 1
        return generated_coords


# check if player input was a hi orr miss and track score
class Shoot:
    def __init__(self, ship_coords):
        self.ship_coords = ship_coords
        self.usr_input = str(Draw.usr_input)

    def __repr__(self):
        return '[Shoot %r, %r]' % (self.ship_coords, self.usr_input)

    def hit_calculation(self):
        while GameState.cannon_balls > 0 and self.ship_coords:
            GameState.cannon_balls -= 1
            hit_counter = 0
            hit_coords = 0
            self.usr_input = str(Draw.usr_input)
            quit_game(self.usr_input)

            for x in self.ship_coords:
                x_string = str(x)

                x_string_clean = self.clean_string(x_string)
                usr_input_clean = self.clean_string(self.usr_input)
                if x_string_clean == usr_input_clean:
                    hit_counter = 1
                    hit_coords = x
            if hit_counter == 1:
                hit_text = "Hit at {}".format(self.usr_input)
                self.ship_coords.remove(hit_coords)
                GameState.cannon_balls += 1
            elif hit_counter == 0:
                hit_text = "Miss at {}".format(self.usr_input)

            if GameState.cannon_balls == 0 and self.ship_coords:
                return False
            elif not self.ship_coords:
                return True
            else:
                draw_map_size = map.draw_map(lvl.map_size)
                draw_level_text = GameState.level_text
                # draw_level_text = str(self.ship_coords)
                draw_cannon_balls = GameState.cannon_balls
                update = Draw(draw_map_size, draw_level_text,
                              hit_text, draw_cannon_balls, True)
                quit_game(update.draw_screen())

    # remove spaces and brackets from a string

    def clean_string(self, text):
        clean_text_1 = text.replace(" ", "")
        clean_text_2 = clean_text_1.replace(" ", "")
        clean_text_3 = clean_text_2.replace("(", "")
        clean_text_4 = clean_text_3.replace(")", "")
        return clean_text_4


# keep track of levels and game data
class GameState:
    game = True
    lvl_lst = {1: {'map_size': 1, 'cannon_balls': 1, 'ship_size': 1, 'ship_quantity': 1, 'intro_text': level_1_text},
               2: {'map_size': 3, 'cannon_balls': 5, 'ship_size': 2, 'ship_quantity': 1, 'intro_text': level_2_text},
               3: {'map_size': 4, 'cannon_balls': 7, 'ship_size': 3, 'ship_quantity': 1, 'intro_text': level_3_text},
               4: {'map_size': 5, 'cannon_balls': 11, 'ship_size': 4, 'ship_quantity': 1, 'intro_text': "initiater"}
               }
    levels = len(lvl_lst)
    cannon_balls = 0
    map_size = 0
    level_text = ""

    def __init__(self, level=1):
        self.level = level
        GameState.cannon_balls = GameState.lvl_lst[self.level]['cannon_balls']
        GameState.map_size = GameState.lvl_lst[self.level]['map_size']
        self.ship_size = GameState.lvl_lst[self.level]['ship_size']
        self.ship_quantity = GameState.lvl_lst[self.level]['ship_quantity']
        GameState.level_text = GameState.lvl_lst[self.level]['intro_text']

    def __repr__(self):
        rep = "Level: {}, Map size: {}, Cannonballs: {}, Ship size: {}. Ship #: {}".format(
            self.level, self.map_size, GameState.cannon_balls, self.ship_size, self.ship_quantity)
        return rep

    def next_level(self):
        self.level += 1
        GameState.cannon_balls = GameState.lvl_lst[self.level]['cannon_balls']
        GameState.map_size = GameState.lvl_lst[self.level]['map_size']
        self.ship_size = GameState.lvl_lst[self.level]['ship_size']
        self.ship_quantity = GameState.lvl_lst[self.level]['ship_quantity']
        GameState.level_text = GameState.lvl_lst[self.level]['intro_text']


# before the gameplay loop
# Initial screen
intro = Draw(logo, intro_text, "", 0, False)
intro.draw_screen()

# create level and map objects
lvl = GameState()
map = Map_gen()

# gameplay loop
while GameState.game:
    # create enemies
    enemy = Ship(lvl.ship_size, lvl.map_size, lvl.ship_quantity)

    # create map
    map.draw_map(lvl.map_size)

    # draw screen and input
    update = Draw(map, lvl.level_text, "", lvl.cannon_balls, True)
    quit_game(update.draw_screen())

    # calculate hit
    self = Shoot(enemy.coords)
    won = self.hit_calculation()

    if lvl.level >= lvl.levels:
        update = Draw(victory, "", victory_text, 0, False)
        update.draw_screen()
        GameState.game = False
        break
    elif won:
        lvl.next_level()
    else:
        update = Draw(loss, "", "Tragically, you have sunk", 0, False)
        update.draw_screen()
        GameState.game = False
        break


'''

Questions:
1: Should I track data in class objects or in class globals?

2: can I use def __str__(self): in Map_gen to draw the game map?

3: should I make classes or functions for things like Map_gen that doesn't need any classobjects to work with, or is it smart to future / feature proof like that?


'''
