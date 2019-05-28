from talon import Module, Context, actions
from talon import ui
import time
import os

mod = Module()
mod.list('running', desc='all running applications')
mod.list('launch', desc='all launchable applications')

@mod.action_class
class Actions:
    def focus(bundle: str):
        """Focus a new application by bundle name"""
        app = ui.apps(bundle=bundle)
        if app:
            app = app[0]
            app.focus()
            # TODO: replace sleep with a registered callback
            for i in range(25):
                if ui.active_app().bundle == bundle:
                    break
                time.sleep(0.01)
            time.sleep(0.05)

    def launch_app(path: str):
        """Launch a new application by path"""
        ui.launch(path=path)


ctx = Context()
ctx.commands = {
    'focus {self.running}': lambda m: actions.self.focus(m.running),
    'launch {self.launch}': lambda m: actions.selef.launch(m.launch),
}

def update_lists():
    new = {}
    for app in ui.apps():
        if app.background and not app.windows():
            continue
        words = app.name.lower().split(' ')
        for word in words:
            if word and not word in new:
                new[word] = app.bundle
        new[app.name] = app.bundle
    ctx.lists['self.running'] = new

    new = {}
    for base in '/Applications', '/Applications/Utilities':
        for name in os.listdir(base):
            path = os.path.join(base, name)
            name = name.rsplit('.', 1)[0].lower()
            new[name] = path
            words = name.split(' ')
            for word in words:
                if word and word not in new:
                    if len(name) > 6 and len(word) < 3:
                        continue
                    new[word] = path
    ctx.lists['self.launch'] = new

def ui_event(event, arg):
    if event in ('app_activate', 'app_launch', 'app_close', 'win_open', 'win_close'):
        update_lists()

ui.register('', ui_event)
update_lists()