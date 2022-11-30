# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:49:49 2022

@author: Julian Hsu, Austin
"""
import random
import time
import os
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
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, AliasProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

LabelBase.register(name="msjh", fn_regular="./fonts/msjh.ttc")
LabelBase.register(name="ming", fn_regular="./fonts/cwTeXQMingZH-Medium.ttf")

# define variables
cur_status = 1      # 目前的狀態關卡，例：1表示1-1第一次，2表示1-1第二次
wrong_chance = 2    # 答錯的機會計數，若等於零的話要降1個關卡

class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_press(self):
        pass
        # print("This image button is pressed!")
        
class MyTextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__()
        self.font_name = "./fonts/msjh.ttc"
        self.font_name_helper_text = "./fonts/msjh.ttc"
        print(self.font_name_helper_text)

class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__()
        self.font_name = "./fonts/msjh.ttc"
        
class WelcomePage1(Screen):
    pass

class StartPage(Screen):
    def go_diff_branch(self):
        if cur_status in tuple(range(1, 15)):
            self.manager.current = "instruction1"
        else:
            self.manager.current = "instruction2"

class Instruction1(Screen):
    print("cur_status=", cur_status)
    print("wrong_chance=", wrong_chance)
    
    def go_diff_digits(self):
        if cur_status in (1, 2):
            self.manager.current = "temp_show1_2"
        elif cur_status in (3, 4):
            self.manager.current = "temp_show1_3"

class Instruction2(Screen):
    pass

class TempShow1_2(Screen):
    pass
    # def go_stage_1_2(self):
    #     if cur_status == 1 or cur_status == 2:
    #         self.manager.current = 'stage1_2'

class TempShow1_3(Screen):
    pass

class Stage1_2(Screen):
    my_text = StringProperty('開始')
    event = Event()
    
    def on_button_click(self):
        # Start a new thread. Be aware of creating new thread every time you press the button.
        # In which case you need to keep a reference or track the created thread.
        self.event.clear()
        global thread1
        thread1 = threading.Thread(target=self.do_button_click, args=(self.event,))
        thread1.start()
        self.ids.next_button.opacity = 1

    def do_button_click(self, event):
        global stage1_2_correct_numbers
        stage1_2_correct_numbers = []
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
                stage1_2_correct_numbers.append(number)
                print(number)
                print(stage1_2_correct_numbers)
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
                self.my_text = " "
                time.sleep(1)
    def stop_sound(self):
        self.ids.next_button.opacity = 1
        self.event.set()
        self.my_text = "開始"
        print("Main stopping thread")
        # thread1.join()
    
    def go_next_screen(self):
        self.my_text = '開始'
        self.manager.current = 'number_input1_2'
            
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()

class Stage1_3(Screen):
    my_text = StringProperty('開始')
    event = Event()
    
    def on_button_click(self):
        # Start a new thread. Be aware of creating new thread every time you press the button.
        # In which case you need to keep a reference or track the created thread.
        self.event.clear()
        global thread1
        thread1 = threading.Thread(target=self.do_button_click, args=(self.event,))
        thread1.start()
        self.ids.next_button.opacity = 1

    def do_button_click(self, event):
        global stage1_3_correct_numbers
        stage1_3_correct_numbers = []
        ROUND_ = 3
        for i in range(ROUND_ + 1):
            if event.is_set():
                self.my_text = "開始"
                break
            if i == ROUND_:
                self.my_text = "結束"
                break
            else:
                number = random.randint(1,9)
                stage1_3_correct_numbers.append(number)
                print(number)
                print(stage1_3_correct_numbers)
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
                self.my_text = " "
                time.sleep(1)
    def stop_sound(self):
        self.ids.next_button.opacity = 1
        self.event.set()
        self.my_text = "開始"
        print("Main stopping thread")
        # thread1.join()
    
    def go_next_screen(self):
        self.my_text = '開始'
        self.manager.current = 'number_input1_3'
            
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()


class NumberInput1_2(Screen):
    def save_result(self):
        global stage_1_2_response
        stage_1_2_response = []
        stage_1_2_response.append(self.ids.answer_one.text)
        stage_1_2_response.append(self.ids.answer_two.text)
        stage_1_2_response = [int(res_num) for res_num in stage_1_2_response if res_num != '']
        print("1_2關填入的答案：", stage_1_2_response)
        print("1_2關填入答案：", Counter(stage_1_2_response))
        print("1_2關正確答案：", Counter(stage1_2_correct_numbers))
        
class NumberInput1_3(Screen):
    def save_result(self):
        global stage_1_3_response
        stage_1_3_response = []
        stage_1_3_response.append(self.ids.answer_one.text)
        stage_1_3_response.append(self.ids.answer_two.text)
        stage_1_3_response.append(self.ids.answer_three.text)
        stage_1_3_response = [int(res_num) for res_num in stage_1_3_response if res_num != '']
        print("1_3關填入的答案：", stage_1_3_response)
        print("1_3關填入答案：", Counter(stage_1_3_response))
        print("1_3關正確答案：", Counter(stage1_3_correct_numbers))

class LotteryDraw1_2(Screen):
    def show_result(self):
        global cur_status
        global wrong_chance
        if Counter(stage_1_2_response) == Counter(stage1_2_correct_numbers):
            cur_status = cur_status + 1
            wrong_chance = 2
            print("cur_status=", cur_status)
            print("wrong_chance=", wrong_chance)
            time.sleep(1)
            self.manager.current = 'win_lottery1_2'
        else:
            wrong_chance -= 1
            if wrong_chance == 0:
                wrong_chance = 2
                cur_status = 1
            print("cur_status=", cur_status)
            print("wrong_chance=", wrong_chance)
            time.sleep(1)
            self.manager.current = 'lose_lottery1_2'
            
class LotteryDraw1_3(Screen):
    def show_result(self):
        global cur_status
        global wrong_chance
        if Counter(stage_1_3_response) == Counter(stage1_3_correct_numbers):
            cur_status = cur_status + 1
            wrong_chance = 2
            print("cur_status=", cur_status)
            print("wrong_chance=", wrong_chance)
            time.sleep(1)
            self.manager.current = 'win_lottery1_3'
        else:
            wrong_chance -= 1
            if wrong_chance == 0:
                wrong_chance = 2
                cur_status -= 2
            print("cur_status=", cur_status)
            print("wrong_chance=", wrong_chance)
            time.sleep(1)
            self.manager.current = 'lose_lottery1_3'

class WinLottery1_2(Screen):
    pass

class LoseLottery1_2(Screen):
    pass

class WinLottery1_3(Screen):
    pass

class LoseLottery1_3(Screen):
    pass
 
        





# Create the screen manager
sm = ScreenManager()
sm.add_widget(WelcomePage1(name='welcom_page1'))
sm.add_widget(StartPage(name='start_page'))
sm.add_widget(Instruction1(name='instruction1'))
sm.add_widget(Instruction2(name='instruction2'))
sm.add_widget(TempShow1_2(name='temp_show1_2'))
sm.add_widget(TempShow1_3(name='temp_show1_3'))
sm.add_widget(Stage1_2(name='stage1_2'))
sm.add_widget(Stage1_3(name='stage1_3'))
sm.add_widget(NumberInput1_2(name='number_input1_2'))
sm.add_widget(NumberInput1_3(name='number_input1_3'))
sm.add_widget(LotteryDraw1_2(name='lottery_draw1_2'))
sm.add_widget(LotteryDraw1_3(name='lottery_draw1_3'))
sm.add_widget(WinLottery1_2(name='win_lottery1_2'))
sm.add_widget(WinLottery1_3(name='win_lottery1_3'))
sm.add_widget(LoseLottery1_2(name='lose_lottery1_2'))
sm.add_widget(LoseLottery1_3(name='lose_lottery1_3'))

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_file("./TheLab_v2.kv")
        return screen

if __name__ == "__main__":
    DemoApp().run()