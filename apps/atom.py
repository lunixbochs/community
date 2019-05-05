from talon import Context, actions

edit = actions.edit
key = actions.key
insert = actions.insert

ctx = Context()
ctx.on({'app.bundle': 'com.github.atom'})

@ctx.action_class('edit')
class EditActions:
    def save():     key('cmd-s')
    def save_all(): key('cmd-alt-s')
    def undo():     key('cmd-z')
    def redo():     key('cmd-shift-z')
    def cut():      key('cmd-x')
    def copy():     key('cmd-c')
    def paste():    key('cmd-v')
    def delete():   key('backspace')

    # basic selection
    def select_none():  key('right')
    def select_all():   key('cmd-a')
    def select_word():  key('left shift-right left alt-left alt-right shift-alt-left')
    # def select_sentence():
    # def select_paragraph():
    def select_line(n: int=None):
        if n is None:
            key('cmd-left cmd-shift-right')
        else:
            edit.jump_line(n)
            key('cmd-left cmd-shift-right')
    def select_lines(a: int, b: int):
        a, b = min((a, b)), max((a, b))
        edit.jump_line(n)
        for i in range(b):
            key('shift-down')
        key('cmd-shift-right')

    # extending selection
    # def extend_column(n: int):
    # def extend_line(n: int):
    def extend_left():       key('shift-left')
    def extend_right():      key('shift-right')
    def extend_up():         key('shift-up')
    def extend_down():       key('shift-down')
    def extend_file_start(): key('cmd-shift-up')
    def extend_file_end():   key('cmd-shift-down')
    def extend_line_up():    key('shift-left cmd-shift-left')
    def extend_line_down():  key('shift-right cmd-shift-right')
    def extend_line_start(): key('cmd-shift-left')
    def extend_line_end():   key('cmd-shift-right')
    def extend_page_up():    key('cmd-shift-pageup')
    def extend_page_down():  key('cmd-shift-pagedown')
    # def extend_again():

    def extend_word_left():  key('cmd-shift-alt-left')
    def extend_word_right(): key('cmd-shift-alt-right')
    # def extend_sentence_previous():
    # def extend_sentence_next():
    # def extend_sentence_start():
    # def extend_sentence_end():
    # def extend_paragraph_previous():
    # def extend_paragraph_next():
    # def extend_paragraph_start():
    # def extend_paragraph_end():

    # moving cursor
    def jump_column(n: int):
        key('ctrl-g')
        insert(f":{n}")
        key('enter')
    def jump_line(n: int):   
        key('ctrl-g')
        insert(str(n))
        key('enter')
    def left():       key('left')
    def right():      key('right')
    def up():         key('up')
    def down():       key('down')
    def file_start(): key('cmd-up cmd-left')
    def file_end():   key('cmd-down cmd-left')
    def line_start(): key('cmd-left')
    def line_end():   key('cmd-right')
    def line_up():    key('up cmd-left')
    def line_down():  key('down cmd-left')
    def page_up():    key('pageup')
    def page_down():  key('pagedown')
    # def move_again():

    def word_left():  key('alt-left')
    def word_right(): key('alt-right')
    # def sentence_previous():  
    # def sentence_next():      
    # def sentence_start():     
    # def sentence_end():       
    # def paragraph_previous(): 
    # def paragraph_next():     
    # def paragraph_start():    
    # def paragraph_end():      

    # misc actions
    def zoom_in():  key('cmd-+')
    def zoom_out(): key('cmd--')

    def line_insert_up():   key('cmd-shift-enter')
    def line_insert_down(): key('cmd-enter')

    def indent_more(): key('cmd-]')
    def indent_less(): key('cmd-[')

    def delete_line():
        edit.select_line()
        edit.delete()
    def delete_word(): 
        edit.select_word()
        edit.delete()
    # def delete_sentence():
    # def delete_paragraph(): 

    def find(text: str=None): 
        key('cmd-f')
        if text:
            actions.insert(text)
            key('enter')

    def find_next():     key('cmd-g')
    def find_previous(): key('cmd-shift-g')

    def selected_text() -> str:
        key('shift-right')
        with clip.capture() as s:
            key('cmd-c')
        key('shift-left')
        return s.get()[:-1]

@ctx.action_class('code')
class CodeActions:
    def toggle_comment(): key('cmd-/')
