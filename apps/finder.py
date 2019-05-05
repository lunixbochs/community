from talon import Module, actions

key = actions.key

# TODO: how do I tag an app as having specific global actions? tags on a context?
# also need a concept of "app-specific module"
mod = Module()
@mod.action_class
class Actions:
    def duplicate(): key('cmd-d')
    def eject():     key('cmd-e')

    # FIXME: move these to app actions
    def hide():        key('cmd-h')
    def hide_others(): key('cmd-h')

    def hide_toolbar(): key('cmd-alt-t')
    def view_options(): key('cmd-j')
    def connect(): key('cmd-k')
    def alias(): key('cmd-l')
    def info(): key('cmd-i')
    def new_folder(): key('cmd-shift-n')
    def collapse(): key('cmd-left')
    def expand(): key('cmd-right')
    def open(): key('cmd-down')
    def show_original(): key('cmd-r')
    def add_to_sidebar(): key('cmd-t')
    def trash(): key('cmd-backspace')

# actions
"select all": Key("cmd-a"),
"copy": Key("cmd-c"),
"duplicate": Key("cmd-d"),
"eject": Key("cmd-e"),
"(search | find)": Key("cmd-f"),
"hide [finder]": Key("cmd-h"),
"hide (others | else)": Key("cmd-alt-h"),
"(hide | no) toolbar": Key("cmd-alt-t"),
"info": Key("cmd-i"),
"view [options]": Key("cmd-j"),
"connect [to server]": Key("cmd-k"),
"[(make | create)] (alias | shortcut)": Key("cmd-l"),
"minimize": Key("cmd-m"),
"new window": Key("cmd-n"),
"new folder": Key("cmd-shift-n"),
# NOT WORKING "new smart folder": Key("cmd-alt-n"),
"collapse": Key("cmd-left"),
"expand": Key("cmd-right"),
"open": Key("cmd-down"),
"[show] original": Key("cmd-r"),
"add to side bar": Key("cmd-t"),
"trash it": Key("cmd-backspace"),
"new tab": Key("cmd-alt-o"),
"paste": Key("cmd-v"),
"close": Key("cmd-w"),
"cut": Key("cmd-x"),
"undo": Key("cmd-z"),
"[finder] preferences": Key("cmd-,"),
"(icon | icons) [(mode | view)]": Key("cmd-1"),
"list [(mode | view)]": Key("cmd-2"),
"(column | columns) [(mode | view)]": Key("cmd-3"),
"cover [flow] [(mode | view)]": Key("cmd-4"),
"help": Key("cmd-?"),
# navigation
"back": Key("cmd-["),
"(forward | next)": Key("cmd-]"),
"(up | (parent [folder]))": Key("cmd-up"),
"(cycle | switch) [window]": Key("cmd-`"),
"computer": Key("cmd-shift-c"),
"desktop": Key("cmd-shift-d"),
"all files": Key("cmd-shift-f"),
"go to": Key("cmd-shift-g"),
"home": Key("cmd-shift-h"),
"icloud": Key("cmd-shift-i"),
"documents": Key("cmd-shift-o"),
"air drop": Key("cmd-shift-r"),
"utilities": Key("cmd-shift-u"),
"downloads": Key("cmd-shift-l"),
"applications": Key("cmd-shift-a"),
"developer": go_to_path("~/Developer"),
"talon": go_to_path("~/.talon/user"),
# NOT WORKING "(delete | empty) trash": Key("cmd-shift-del"),
"spotlight [menu]": Key("cmd-space"),
"spotlight window": Key("cmd-alt-space"),
# NOT WORKING: Function key shorcuts (f8 through f12)
"toggle hidden files": Key("cmd-shift-."),
