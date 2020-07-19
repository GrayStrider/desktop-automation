#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import keyboard as kb
import speech_recognition as sr
from halo import Halo

from routines import commands 
from process_response import process
from util import timestamp

HOTKEY = 'ctrl+alt+shift+f1'

r = sr.Recognizer()

ready = timestamp('Ready')

def main_loop():
    try:
        with sr.Microphone() as source:
            with Halo(text='Awaiting voice input.'):
                audio = r.listen(source)

            with Halo(text='Processing audio..'):
                result = r.recognize_google(audio)

            timestamp(result + '\n')()

            result = process(result, commands)

            if result == '':
                ready()
                return

            kb.write(result + ' ')

            ready()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

ready()
kb.add_hotkey(HOTKEY, main_loop)
# kb.on_press(lambda e: print(e.scan_code))

kb.wait()
