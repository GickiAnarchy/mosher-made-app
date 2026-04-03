from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.widget import MDWidget
from kivy.properties import ObjectProperty,StringProperty



class CheckItem(MDBoxLayout):
    name_text = StringProperty("")
    checkbox = ObjectProperty()

    
    def __init__(self, text = "", group = "", **kwargs):
        super().__init__(**kwargs)
        self.name_text = text
        self.checkbox.group = group
    

    @property
    def group(self):
        return self.checkbox.group
    
    @group.setter
    def group(self, value):
        self.checkbox.group = value