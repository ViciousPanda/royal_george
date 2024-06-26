from random import randint
from assets import img_victory, img_logo, img_loss, text
import os
import sys

"""
Royal George: a console base computergame based on the boardgame Seabattle



# game instructions and intro
intro_text = "You are the Chief Gunner at the H.M.S. Royal George. You are to give orders to your gunners in the form of coordinates. Good luck on the battles ahead!"
level_1_text = "Februari 1757. Oh no, you thought you were fine in port, but a pirate sloop is attacking. It isn't hard to miss."
level_2_text = "September 1757. At the Raid on Rochefort you are about to be boarded by a French Caravel which is 2 squares long"
level_3_text = "20 November 1759. In the Battle of Quiberon Bay it is up to HMS Royal George as the flagship of the fleet to prevent a landing on our homeland. Ahead there is a French galleon, which is 3 squares long"
level_4_text = ""
victory_text = "28 August 1782. Well done Ser, your cannons and skilled interventions have keps us alive! After a well deserved rest at the Spithead port in Gibraltar we will set off on a final voyage home..."

"""

# press q to exit game


def quit_game(user_input):
    user_input = str(user_input).lower()
    if user_input == "q":
        cls()
        GameState.game = False
        print("Quit program" + '\n')
        sys.exit(0)


# clear screen
def cls():
    os.system("cls" if os.name == "nt" else "clear")


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
        cls()
        # image or map
        print(self.intro_image)

        # introduction text
        print(self.text_layout(self.intro_text) + '\n')

        # hit indicator
        print(self.text_layout(self.hit_text) + '\n')

        # cannonball tracker
        if self.cannons > 0:
            print(self.text_layout(
                "you have {} shots left".format(self.cannons)) + '\n')

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
            quit_game(input())
        else:
            Draw.usr_input = input("X, Y: ")

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
    hit_data = {}

    def __init__(self):
        self.rendered_map = ""

    def __str__(self):
        return self.rendered_map

    def populate_hit_data(self, grid_size):
        Map_gen.hit_data = {}
        length = grid_size
        hit_lst = []
        hit_dict = {}
        for i in range(1, length + 1):
            for j in range(1, length + 1):
                hit_lst.append("~")
            hit_dict[i] = hit_lst
            hit_lst = []
        Map_gen.hit_data.update(hit_dict)

    def draw_map(self, grid_size):
        temp_hit_data = Map_gen.hit_data.copy()
        # print(temp_hit_data)
        self.rendered_map = ""
        self.rendered_map += ('\n' + " Y" + '\n')
        self.rendered_map += (" " * 3)
        self.rendered_map += ("-" * 4 * grid_size + "-" + '\n')
        for key, value in temp_hit_data.items():
            # print(value)
            self.rendered_map += (" " + str(key) + " |")
            for i in range(len(value)):
                self.rendered_map += (" " + value[i] + " |")
            self.rendered_map += ("\n" + " " * 3)
            for j in range(len(value)):
                self.rendered_map += ("-" * 4)
            self.rendered_map += ("-" + '\n')
        self.rendered_map += (" " * 3)
        for i in range(1, grid_size + 1):
            self.rendered_map += ("  " + str(i) + " ")
        self.rendered_map += ("   X" + '\n')
        return self.rendered_map

    @staticmethod
    def update_hit(x, y):
        upd_hit_dict = Map_gen.hit_data.copy()
        for key, value in upd_hit_dict.items():
            if key == int(y):
                value[int(x) - 1] = "X"
                upd_hit_dict[key] = value
        Map_gen.hit_data.update(upd_hit_dict)

    @staticmethod
    def update_miss(x, y):
        upd_miss_dict = Map_gen.hit_data.copy()
        for key, value in upd_miss_dict.items():
            print(key, y)
            if int(key) == int(y):
                print("now")
                value[int(x) - 1] = "O"
                upd_miss_dict[key] = value
        Map_gen.hit_data.update(upd_miss_dict)


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
            input_check = True
            number_check = []
            for i in range(1, 100):
                number_check.append(str(i))

            while input_check:
                self.usr_input = str(Draw.usr_input)
                quit_game(self.usr_input)
                print(self.usr_input)
                check = self.usr_input.split(',')
                if check[0] in number_check and check[1] in number_check:
                    input_check = False
                else:
                    print('Wrong input')
                    GameState.game = False
                    sys.exit(0)

            for x in self.ship_coords:
                x_string = str(x)
                x_string_clean = self.clean_string(x_string)
                usr_input_clean = self.clean_string(self.usr_input)
                input_xy = usr_input_clean.split(",")
                # print(input_xy)
                if x_string_clean == usr_input_clean:
                    hit_counter = 1
                    hit_coords = x
            if hit_counter == 1:
                Map_gen.update_hit(input_xy[0], input_xy[1])
                hit_text = "Hit at {}".format(self.usr_input)
                self.ship_coords.remove(hit_coords)
                GameState.cannon_balls += 1
            elif hit_counter == 0:
                Map_gen.update_miss(input_xy[0], input_xy[1])
                hit_text = "Miss at {}".format(self.usr_input)

            if GameState.cannon_balls == 0 and self.ship_coords:
                return False
            elif not self.ship_coords:
                return True
            else:
                map = Map_gen()
                draw_map = map.draw_map(GameState.map_size)
                draw_level_text = GameState.level_text
                draw_cannon_balls = GameState.cannon_balls
                update = Draw(draw_map, draw_level_text,
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
    lvl_lst = {1: {'map_size': 1, 'cannon_balls': 1, 'ship_size': 1, 'ship_quantity': 1, 'intro_text': text.level_1_text},
               2: {'map_size': 3, 'cannon_balls': 5, 'ship_size': 2, 'ship_quantity': 1, 'intro_text': text.level_2_text},
               3: {'map_size': 4, 'cannon_balls': 7, 'ship_size': 3, 'ship_quantity': 1, 'intro_text': text.level_3_text},
               4: {'map_size': 5, 'cannon_balls': 11, 'ship_size': 4, 'ship_quantity': 1, 'intro_text': "placeholder"}
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


def main():
    # before the gameplay loop
    # Initial screen
    intro = Draw(img_logo.logo(), text.intro_text, "Press Q to quit", 0, False)
    intro.draw_screen()

    # create level and map objects
    lvl = GameState()
    map = Map_gen()

    # gameplay loop
    while GameState.game:
        # create enemies
        enemy = Ship(lvl.ship_size, lvl.map_size, lvl.ship_quantity)

        # create map
        map.populate_hit_data(lvl.map_size)
        map.draw_map(lvl.map_size)

        # draw screen and input
        update = Draw(map, lvl.level_text, "", lvl.cannon_balls, True)
        quit_game(update.draw_screen())

        # calculate hit
        self = Shoot(enemy.coords)
        won = self.hit_calculation()

        if lvl.level >= lvl.levels:
            update = Draw(img_victory.victory(), "",
                          text.victory_text, 0, False)
            update.draw_screen()
            GameState.game = False
            break
        elif won:
            lvl.next_level()
        else:
            update = Draw(img_loss.loss(), "",
                          "Tragically, you have sunk", 0, False)
            update.draw_screen()
            GameState.game = False
            break


if __name__ == "__main__":
    main()

'''

Questions:
1: Should I track data in class objects or in class globals?

2: can I use def __str__(self): in Map_gen to draw the game map?

3: should I make classes or functions for things like Map_gen that doesn't need any classobjects to work with, or is it smart to future / feature proof like that?

4: what order should the classes and functions be for readability?

'''
