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

class WidgetExample(BoxLayout):
    my_text = StringProperty('Start')
    def on_button_click(self):
        # Start a new thread. Be aware of creating new thread every time you press the button.
        # In which case you need to keep a reference or track the created thread.
        threading.Thread(target = self.do_button_click).start()

    def do_button_click(self):
        for i in range(1,11):
            i=random.randint(1,10)
            time.sleep(1)
            print(i)
            self.my_text = str(i)

class GridLayout(GridLayout):
    pass


class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


TheLabApp().run()