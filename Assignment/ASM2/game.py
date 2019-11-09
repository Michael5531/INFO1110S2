# A few import statements to start you off. This is how you can
# access the classes and functions defined in other classes;
# be sure to update this if you choose to create functions that
# are otherwise not imported!
import sys

from creature import Creature
from item import Item
from location import Location
from preprocessing import process_locations, process_exits,\
                          process_items, process_creatures
#==============================================================================================
def read_path(source): #Build up a function reads the file and return into a list which contains unique objects
    f = open(source, "r")
    file_location_read = f.readlines()
    f.close()
    path_list = []
    i = 0
    while i < len(file_location_read):
        if file_location_read[i] == '\n':
            i += 1
            continue
        if file_location_read[i] != '\n':
            path_list.append(file_location_read[i].rstrip("\n").split(" > ")) # data cleaning, remove extra new lines and " > "
        i += 1
    return path_list
#==============================================================================================
if len(sys.argv) < 4:
    print("Usage: python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>")
    sys.exit()
else:
    try:
        file_location = open(sys.argv[1], "r")
        file_item = open(sys.argv[2], "r")
        file_creature = open(sys.argv[3], "r")
        file_exits = open(sys.argv[4], "r")
    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        sys.exit()
    try:
        open(sys.argv[1], "r")
    except FileExistsError:
        print("The game cannot run without any room :(")
        sys.exit()
#==============================================================================================
if len(file_location.readlines()) == 0:
    print("The game cannot run without any rooms :(")
    sys.exit()
if len(file_creature.readlines()) == 0:
    print("There is nothing chasing you!")
    sys.exit()
#==============================================================================================
path = read_path(sys.argv[1])
all_location = process_locations(sys.argv[1])
# goose.position = all_location[0]
all_item = process_items(sys.argv[2], all_location)
all_creature = process_creatures(sys.argv[3], all_location)
goose = Creature('player', 'goose', 5, all_location[0])
#==============================================================================================

#==============================================================================================
process_exits(sys.argv[4], all_location)
goose.position.map_draw()
#==============================================================================================
while True:
    command = input(">> ")
    if command.upper() == "LOOK ME":
        print("You are a goose. You are probably quite terrifying.\nIn fact, you have a terror rating of: {}".format(goose.terror_rating))
        print()
        continue
#==============================================================================================
    elif command.upper() == "INV":
        if len(goose.item_list) == 0:
            print("You are carrying nothing.\n")
        elif len(goose.item_list) == 1:
            print("You, a goose, are carrying the following item:")
            print(" - {}".format(goose.item_list[0].item_name))
            print()
        elif len(goose.item_list) > 1:
            print("You, a goose, are carrying the following items:")
            i = 0
            while i < len(goose.item_list):
                print(" - {}".format(goose.item_list[i].item_name))
                i += 1
            print()
#==============================================================================================
    elif command.upper() == "QUIT":
        print("Game terminated.")
        sys.exit()
    elif command.upper() == "HELP":
        print("""HELP            - Shows some available commands.
INV             - Lists all the items in your inventory.
TAKE <ITEM>     - Takes an item from your current location.
DROP <ITEM>     - Drops an item at your current location.

LOOK or L       - Lets you see the map/location again.
LOOK <ITEM>     - Lets you see an item in more detail.
LOOK ME         - Sometimes, you just have to admire the feathers.
LOOK <CREATURE> - Sizes up a nearby creature.
LOOK HERE       - Shows a list of all items in the room.

NORTHWEST or NW - Moves you to the northwest.
NORTH or N      - Moves you to the north.
NORTHEAST or NE - Moves you to the northeast.
EAST or E       - Moves you to the east.

SOUTHEAST or SE - Moves you to the southeast.
SOUTH or S      - Moves you to the south.
SOUTHWEST or SW - Moves you to the southwest.
WEST or W       - Moves you to the west.

FLEE            - Attempt to flee from your current location.
HONK or Y       - Attempt to scare off all creatures in the same location.
WAIT            - Do nothing. All other creatures will move around you.
QUIT            - Ends the game. No questions asked.\n""")
#==============================================================================================
    elif command.upper() == "FLEE":
        if goose.position.exit_status == False:
            print(goose.position.exit_message())
            continue
        elif goose.position.exit_status == True:
            print(goose.position.exit_message())
            break
#==============================================================================================
    elif command.upper().split(" ")[0] == "DROP":
        drop_sucess = False
        for i in goose.item_list:
            if command.upper().split()[1] == i.short_name.upper():
                goose.drop(i)
                goose.position.add_item(i)
                i.position = goose.position
                goose.terror_rating -= i.terror_rating
                print("You drop the {}.".format(i.item_name))
                print()
                drop_sucess = True
                break
        if drop_sucess == False:
            print("You don't have that in your inventory.\n")
            continue
        elif drop_sucess == True:
            goose.position.chaser_round(all_creature, goose)
#==============================================================================================
    elif command.upper().split(" ")[0] == "TAKE":
        take_sucess = False
        for i in goose.position.item_list:
            if command.upper().split()[1] == i.short_name.upper():
                goose.take(i)
                goose.position.remove_item(i)
                i.position = goose
                goose.terror_rating += i.terror_rating
                print("You pick up the {}.".format(i.item_name))
                print()
                take_sucess = True
                break
        if take_sucess == False:
            print("You don't see anything like that here.\n")
            continue
        elif take_sucess == True:
            goose.position.chaser_round(all_creature, goose)
