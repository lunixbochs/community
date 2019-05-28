from talon import Module, Context
from talon import actions, ctrl
from talon.scripting import rctx

METAS = ['cmd', 'shift', 'ctrl', 'alt', 'fn']
SPECIALS = {
    '-': 'minus',
    '+': 'plus',
    '\n': 'enter',
    '\t': 'tab',
    ' ': 'space',
}
# allow specifying the separator keys using Key()
REMAP = {'dash': '-', 'minus': '-', 'plus': '+'}

ctx = Context()

@ctx.action_class('main')
class MainActions:
    def insert(text: str):
        for c in str(text):
            c = SPECIALS.get(c, c)
            actions.key(c)

    def key(key: str):
        if key == ' ': key = 'space'
        keys = key.strip().split(' ')

        for key in keys:
            parts = [key]
            if len(key) > 1:
                sep = '-'
                if '+' in key and (not '-' in key or key.index('+') < key.index('-')):
                    sep = '+'
                if sep == '-':
                    if key.endswith('--'):
                        key = key[:-1] + 'dash'
                else:
                    if key.endswith('++'):
                        key = key[:-1] + 'plus'
                parts = key.split(sep)
            metas, key = parts[:-1], parts[-1]
            kwargs = {}
            kwargs.update({k: True for k in metas})
            key = REMAP.get(key, key)
            if not 'wait' in kwargs:
                kwargs['wait'] = 1000
            ctrl.key_press(key, **kwargs)

    def modifiers():
        pass

    def mouse_move(x: int, y: int):
        ctrl.mouse_move(x, y)

    def mouse_click(button: int=0, down: bool=None, up: bool=None, hold: int=None):
        ctrl.mouse_click(button=button)

    def mouse_scroll(y: int=0, x: int=0, by_lines: bool=False):
        ctrl.mouse_scroll(y=y, x=x, by_lines=by_lines)
