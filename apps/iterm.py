from talon import Module, Context, actions

key = actions.key
self = actions.self

mod = Module()
@mod.action_class
class Actions:
    def split_horizontal():
        "Split current pane (horizontal)"
        key('cmd-shift-d')
    def split_vertical():
        "Split current pane (vertical)"
        key('cmd-d')
    def pane_next():
        "Go to next pane"
        key('cmd-]')
    def pane_previous():
        "Go to previous pane"
        key('cmd-[')

ctx = Context()
ctx.on({'app.bundle': 'com.googlecode.iterm2'})

ctx.commands = {
    'split horizontal': lambda m: self.split_horizontal(),
    'split vertical': lambda m: self.split_vertical(),
    'pane next': lambda m: self.pane_next(),
    'pane last': lambda m: self.pane_previous(),
}
