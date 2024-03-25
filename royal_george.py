from random import randint
import os

"""
A computergame based on the boardgame Seasbattle
"""

logo = """
.::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.
.:::::  _    _  __  __   _____   _____  ...:::::::::::::...  _  :::::.
.::::: | |  | ||  \/  | / ____| |  __ \   ......:::::...... | | :::::.
.::::: | |__| || \  / || (___   | |__) | ___   _   _   __ _ | | :::::.
.::::: |  __  || |\/| | \___ \  |  _  / / _ \ | | | | / _` || | :::::.
.::::: | |  | || |  | | ____) | | | \ \| (_) || |_| || (_| || | :::::.
.::::: |_|__|_||_|  |_||_____/  |_|  \_\\___/  \__, | \__,_||_| :::::.
 ::::: :/ ____|   .........::::::::::........   __/ |   :::::::::::::.
.::::: | |  __   ___   ___   _ __  __ _   ___  |___/   ::::::::::::::.
.::::: | | |_ | / _ \ / _ \ | '__|/ _` | / _ \  :::::::::::::::::::::.
.::::: | |__| ||  __/| (_) || |  | (_| ||  __/  :::::::::::::::::::::.
 .::::: \_____| \___| \___/ |_|   \__, | \___|  :::::::::::::::::::::.
.:::::::::......................:  __/ |  :::::::::::::::::::::::::::.
::::::::::::....................: |___/   :::::::::::::::::::::::::::.
:::::::::::::::::...........:::..........:::::::::::::::::::::::::::::
:::::::::::::::::::::....:::::::::.:::::::::::::::::::::::::::::::::::
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
def intro():
    print(logo)
    into_text = text_layout(
        "You are the Chief Gunner at the H.M.S. Royal George. You are to give orders to your gunners in the form of coordinates. Good luck on the battles ahead! \n"
    )
    print(into_text)


def press():
    print("Press enter to continue...")
    input()


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def text_layout(text):
    count = 0
    new_text = ""
    for c in text:
        if count > 60 and c.isspace():
            new_text += "\n"
            count = 0
        else:
            new_text += c
            count += 1
    return new_text


# generate the conditions for the current level
class Level_gen:
    def __init__(self, grid_size, cannon_balls, ship_size, text):
        self.grid_size = grid_size
        self.cannon_balls = cannon_balls
        self.ship_size = ship_size
        self.text = text

    # draw level table
    def __repr__(self):
        print("\n" + " Y")
        print(" " * 3, end="")
        print("-" * 4 * self.grid_size + "-")
        for i in range(1, self.grid_size + 1):
            #1 to i on the Y axis
            print(" " + str(i) + " |", end="")
            for j in range(1, self.grid_size + 1):
                print(" ~" + " |",end="")
                # print("-", end="")
            print("\n" + " " * 3, end="")
            for k in range(1, self.grid_size + 1):
                print("-" * 4, end="")
                # print("-", end="")
            print("-")
        print(" " * 3, end="")
        for i in range(1, self.grid_size + 1):
            print("  " + str(i) + " ", end="")
        print("   X")
        return " "


class Ship:
    def __init__(self, ship_size, grid_size):
        self.grid_size = grid_size
        self.ship_size = ship_size
        self.coords = self.generate_coords()

    def __repr__(self):
        return "Enemy ship can be found at {}".format(self.coords)

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

        # check if ship is within bounds of the field
        # a simple solution, in the future it should roll for NESW



class Shoot:
    def __init__(self, ship_coords, cannon_balls):
        self.ship_coords = ship_coords
        self.cannon_balls = cannon_balls

    def __repr__(self):
        return "Cannonballs left: {}".format(self.cannon_balls)

    def Input(self, ship_coords):
        while self.cannon_balls > 0 and ship_coords:
            print("Cannonballs left: {}".format(self.cannon_balls))
            self.usr_input = input(str("X, Y: "))
            self.cannon_balls -= 1
            hit_counter = 0
            hit_coords = 0
            if self.usr_input == "q":
                global game
                game = 0
                print("quit program")
                break
            for x in ship_coords:
                x_string = str(x)
                x_string_clean = self.clean_string(x_string)
                usr_input_clean = self.clean_string(self.usr_input)
                # print(x_string[1:-1])
                if x_string_clean == usr_input_clean:
                    hit_counter = 1
                    hit_coords = x
            if hit_counter == 1:
                print("\n  Hit at {}".format(self.usr_input))
                ship_coords.remove(hit_coords)
                self.cannon_balls += 1
                # print(ship_coords)
            elif hit_counter == 0:
                print("\n  miss!")
        if self.cannon_balls == 0 and ship_coords:
            return "game_over"
            print("test")
        if not ship_coords:
            return "won"
        else:
            return 0
            print("error")

    # remove spaces and brackets from a string
    def clean_string(self, text):
        clean_text_1 = text.replace(" ", "")
        clean_text_2 = clean_text_1.replace(" ", "")
        clean_text_3 = clean_text_2.replace("(", "")
        clean_text_4 = clean_text_3.replace(")", "")
        return clean_text_4


# game data
level_lst = [
    [0, 0, 0, 0, "initiater"],
    [
        1,
        1,
        1,
        1,
        "Februari 1757. Oh no, you thought you were fine in port, but a pirate sloop is attacking. It isn't hard to miss. \n",
    ],
    [
        2,
        3,
        5,
        2,
        "September 1757. At the Raid on Rochefort you are about to be boarded by a French Caravel which is 2 squares long \n",
    ],
    [
        3,
        4,
        7,
        3,
        "20 November 1759. In the Battle of Quiberon Bay it is up to HMS Royal George as the flagship of the fleet to prevent a landing on our homeland. Ahead there is a French galleon, which is 3 squares long \n",
    ],
]

final_text = "\n 28 August 1782. Well done Ser, your cannons and skilled interventions have keps us alive! After a well deserved rest at the Spithead port in Gibraltar we will set off on a final voyage home... \n"

game = True
lvl = 1

# before the gameplay loop
cls()
intro()
press()
cls()

# gameplay loop
while game:

    # end game when out of levels
    if lvl >= len(level_lst):
        cls()
        print(victory)
        print(text_layout(final_text))
        game = False
        break

    # Populates level data from level_lst
    level_generated = Level_gen(
    
        level_lst[lvl][1], level_lst[lvl][2], level_lst[lvl][3], level_lst[lvl][4]
    )

    # dynamic map generator
    print(level_generated)

    # level introduction flavour text
    print(text_layout(level_generated.text))

    # create enemy
    enemy = Ship(level_generated.ship_size, level_generated.grid_size)

    # cheats
    print(enemy)

    # create self
    self = Shoot(enemy.coords, level_generated.cannon_balls)

    evaluation = self.Input(enemy.coords)
    if evaluation == "game_over":
        cls()
        print(loss)
        print(
            "You lost, the enemy ship sailed at coordinates " + str(enemy.coords) + "\n"
        )
        game = 0
    elif evaluation == "won":
        print("You won the battle! \n")
        lvl += 1
        press()
        cls()


"""
Pseudo code

at start:

intro

generate levels (map_size, ship_quantity, ship_position, cannon_balls)
level loop:
  run level 1
    show grid and text
    generate ships (size, coords)
    generate self

"""
