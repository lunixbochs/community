from talon import Context, Module, actions
from talon import ui

key = actions.key

ctx = Context()
ctx.on({'app.bundle': 'com.apple.Safari'})

@ctx.action_class('app')
class AppActions:
    def window_close(): key('cmd-shift-w')
    def tab_reopen():   key('cmd-shift-t')

@ctx.action_class('browser')
class BrowserActions:
    def focus_address():       key('cmd-l')
    def reload():              key('cmd-r')
    def reload_hard():         key('cmd-alt-r')
    def open_private_window(): key('cmd-shift-n')

    def address():
        win = ui.active_window()
        if win:
            child = win.children.find_one(
                {'AXRole': 'AXStaticText', 'AXDescription': 'Address and Search'},
                {'AXRole': 'AXWebArea'},
            )
            if child.AXRole == 'AXWebArea':
                try:
                    url = child.AXURL
                except AttributeError:
                    url = ''
            else:
                url = child.AXValue
            return url
