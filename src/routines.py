import keyboard as kb
from pywinauto.application import Application
from threading import Timer
import datetime
import re

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

def note(res): 
    timeline.set_focus()

def start_timer_next(text):
    time = datetime.datetime.now()
    minute, second = (time.minute % 10), time.second

    if minute >= 5: 
        minute = 10 - (minute + 1)
    else:
        minute = 5 - (minute + 1)

    OFFSET = 3
    second = 60 - second + OFFSET

    total = (minute * 60) + second

    print(f'Timer will start in {minute}m {second}s from now')
    timer = Timer(total, start_timer, [text])
    timer.start()

def capitalize(text):
    return re.sub('^(.)', lambda m: m[0].upper(), text)

commands = {
    'new time': new_time_entry,
    'new line': new_line,
    'more time': add_time,
    'stop timer': stop_timer,
    'start timer next': start_timer_next,
    'timeline': note,
    'capitalize': capitalize
}