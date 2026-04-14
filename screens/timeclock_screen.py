import os
import json

from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ListProperty, DictProperty, StringProperty, ObjectProperty
from kivymd.uix.pickers import MDTimePickerInput, MDModalInputDatePicker
from kivymd.app import MDApp
from kivy.clock import Clock
from data import CheckItem



class TimeClockScreen(MDScreen):


#   --- App Properties ---

    @property
    def app(self):
        return MDApp.get_running_app()