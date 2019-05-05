from talon import Module, Context, actions

key = actions.key
self = actions.self

mod = Module()
@mod.action_class
class Actions:
    def email_reply():
        "Reply to email"
        key('cmd-r')
    def email_send():
        "Send current email"
        key('cmd-enter')
    def pane_next():
        "Go to next pane"
        key('shift-ctrl-[')
    def pane_previous():
        "Go to previous pane"
        key('shift-ctrl-]')

ctx = Context()
ctx.on({'app.bundle': 'com.microsoft.Outlook'})

ctx.commands = {
    'reply to email': lambda m: self.email_reply(),
    'send email':     lambda m: self.email_send(),
    'next pain':      lambda m: self.pane_next(),
    'preev pain':     lambda m: self.pane_previous(),
    # 'dismiss outlook',
}
