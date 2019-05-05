from talon import Module, Context, actions

key = actions.key
self = actions.self

mod = Module()
@mod.action_class
class Actions:
    def highlight():
        "FIXME: Highlight what?"
        key('cmd-ctrl-h')
    def note():
        "FIXME: Note what?"
        key('cmd-ctrl-n')

ctx = Context()
ctx.on({'app.bundle': 'com.apple.Preview'})

ctx.commands = {
    'highlight': lambda m: self.highlight(),
    'note': lambda m: self.note(),
}
