from creature import Creature
from item import Item
from location import Location

#-----------------------------------------process_locations-----------------------------------------------------------#
def process_locations(source): #Build up a function reads the file and return into a list which contains unique objects
    f = open(source, "r")
    file_location = f.readlines()
    f.close()
    store_list = []
    object_store = []
    object_list_use = []
    i = 0
    while i < len(file_location):
        if file_location[i] == '\n':
            i += 1
            continue
        if file_location[i] != '\n':
            store_list.append(file_location[i].rstrip("\n").split(" > ")) # data cleaning, remove extra new lines and " > "
        i += 1
    j = 0
    while j < len(store_list):
        if store_list[j][0].rstrip() not in object_store:
            object_store.append(store_list[j][0].rstrip())
        if store_list[j][2].rstrip() not in object_store:
            object_store.append(store_list[j][2].rstrip())
        j += 1
    k = 0
    while k < len(object_store):
        location_obj = Location(object_store[k])
        object_list_use.append(location_obj)
        k += 1
    z = 0
    while z < len(store_list):
        p = 0
        while p < len(object_list_use):
            if store_list[z][0].rstrip() == object_list_use[p].name:
                m = 0
                while m < len(object_list_use):
                    if object_list_use[m].name == store_list[z][2].rstrip():
                        object_list_use[p].set_path(store_list[z][1].upper(), object_list_use[m])
                    m += 1
            p += 1
        z += 1
    return object_list_use
#-------------------------- ---------------process_items-----------------------------------------------------------#
def process_items(source, locations):
    item_obj_list = []
    item_obj_use = []
    item_tmp = []
    f = open(source, "r")
    file_item = f.read().splitlines()
    f.close()
    for i in file_item:
        item_tmp.append(i.split(" | "))
    for i in item_tmp:
        if len(i) > 1:
            obj_item = Item(i[0], i[1], i[2], i[3], i[4])
            item_obj_list.append(obj_item)
    for i in locations:
        for k in item_obj_list:
            if i.name == k.position:
                item_obj_use.append(k)
                i.add_item(k)
    return item_obj_use
#-----------------------------------------process_creatures-----------------------------------------------------------#
def process_creatures(source, locations):
    creature_obj_list = []
    f = open(source, "r")
    file_creature = f.read().splitlines()
    f.close()
    for i in file_creature:
        tmp_creature = i.split(" | ")
        creature_obj = Creature(tmp_creature[0], tmp_creature[1], tmp_creature[2], tmp_creature[3])
        for loc in locations:
            if loc.name == creature_obj.position:
                creature_obj_list.append(creature_obj)
                loc.creature_store(creature_obj)
    return creature_obj_list
#-----------------------------------------process_exits-----------------------------------------------------------#
def process_exits(source, locations):
    f = open(source, "r")
    file_exits = f.read().splitlines()
    f.close()
    i = 0
    while i < len(file_exits):
        j = 0
        while j < len(locations):
            if locations[j].name == file_exits[i]:
                locations[j].exit_status = True
            j += 1
        i += 1
