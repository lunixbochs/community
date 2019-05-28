from talon import Context, ctrl

ctx = Context()

# Mouse coordinates
x, y = ctrl.mouse_pos()

# Click!
def backdated_click(m, button=0, times=1):
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
def backdated_rightclick(m):
    backdated_click(m, button=1, times=1)

def backdated_dubclick(m):
    backdated_click(m, button=0, times=2)

def backdated_tripclick(m):
    backdated_click(m, button=0, times=3)

# Hold key and click
def hold_key_and_click(m, key, button=0, times=1):
    ctrl.key_press(key, down=True)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    ctrl.key_press(key, up=True)

def shift_click(m, button=0, times=1):
    hold_key_and_click(m, "shift", button, times)

def command_click(m, button=0, times=1):
    hold_key_and_click(m, "cmd", button, times)

# Click and drag
def backdated_drag(m):
    ctrl.mouse_click(x, y, down=True, wait=16000)

def backdated_release(m):
    ctrl.mouse_click(x, y, up=True, wait=16000)

# Scrolling with mouse wheel
def scroll_down(m):
    ctrl.mouse_scroll(200)

def scroll_up(m):
    ctrl.mouse_scroll(-200)

# Voice commands
ctx.commands = {
    'click': backdated_click,
    '(right click | righty)': backdated_rightclick,
    'dub click': backdated_dubclick,
    '(trip click | triplick)': backdated_tripclick,
    '(drag | press | hold)': backdated_drag,
    'release': backdated_release,
    'shift click': shift_click,
    'command click': command_click,
    '(scroll down | wheel down)': scroll_down,
    '(scroll up | wheel up)': scroll_up,
}