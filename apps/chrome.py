from talon import Context, Module, actions

key = actions.key

ctx = Context()
ctx.on({'app.bundle': 'com.google.Chrome'})

@ctx.action_class('app')
class AppActions:
    def window_close(): key('cmd-shift-w')
    def tab_reopen():   key('cmd-shift-t')

@ctx.action_class('browser')
class BrowserActions:
    def focus_url():           key('cmd-l')
    def reload():              key('cmd-r')
    def reload_hard():         key('cmd-shift-r')
    def open_private_window(): key('cmd-shift-n')
