from talon import Module, Context, actions, clip

# slack = actions.apps.slack
edit = actions.edit
insert = actions.insert

mod = Module()

emojis = {
    'thumbs up': ':+1:',
    'okay hand': ':ok_hand',
    'okay': ':ok_hand:',
    'check': ':white_check_mark:',
    'crossed fingers': ':crossed_fingers:',
    'fingers': ':crossed_fingers:',
    'pray': ':pray:',
}

@mod.capture
def emoji(m) -> str:
    """Common Slack emoji"""

# FIXME: move this into the slack app script
ctx = Context()
ctx.on({'app.bundle': 'com.tinyspeck.slackmacgap'})

def react(m):
    emoji = m.emoji[0]
    edit.select_all()
    with clip.capture() as s:
        edit.copy()

    insert(f"+{emoji}\n")
    try:
        insert(s.get())
    except clip.NoChange:
        pass

# TODO: use a mapping list instead?
@ctx.capture(rule='|'.join(emojis.keys()))
def emoji(m):
    return emojis[' '.join(m)]

ctx.commands = {
    'inline <self.emoji>': lambda m: insert(m.emoji[0]),
    'react <self.emoji>': react, # lambda m: slack.react(m.emoji[0]),
}
