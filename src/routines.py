import keyboard as kb
from pywinauto.application import Application


title = ".*Timeline.*"
timeline = Application()\
.connect(title_re=title)\
.window(title_re=title)

hourglass = Application()\
.connect(path=r"C:\Program Files (x86)\Hourglass\Hourglass.exe")\
.top_window()

def toggle_comment():
    kb.send('shift+enter')

def timestamp():
    kb.write(',t', delay=0.5)

def new_line():
    kb.send('enter')

def new_time_entry(text):
    timeline.set_focus()


    toggle_comment()
    kb.send('enter')
    timestamp()
    toggle_comment()

def add_time(text):
    timeline.set_focus()

    toggle_comment()
    timestamp()
    toggle_comment()

    if text:
        kb.send('backspace')
        kb.send(39) # semi in qwerty
        kb.send('space')

def stop_timer(text):
    hourglass.set_focus()
    kb.send('ctrl+s')

def start_timer(text):
    hourglass.set_focus()
    kb.send('Enter')  

commands = {
    'new time': new_time_entry,
    'new line': new_line,
    'more time': add_time,
    'stop timer': stop_timer,
    'start timer': start_timer
}