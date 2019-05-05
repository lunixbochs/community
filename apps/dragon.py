from talon import Module
from talon import applescript, ctrl

mod = Module()
@mod.action_class
class Actions:
    def open_dragon_pad():
        "Open DragonPad"
        old = ctrl.mouse_pos()
        x = applescript.run("""
        tell application "System Events" to tell process "Dragon" to tell (menu bar item 1 of menu bar 2)
            set AppleScript's text item delimiters to ", "
            position as string
        end tell
        """)
        x, y = map(int, x.split(", "))
        ctrl.mouse(x, y)
        ctrl.mouse_click()
        ctrl.mouse(*old)
        applescript.run("""
        tell application "System Events" to tell process "Dragon" to tell (menu bar item 1 of menu bar 2)
            click menu item "Help" of menu 1
            click menu item "DragonPad" of menu of menu item "Help" of menu 1
        end tell
        """)
