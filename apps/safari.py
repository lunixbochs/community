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
            search_box = win.children.find(AXRole='AXStaticText', AXDescription='Address and Search')
            if not search_box:
                search_box = win.children.find(AXIdentifier='WEB_BROWSER_ADDRESS_AND_SEARCH_FIELD')
            url = search_box[0].AXValue
            return url
