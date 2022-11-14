# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:49:49 2022

@author: Austin
"""
import random
import time
import threading
from kivy.app import App
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class WidgetExample(BoxLayout):
    my_text = StringProperty('Start')
    def on_button_click(self):
        # Start a new thread. Be aware of creating new thread every time you press the button.
        # In which case you need to keep a reference or track the created thread.
        threading.Thread(target = self.do_button_click).start()

    def do_button_click(self):
        for i in range(1,11):
            number = random.randint(1,9)
            print(number)
            self.my_text = str(number)
            
            if number == 1:
                self.play_sound("./audio/教育部辭典1.mp3")
            elif number == 2:
                self.play_sound("./audio/2.mp3")
            elif number == 3:
                self.play_sound("./audio/3.mp3")
            elif number == 4:
                self.play_sound("./audio/4.mp3")
            elif number == 5:
                self.play_sound("./audio/5.mp3")
            elif number == 6:
                self.play_sound("./audio/教育部辭典6.mp3")
            elif number == 7:
                self.play_sound("./audio/教育部辭典7.mp3")
            elif number == 8:
                self.play_sound("./audio/8.mp3")
            elif number == 9:
                self.play_sound("./audio/9.mp3")
            time.sleep(2)
            
            
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()

class GridLayout(GridLayout):
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    def build(self):
        return WidgetExample()

TheLabApp().run()