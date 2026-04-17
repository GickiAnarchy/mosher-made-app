import os
import json
from datetime import datetime

from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout 
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ListProperty, DictProperty, StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivy.clock import Clock


class PunchScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clock_file = "clocked_in.json"
        self.on_the_clock = {}      
        '''
        self.on_the_clock = {
            "mm-dd-yyyy": {
                "time_in": "hh:mm,
                "time_out": "hh:mm"
            },
        }
        '''



    def on_enter(self):
        self.load_clocked_on()


    def load_clocked_on(self):
        if os.path.exists(self.clock_file):
            try:
                with open(self.clock_file, "r") as f:
                    self.on_the_clock = json.load(f)  
                    print("Loaded clocked_in people")
            except json.JSONDecodeError:
                print("Error decoding clocked_in.json. Starting with empty clocked_in.")
                self.on_the_clock = {}


    def update_clocked_file(self):
        with open(self.clock_file, "w") as f:
            json.dump(self.on_the_clock,f)


    def pressed_clock_in(self, btn=None):
        date = self.app.rc.time_manager.get_current_date()
        self.on_the_clock.update({date:{"time_in":self.app.rc.time_manager.get_current_time()}})
        self.print_clocked_in()
        self.update_clocked_file()


    def pressed_clock_out(self, btn=None):
        date = self.app.rc.time_manager.get_current_date()
        if date in self.on_the_clock.keys():
            self.on_the_clock[date]["time_out"] = self.app.rc.time_manager.get_current_time()
            self.print_clocked_in()
            self.update_clocked_file()
    

    def print_clocked_in(self):
        for k,v in self.on_the_clock.items():
            print(k)
            print(v)


    @property
    def app(self):
        return MDApp.get_running_app()