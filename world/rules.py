from random import randint
from evennia import utils
from evennia import TICKER_HANDLER as tickerhandler

combatlist = []

def can_hit(caller, target):
    if not target:
        caller.msg("Hit whom?")
        return False
    if not utils.inherits_from(target, 'typeclasses.characters.Character'):
        caller.msg("This is not a valid target.")
        return False
    if target == caller:
        caller.msg("You affectionately pat yourself on the back.")
        caller.location.msg_contents("{} affectionately pats themselves on the back.".format(caller.name),
                                     exclude=[caller])
        return False
    else:
        return True

def combat_list(character):
    combatlist.append(character)

def set_fighting(caller, target):
    caller.db.fighting = target
    target.db.fighting = caller
    if caller not in combatlist:
        combatlist.append(caller)
    if target not in combatlist:
        combatlist.append(target)

def do_hit():
    for character in combatlist:
        delay = randint(0,3)
        utils.delay(delay, callback=attack_msg, character=character)
        print combatlist

def attack_msg(character):
    dmg = randint(0, 10)
    character.msg("You strike {} for {} damage".format(character.db.fighting, dmg))
    character.db.fighting.msg("{} strikes you for {} damage".format(character, dmg))


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
        character.db.fighting = None
        tickerhandler.remove(5, skill_combat, persistent=False, idstring=id)
        update_prompt(character)
        return

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
    caller
    target
    roll1, roll2 = roll_hit(), roll_hit()
    failtext = "You are hit by %s for %i damage!"
    wintext = "You hit %s for %i damage!"
    #char1.msg("{} is char1. Their combat score is {}.".format(char1.name,char1.db.skills['combat']))
    #char1.msg("{} is char2. Their combat score is {}.".format(char2.name, char2.db.skills['combat']))
    #char1.msg("Roll1 = {}".format(roll1))
    #char1.msg("Roll2 = {}".format(roll2))
    if caller.db.skills['combat'] >= roll1 > roll2:
        # Char 1 hits
        dmg = roll_dmg() + caller.db.str
        caller.msg(wintext % (target, dmg))
        target.msg(failtext % (caller, dmg))
        target.db.hp['Current'] -= dmg
        check_defeat(target, id)
        update_prompt(target)
    elif target.db.skills['combat'] >= roll2 > roll1:
        # char 2 hits
        dmg = roll_dmg() + target.db.str
        caller.msg(failtext % (target, dmg))
        caller.db.hp['Current'] -= dmg
        check_defeat(caller, id)
        target.msg(wintext % (caller, dmg))
        update_prompt(caller)
    else:
        # draw
        drawtext = "Neither of you can find an opening."
        caller.msg(drawtext)
        target.msg(drawtext)
