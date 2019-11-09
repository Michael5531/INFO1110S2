"""
TODO: Define the Location class, as described on page 6 of the assignment
description. You are allowed to change the scaffold somewhat to better suit
the needs of your program (change function parameters, etc.)

You are allowed to create as many methods as you feel are necessary.
"""
class Location:
    def __init__(self, name,):
        self.name = name
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.southeast = None
        self.northeast = None
        self.southwest = None
        self.northwest = None
        self.exit_status = False
        self.item_list = []
        self.creature_list = []
        self.creature = None
        self.creature_sign = "C"
#==============================================================================================
    def creature_store(self, creature):
        self.creature_list.append(creature)
#==============================================================================================
    def set_chaser(self, chaser):
        self.chaser = chaser
#==============================================================================================
    def add_item(self, item):
        self.item_list.append(item)
#==============================================================================================
    def remove_item(self, item):
        self.item_list.remove(item)
#==============================================================================================
    def set_path(self, dir, dest):
        if dir.upper() == "NORTH":
            self.north = dest
        if dir.upper() == "WEST":
            self.west = dest
        if dir.upper() == "EAST":
            self.east = dest
        if dir.upper() == "SOUTH":
            self.south = dest
        if dir.upper() == "SOUTHEAST":
            self.southeast = dest
        if dir.upper() == "NORTHEAST":
            self.northeast = dest
        if dir.upper() == "SOUTHWEST":
            self.southwest = dest
        if dir.upper() == "NORTHWEST":
            self.northwest = dest
#==============================================================================================
    def exit_message(self):
        if self.exit_status == False:
            return ("There's nowhere you can run or hide! Find somewhere else to FLEE.\n")
        elif self.exit_status == True:
            return ("You slip past the dastardly Goosechasers and run off into the wilderness! Freedom at last!\n========= F R E E D O M =========")
#==============================================================================================
    def get_item_full_desc(self):
        for i in self.item_list:
            if i.position == self.name:
                short_desc = i.full_desc
            return short_desc
#==============================================================================================
    def get_chaser_full_desc(self):
        for i in self.creature_list:
            if i.position == self.name:
                chaser_desc = i.desc
            return chaser_desc
#==============================================================================================
    def map_draw(self):
        north_position = " "
        north_dash = ""
        nwest_position = ""
        nwest_dash = ""
        neast_position = ""
        neast_dash = ""
        west_position = ""
        west_dash = ""
        east_position = ""
        east_dash = ""
        swest_position = ""
        swest_dash = ""
        south_position= ""
        south_dash = ""
        seast_postion = ""
        seast_dash = ""
        if self.north is not None:
            north_position = "[{}]".format("C" if len(self.north.creature_list) else " ")
            north_dash = '|'
        if self.south is not None:
            south_position = "[{}]".format("C" if len(self.south.creature_list) else " ")
            south_dash = '|'
        if self.east is not None:
            east_position = "[{}]".format("C" if len(self.east.creature_list) else " ")
            east_dash = '-'
        if self.west is not None:
            west_position = "[{}]".format("C" if len(self.west.creature_list) else " ")
            west_dash = "-"
        if self.northeast is not None:
            neast_position = "[{}]".format("C" if len(self.northeast.creature_list) else " ")
            neast_dash = "/"
        if self.northwest is not None:
            nwest_position = "[{}]".format("C" if len(self.northwest.creature_list) else " ")
            nwest_dash = "\\"
        if self.southeast is not None:
            seast_postion = "[{}]".format("C" if len(self.southeast.creature_list) else " ")
            seast_dash = "\\"
        if  self.southwest is not None:
            swest_position = "[{}]".format("C" if len(self.southwest.creature_list) else " ")
            swest_dash = "/"
        print("{:>3}{:>4}{:>4}".format(nwest_position, north_position, neast_position).rstrip())
        print("{:>4}{:>2}{:>2}".format(nwest_dash, north_dash, neast_dash).rstrip())
        print("{:>3}{:>1}[x]{:>1}{:>2}".format(west_position, west_dash, east_dash, east_position).rstrip())
        print("{:>4}{:>2}{:>2}".format(swest_dash, south_dash, seast_dash).rstrip())
        print("{:>3}{:>4}{:>4}".format(swest_position, south_position, seast_postion).rstrip())
        print("You are now at: {}.".format(self.name))
        if len(self.item_list) == 0 and len(self.creature_list) == 0:
            print("There is nothing here.")
        else:
            print_string = ""
            if len(self.item_list) != 0:
                for i in self.item_list:
                    print_string += i.get_short_desc() + " " 
            if len(self.creature_list) != 0:
                for i in self.creature_list:
                    print_string += i.get_chaser_desc() + " " 
            print(print_string.rstrip())
        if self.exit_status == True:
            print("The path to freedom is clear. You can FLEE this place.")
        print()
#==============================================================================================
    def chaser_round(self, creature_list, player):
        player_fail_status = False
        for i in creature_list:
            # print(i.counter)
            # print(self.name)
            if i.position == self.name:
                if i.counter == 0:
                    if i.terror_rating > player.terror_rating:
                        player_fail_status = True
                    else:
                        print()
                        print("{} is trying to catch you!".format(i.name))
                        print("But your presence still terrifies them...")
                        i.counter += 1
                        continue
                if i.counter == 1:
                    player_fail_status = True
                if player_fail_status == True:
                    print("{} is trying to catch you!\nOh no, you've been caught!\n========= GAME OVER =========".format(i.name))
                    quit()
                      
                
        
