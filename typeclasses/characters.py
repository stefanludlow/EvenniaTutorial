"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from evennia.contrib.rpsystem import ContribRPCharacter
from random import randint

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(player) -  when Player disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Player has disconnected" 
                    to the room.
    at_pre_puppet - Just before Player re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "PlayerName has entered the game" to the room.

    """
    def at_object_creation(self):
        """

        Called at initial object creation.

        """
        # set persistent attributes
        # health, stam, and mp
        self.db.level = 0
        self.db.hp = {'Max': 100, 'Min': 0, 'Current': 100}
        self.db.stam = {'Max': 100, 'Min': 0, 'Current': 100}
        self.db.mp = {'Max': 100, 'Min': 0, 'Current': 100}
        # attributes
        self.db.str = 10
        self.db.dex = 10
        self.db.con = 10
        self.db.int = 10
        self.db.wis = 10
        self.db.chr = 10
        self.db.skills = {  'combat' : randint(1,100),
                            'unarmed' : randint(5,10),
                            'long-blade': randint(5,10 )}

    def get_abilities(self):
        """

        Simple access method to return ability scores

        """
        return self.db.str, self.db.dex, self.db.con, self.db.int, self.db.wis, self.db.chr
