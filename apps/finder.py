from talon import Module, Context, actions

key = actions.key

# TODO: how do I tag an app as having specific global actions? tags on a context?
# also need a concept of "app-specific module"
mod = Module()
@mod.action_class
class Actions:
    def eject():
        """Eject the selected volume"""
        key('cmd-e')

    def toggle_toolbar():
        """Show or hide the Finder toolbar"""
        key('cmd-alt-t')

    def view_options():
        'Open "View Options" dialog'
        key('cmd-j')

    def connect():
        'Open "Connect" dialog'
        key('cmd-k')

    def item_duplicate():
        """Duplicate selected item"""
        key('cmd-d')

    def item_alias():
        """Make an alias of selected item"""
        key('cmd-l')

    def item_info():
        """Show info of selected item"""
        key('cmd-i')

    def item_open():
        """Open selected item"""
        key('cmd-down')

    def item_add_to_sidebar():
        """Add selected item to sidebar"""
        key('cmd-t')

    def item_trash():
        """Move selected item to Trash"""
        key('cmd-backspace')

    def item_show_original():
        """Show the target of selected alias"""
        key('ctrl-cmd-alt-a')

    def new_folder():
        """Create a new folder"""
        key('cmd-shift-n')

    def collapse():
        """Collapse current row"""
        key('cmd-left')

    def expand():
        """Expand current row"""
        key('cmd-right')

    def icon_view():
        'Switch to "Icon" view'
        key('cmd-1')

    def list_view():
        'Switch to "List" view'
        key('cmd-2')

    def column_view():
        'Switch to "Column" view'
        key('cmd-3')

    def cover_flow_view():
        'Switch to "Cover Flow" view'
        key('cmd-4')

    def help():
        'Open "Help" menu'
        key('cmd-?')

    def toggle_hidden_files():
        "Toggle showing hidden files"
        key('cmd-shift-.')

    def go_to(path: str=None):
        "Open the Go To dialog, or go directly to a path"
        key('cmd-shift-g')
        if path is not None:
            actions.insert(path)
            key('enter')

    def go_computer():
        'Open "Computer"'
        key('cmd-shift-c')

    def go_desktop():
        'Open "Desktop"'
        key('cmd-shift-d')

    def go_all_files():
        'Open "All Files"'
        key('cmd-shift-f')

    def go_home():
        'Open "Home Directory"'
        key('cmd-shift-h')

    def go_icloud():
        'Open "iCloud"'
        key('cmd-shift-i')

    def go_documents():
        'Open "Documents"'
        key('cmd-shift-o')

    def go_airdrop():
        'Open "AirDrop"'
        key('cmd-shift-r')

    def go_utilities():
        'Open "Utilities"'
        key('cmd-shift-u')

    def go_downloads():
        'Open "Downloads"'
        key('cmd-shift-l')

    def go_applications():
        'Open "Applications"'
        key('cmd-shift-a')

    def go_talon():
        'Open "~/.talon"'
        actions.self.go_to('~/.talon')

    def go_talon_user():
        'Open "~/.talon/user"'
        actions.self.go_to('~/.talon/user')

ctx = Context()
ctx.on({'app.bundle': 'com.apple.Finder'})

@ctx.action_class('app')
class AppActions:
    def window_close(): key('cmd-shift-w')
    def tab_open():  key('cmd-t')
    def tab_close(): key('cmd-w')
