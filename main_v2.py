# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:49:49 2022

@author: Julian, Austin
"""
import random
import time
from collections import Counter
import threading
from threading import Event
from kivymd.app import App, MDApp
from kivy.lang.builder import Builder
from kivy.core.text import LabelBase
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivymd.uix.textfield.textfield import MDTextField
from kivy.uix.textinput import TextInput
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader


LabelBase.register(name="msjh", fn_regular="./fonts/msjh.ttc")
LabelBase.register(name="ming", fn_regular="./fonts/cwTeXQMingZH-Medium.ttf")
class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        print("This image button is pressed!")
        
class MyTextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__()
        self.font_name = "./fonts/msjh.ttc"
        self.font_name_helper_text = "./fonts/msjh.ttc"
        print(self.font_name_helper_text)
        
class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__()
        self.font_name = 'msjh'
        self.te
        
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

# global variables
## stage1_correct_numbers = []
## first_stage_user_response = []
current_digit = '2'
difficulty = 1             # 難易度

class FirstStage(Screen):
    my_text = StringProperty('開始')
    event = Event()
    def on_button_click(self):
        # Start a new thread. Be aware of creating new thread every time you press the button.
        # In which case you need to keep a reference or track the created thread.
        self.event.clear()
        global thread1
        thread1 = threading.Thread(target=self.do_button_click, args=(self.event,))
        thread1.start()

    def do_button_click(self, event):
        global stage1_correct_numbers
        stage1_correct_numbers = []
        if self.ids.current_digit.text in ("2", "3", "4", "5", "6", "7", "8"):
            ROUND_ = int(self.ids.current_digit.text)
        else:
            ROUND_ = 2
        for i in range(ROUND_ + 1):
            if event.is_set():
                self.my_text = "開始"
                break
            if i == ROUND_:
                self.my_text = "結束"
                break
            else:
                number = random.randint(1,9)
                stage1_correct_numbers.append(number)
                print(number)
                print(stage1_correct_numbers)
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

class NumberInput1(Screen):
    def save_result(self):
        global first_stage_user_response
        first_stage_user_response = []
        first_stage_user_response.append(self.ids.answer_one.text)
        first_stage_user_response.append(self.ids.answer_two.text)
        first_stage_user_response.append(self.ids.answer_three.text)
        first_stage_user_response.append(self.ids.answer_four.text)
        first_stage_user_response.append(self.ids.answer_five.text)
        first_stage_user_response.append(self.ids.answer_six.text)
        first_stage_user_response.append(self.ids.answer_seven.text)
        first_stage_user_response.append(self.ids.answer_eight.text)
        first_stage_user_response = [int(res_num) for res_num in first_stage_user_response if res_num != '']
        print("第一關填入的答案：", first_stage_user_response)
        print(Counter(first_stage_user_response), Counter(stage1_correct_numbers))
        
class LotteryDraw(Screen):
    def show_result(self):
        if Counter(first_stage_user_response) == Counter(stage1_correct_numbers):
            time.sleep(1)
            self.manager.current = 'win_lottery'
        else:
            time.sleep(1)
            self.manager.current = 'lose_lottery'

class WinLottery(Screen):
    pass

class LoseLottery(Screen):
    pass
 
        

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
sm.add_widget(NumberInput1(name='number_input1'))
sm.add_widget(LotteryDraw(name='lottery_draw'))
sm.add_widget(WinLottery(name='win_lottery'))
sm.add_widget(LoseLottery(name='lose_lottery'))
sm.add_widget(SecondStage(name='second_stage'))

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_file("./TheLab_v2.kv")
        return screen

if __name__ == "__main__":
    DemoApp().run()