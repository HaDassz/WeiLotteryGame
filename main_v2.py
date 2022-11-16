# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:49:49 2022

@author: Austin
"""
import random
import time
import threading
from threading import Event
from kivymd.app import App, MDApp
from kivy.lang.builder import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivymd.uix.textfield import textfield
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader


class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        print("This image button is pressed!")
class WelcomePage1(Screen):
    pass

class WelcomePage2(Screen):
    pass

class Instruction1(Screen):
    pass

class TempShow1(Screen):
    pass

class TempShow2(Screen):
    pass

class FirstStage(Screen):
    my_text = StringProperty('開始')
    event = Event()
    stage1_correct_numbers = []
    def on_button_click(self):
        # Start a new thread. Be aware of creating new thread every time you press the button.
        # In which case you need to keep a reference or track the created thread.
        self.event.clear()
        global thread1
        thread1 = threading.Thread(target=self.do_button_click, args=(self.event,))
        thread1.start()

    def do_button_click(self, event):
        ROUND_ = 7
        for i in range(ROUND_):
            if event.is_set():
                self.my_text = u"開始"
                break
            if i == ROUND_ -1:
                self.my_text = "結束"
                break
            else:
                number = random.randint(1,9)
                self.stage1_correct_numbers.append(number)
                print(number)
                print(self.stage1_correct_numbers)
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
                    
                time.sleep(1)
                self.my_text = "下一個"
                time.sleep(1)

    def stop_sound(self):
        self.event.set()
        self.my_text = "開始"
        print("Main stopping thread")
        # thread1.join()
        
            
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()

class SecondStage(Screen):
    my_text = StringProperty('Start')
    event = Event()
    stage1_correct_numbers = []
    def on_button_click(self):
        # Start a new thread. Be aware of creating new thread every time you press the button.
        # In which case you need to keep a reference or track the created thread.
        self.event.clear()
        global thread1
        thread1 = threading.Thread(target=self.do_button_click, args=(self.event,))
        thread1.start()

    def do_button_click(self, event):
        for i in range(1,11):
            if event.is_set():
                self.my_text = "Start"
                break
            number = random.randint(1,9)
            self.stage1_correct_numbers.append(number)
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
            
    def stop_sound(self):
        self.event.set()
        self.my_text = "Start"
        print("Main stopping thread")
        # thread1.join()
        
            
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()

# Create the screen manager
sm = ScreenManager()
sm.add_widget(WelcomePage1(name='welcom_page1'))
sm.add_widget(WelcomePage2(name='welcom_page2'))
sm.add_widget(Instruction1(name='instruction1'))
sm.add_widget(TempShow1(name='temp_show1'))
sm.add_widget(TempShow2(name='temp_show2'))
sm.add_widget(FirstStage(name='first_stage'))
sm.add_widget(SecondStage(name='second_stage'))

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_file("./TheLab_v2.kv")
        return screen

DemoApp().run()