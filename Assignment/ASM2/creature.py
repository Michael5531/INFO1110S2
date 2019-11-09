"""
TODO: Define the Creature class, as described on page 10 of the assignment
description. You are allowed to change the scaffold somewhat to better suit
the needs of your program (change function parameters, etc.)

You are allowed to create as many methods as you feel are necessary.
"""

class Creature:
    def __init__(self, name, desc, terror_rating, position):
        self.name = name
        self.terror_rating = int(terror_rating)
        self.desc = desc
        self.position = position
        self.item_list = []
        self.counter = 0
        """
        TODO: Constructor; instantiates a Creature class. You may modify
        this constructor so that it can receive additional arguments (or
        fewer arguments).
        """

    def take(self, item):
        return self.item_list.append(item)

    def drop(self, item):
        return self.item_list.remove(item)

    def get_terror_rating(self):
        return self.terror_rating

    def get_chaser_desc(self):
        return self.desc


    # These methods probably aren't enough! You can create more
    # methods here.