#==============================================================================================
    elif command.upper() == "SOUTH" or command.upper() == "S":
        if goose.position.south == None:
            print("You can't go that way.\n")
            continue
        goose.position = goose.position.south
        print("You move south, to {}.".format(goose.position.name))
        goose.position.chaser_round(all_creature, goose)
        goose.position.map_draw()
#==============================================================================================
    elif command.upper() == "NORTH" or command.upper() == "N":
        if goose.position.north == None:
            print("You can't go that way.\n")
            continue
        goose.position = goose.position.north
        print("You move north, to {}.".format(goose.position.name))
        goose.position.chaser_round(all_creature, goose)
        goose.position.map_draw()
#==============================================================================================
    elif command.upper() == "EAST" or command.upper() == "E":
        if goose.position.east == None:
            print("You can't go that way.\n")
            continue
        goose.position = goose.position.east
        print("You move east, to {}.".format(goose.position.name))
        goose.position.chaser_round(all_creature, goose)
        goose.position.map_draw()
#==============================================================================================
    elif command.upper() == "WEST" or command.upper() == "W":
        if goose.position.west == None:
            print("You can't go that way.\n")
            continue
        goose.position = goose.position.west
        print("You move west, to {}.".format(goose.position.name))
        goose.position.chaser_round(all_creature, goose)
        goose.position.map_draw()
#==============================================================================================
    elif command.upper() == "NORTHWEST" or command.upper() == "NW":
        if goose.position.northwest == None:
            print("You can't go that way.\n")
            continue
        goose.position = goose.position.northwest
        print("You move northwest, to {}.".format(goose.position.name))
        goose.position.chaser_round(all_creature, goose)
        goose.position.map_draw()
#==============================================================================================
    elif command.upper() == "SOUTHEAST" or command.upper() == "SE":
        if goose.position.southeast == None:
            print("You can't go that way.\n")
            continue
        goose.position = goose.position.southeast
        print("You move southeast, to {}.".format(goose.position.name))
        goose.position.chaser_round(all_creature, goose)
        goose.position.map_draw()
#==============================================================================================
    elif command.upper() == "NORTHEAST" or command.upper() == "NE":
        if goose.position.northeast == None:
            print("You can't go that way.\n")
            continue
        goose.position = goose.position.northeast
        print("You move northeast, to {}.".format(goose.position.name))
        goose.position.chaser_round(all_creature, goose)
        goose.position.map_draw()
#==============================================================================================
    elif command.upper() == "SOUTHWEST" or command.upper() == "SW":
        if goose.position.southwest == None:
            print("You can't go that way.\n")
            continue
        goose.position = goose.position.southwest
        print("You move southwest, to {}.".format(goose.position.name))
        goose.position.chaser_round(all_creature, goose)
        goose.position.map_draw()
#==============================================================================================
    elif command.upper().split()[0] == "LOOK" or command.upper() == "L":
        if len(command.upper().split()) > 1:
            if command.upper().split()[1] == "HERE":
                if len(goose.position.item_list) == 0:
                    print("There is nothing here.\n")
                    continue
                elif len(goose.position.item_list) > 0:
                    i = 0
                    while i < len(goose.position.item_list):
                        print("{:<16}| {}".format(goose.position.item_list[i].short_name.upper(),goose.position.item_list[i].item_name))
                        i += 1
                    print()
                    continue
            else:
                look_success = False
                for i in goose.position.item_list:
                    if command.upper().split()[1] == i.short_name.upper():
                        print("{} - Terror Rating: {}".format(i.item_name,i.terror_rating))
                        print()
                        look_success = True
                        break
                for i in goose.item_list:
                    if command.upper().split()[1] == i.short_name.upper():
                        print("{} - Terror Rating: {}".format(i.item_name,i.terror_rating))
                        print()
                        look_success = True
                        break
                for i in goose.position.creature_list:
                    if command.upper().split()[1] == i.name.upper():
                        if goose.terror_rating + 5 <= i.terror_rating:
                            print("{} doesn't seem very afraid of you.".format(i.name))
                        elif goose.terror_rating - 5 >= i.terror_rating :
                            print("{} looks a little on-edge around you.".format(i.name))
                        else:
                            print("Hmm. {} is a bit hard to read.".format(i.name))
                        print()
                        look_success = True
                        break
                if look_success == False:
                    print("You don't see anything like that here.\n")
                    continue
        else:
            goose.position.map_draw()
#==============================================================================================
    elif command.upper() == "HONK" or command.upper() == "Y":
        if goose.position.creature_list == []:
            print("All shall quiver before the might of the goose! HONK!\n")
            goose.position.chaser_round(all_creature, goose)
            continue
        else:
            print("You sneak up behind your quarry and honk with all the force of a really angry airhorn! HONK!")
            for i in goose.position.creature_list:
                if goose.terror_rating > i.terror_rating:
                    i.position = None
                    goose.position.creature_list.remove(i)
                    print("{} is spooked! They flee immediately!".format(i.name))
                    
                elif goose.terror_rating < i.terror_rating:
                    print("{} is not spooked :(".format(i.name))
            print()
            goose.position.chaser_round(all_creature, goose)
            i = 0
            j = 0
            while j < len(all_creature):
                if all_creature[j].position == None:
                    i += 1
                j += 1
            if len(all_creature) == i:
              print("None can stand against the power of the goose!\n========= V I C T O R Y =========")
              quit()
#==============================================================================================
    elif command.upper() == "WAIT":
        print("You lie in wait.")
        goose.position.chaser_round(all_creature, goose)
        print()
#==============================================================================================
    else:
        print("You can't do that.\n")
        continue

