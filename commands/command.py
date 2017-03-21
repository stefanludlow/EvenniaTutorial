"""
Commands

Commands describe the input the player can do to the game.

"""

from evennia import Command as BaseCommand
from evennia import TICKER_HANDLER as tickerhandler
from evennia import utils

from world import rules


# from evennia import default_cmds


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_command(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_command(): Extra actions, often things done after
            every command, like prompts.

    """
    pass

#------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
#------------------------------------------------------------

#from evennia.utils import utils
#class MuxCommand(Command):
#    """
#    This sets up the basis for a MUX command. The idea
#    is that most other Mux-related commands should just
#    inherit from this and don't have to implement much
#    parsing of their own unless they do something particularly
#    advanced.
#
#    Note that the class's __doc__ string (this text) is
#    used by Evennia to create the automatic help entry for
#    the command, so make sure to document consistently here.
#    """
#    def has_perm(self, srcobj):
#        """
#        This is called by the cmdhandler to determine
#        if srcobj is allowed to execute this command.
#        We just show it here for completeness - we
#        are satisfied using the default check in Command.
#        """
#        return super(MuxCommand, self).has_perm(srcobj)
#
#    def at_pre_cmd(self):
#        """
#        This hook is called before self.parse() on all commands
#        """
#        pass
#
#    def at_post_cmd(self):
#        """
#        This hook is called after the command has finished executing
#        (after self.func()).
#        """
#        pass
#
#    def parse(self):
#        """
#        This method is called by the cmdhandler once the command name
#        has been identified. It creates a new set of member variables
#        that can be later accessed from self.func() (see below)
#
#        The following variables are available for our use when entering this
#        method (from the command definition, and assigned on the fly by the
#        cmdhandler):
#           self.key - the name of this command ('look')
#           self.aliases - the aliases of this cmd ('l')
#           self.permissions - permission string for this command
#           self.help_category - overall category of command
#
#           self.caller - the object calling this command
#           self.cmdstring - the actual command name used to call this
#                            (this allows you to know which alias was used,
#                             for example)
#           self.args - the raw input; everything following self.cmdstring.
#           self.cmdset - the cmdset from which this command was picked. Not
#                         often used (useful for commands like 'help' or to
#                         list all available commands etc)
#           self.obj - the object on which this command was defined. It is often
#                         the same as self.caller.
#
#        A MUX command has the following possible syntax:
#
#          name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#        The 'name[ with several words]' part is already dealt with by the
#        cmdhandler at this point, and stored in self.cmdname (we don't use
#        it here). The rest of the command is stored in self.args, which can
#        start with the switch indicator /.
#
#        This parser breaks self.args into its constituents and stores them in the
#        following variables:
#          self.switches = [list of /switches (without the /)]
#          self.raw = This is the raw argument input, including switches
#          self.args = This is re-defined to be everything *except* the switches
#          self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                     no = is found, this is identical to self.args.
#          self.rhs: Everything to the right of = (rhs:'right-hand side').
#                    If no '=' is found, this is None.
#          self.lhslist - [self.lhs split into a list by comma]
#          self.rhslist - [list of self.rhs split into a list by comma]
#          self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#          All args and list members are stripped of excess whitespace around the
#          strings, but case is preserved.
#        """
#        raw = self.args
#        args = raw.strip()
#
#        # split out switches
#        switches = []
#        if args and len(args) > 1 and args[0] == "/":
#            # we have a switch, or a set of switches. These end with a space.
#            switches = args[1:].split(None, 1)
#            if len(switches) > 1:
#                switches, args = switches
#                switches = switches.split('/')
#            else:
#                args = ""
#                switches = switches[0].split('/')
#        arglist = [arg.strip() for arg in args.split()]
#
#        # check for arg1, arg2, ... = argA, argB, ... constructs
#        lhs, rhs = args, None
#        lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#        if args and '=' in args:
#            lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#            lhslist = [arg.strip() for arg in lhs.split(',')]
#            rhslist = [arg.strip() for arg in rhs.split(',')]
#
#        # save to object properties:
#        self.raw = raw
#        self.switches = switches
#        self.args = args.strip()
#        self.arglist = arglist
#        self.lhs = lhs
#        self.lhslist = lhslist
#        self.rhs = rhs
#        self.rhslist = rhslist
#
#        # if the class has the player_caller property set on itself, we make
#        # sure that self.caller is always the player if possible. We also create
#        # a special property "character" for the puppeted object, if any. This
#        # is convenient for commands defined on the Player only.
#        if hasattr(self, "player_caller") and self.player_caller:
#            if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                # caller is an Object/Character
#                self.character = self.caller
#                self.caller = self.caller.player
#            elif utils.inherits_from(self.caller, "evennia.players.players.DefaultPlayer"):
#                # caller was already a Player
#                self.character = self.caller.get_puppet(self.session)
#            else:
#                self.character = None
#
class CmdScore(Command):
    """
    Generic score command

    Usage:
        score

    Displays a list of your current ability values
    """
    key = "score"
    aliases = ["score"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        "implements the actual functionality"
        self.caller.msg("HP: {} Stam: {} MP: {}".format(self.caller.db.hp['Current'], self.caller.db.stam['Current'], self.caller.db.mp['Current']))
        self.caller.msg("Str: {} Dex: {} Con: {} Int: {} Wis: {} Chr: {}".format(self.caller.db.str, self.caller.db.dex,
                                                                                 self.caller.db.con, self.caller.db.int,
                                                                                 self.caller.db.wis, self.caller.db.chr))

class UpdatePrompt(Command):
    """
    Update your prompt

    Usage:
        update
    """
    key = "update"
    aliases = ['prompt']
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        prompt = ("HP: {} Stam: {} MP: {}".format(self.caller.db.hp['Current'], self.caller.db.stam['Current'], self.caller.db.mp['Current']))
        self.caller.msg(prompt=prompt)
        #note, the original SOI prompt which I might want is: <****** / ||||||>



class CmdWound(Command):
    """
    Generic wound command

    Usage:
        wound <target>

    Damages the target's hp.
    """
    key = "wound"
    aliases = ["wound"]
    lock = "cmd:all()"
    help_category = "General"

    def parse(self):
        "parses the args to be the target"
        self.target = self.args.strip()

    def func(self):
        "implements the actual functionality"
        caller = self.caller
        target = caller.search(self.target)
        if not target:
            return
        if not utils.inherits_from(target, 'typeclasses.characters.Character'):
            caller.msg("This is not a valid target.")
            return
        if target.db.hp['Current'] > target.db.hp['Min']:
            target.msg("{} wounds you!".format(caller.name))
            caller.msg("You wound {}!".format(target.name))
            target.db.hp['Current'] = target.db.hp['Current'] - 10
            caller.msg("{}'s HP has been reduced by 10 and is now {}. Their max is {}".format(target.name, target.db.hp['Current'], target.db.hp['Max']))
            caller.location.msg_contents("{} wounds {}!".format(caller.name, target.name), exclude=[caller,target])
        else:
            caller.msg("That would kill him!")

class CmdHit(Command):
    """
    Generic hit command

    Usage:
        hit <target>

    Begins combat with the target
    """
    key = "hit"
    aliases = ["hit,kill"]
    lock = "cmd:all()"
    help_category = "General"

    def parse(self):
        "parses the args to be the target"
        self.target = self.args.strip()

    def func(self):
        "implements the actual functionality"
        caller = self.caller
        target = caller.search(self.target)
        # Beginning of the validation checks
        if not target:
            caller.msg("Hit whom?")
            return
        if not utils.inherits_from(target, 'typeclasses.characters.Character'):
            caller.msg("This is not a valid target.")
            return
        if target == caller:
            caller.msg("You affectionately pat yourself on the back.")
            caller.location.msg_contents("{} affectionately pats themselves on the back.".format(caller.name), exclude=[caller])
            return
        tickerhandler.add(15, rules.skill_combat, caller=caller, target=target, persistent=False, idstring="combatticker")
        #rules.skill_combat(caller, target)

        # End of validation checks

"""
        target.msg("{} attacks you!".format(caller.name))
        caller.msg("You attack {}!".format(target.name))
        # target.db.hp = target.db.hp - 10
        caller.location.msg_contents("{} attacks {}!".format(caller.name, target.name), exclude=[caller,target])
        in_combat = True
        target_delay = 5
        caller_delay = 5
        counter = 0
        while in_combat == True and caller.db.hp > 0 and target.db.hp > 0 and counter < 10:
            utils.delay(target_delay, callback=CmdHit.target_strike())
            #utils.delay(caller_delay, callback=caller.target_strike)
            counter = counter + 1
            if counter >= 10:
                break

    def target_strike(self):
        "Actually does the striking"
        roll = random.randint(1,20)
        if roll > 10:
            caller.location.msg_contents("{} strikes {}".format(target.name, caller.name))
        else:
            caller.location.msg_contents("{} misses {}".format(target.name, caller.name))
"""




