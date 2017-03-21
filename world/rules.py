from random import randint
from evennia import utils
from evennia import TICKER_HANDLER as tickerhandler

def roll_hit():
    "Roll 1d100"
    return randint(1, 100)

def roll_dmg():
    "Roll 1d6"
    return randint(1,6)

def check_defeat(character, id):
    "Checks if a character is 'defeated'."
    if character.db.hp['Current'] <= 0:
        character.msg("You fall down, defeated!")
        character.db.hp['Current'] = character.db.hp['Max']
        #TODO need to fix the below line, as the tickerhandler doesn't actually remove itself
        tickerhandler.remove(15, skill_combat, idstring=id)

def update_prompt(character):
    prompt = ("HP: {} Stam: {} MP: {}".format(character.db.hp['Current'], character.db.stam['Current'],
                                              character.db.mp['Current']))
    character.msg(prompt=prompt)

def skill_combat(caller, target, id):
    """
    This determines outcome of combat.
    The one who rolls under theri combat skill AND
    higher than their opponent's roll hits.
    Args:
        *args:

    Returns:

    """
    char1 = caller
    char2 = target
    char1.msg(id)
    # char1 , char2 = args
    roll1, roll2 = roll_hit(), roll_hit()
    failtext = "You are hit by %s for %i damage!"
    wintext = "You hit %s for %i damage!"
    #char1.msg("{} is char1. Their combat score is {}.".format(char1.name,char1.db.skills['combat']))
    #char1.msg("{} is char2. Their combat score is {}.".format(char2.name, char2.db.skills['combat']))
    #char1.msg("Roll1 = {}".format(roll1))
    #char1.msg("Roll2 = {}".format(roll2))
    if char1.db.skills['combat'] >= roll1 > roll2:
        # Char 1 hits
        dmg = roll_dmg() + char1.db.str
        char1.msg(wintext % (char2, dmg))
        char2.msg(failtext % (char1, dmg))
        char2.db.hp['Current'] -= dmg
        check_defeat(char2, id)
        update_prompt(char2)
    elif char2.db.skills['combat'] >= roll2 > roll1:
        # char 2 hits
        dmg = roll_dmg() + char2.db.str
        char1.msg(failtext % (char2, dmg))
        char1.db.hp['Current'] -= dmg
        check_defeat(char1, id)
        char2.msg(wintext % (char1, dmg))
        update_prompt(char1)
    else:
        # draw
        drawtext = "Neither of you can find an opening."
        char1.msg(drawtext)
        char2.msg(drawtext)
