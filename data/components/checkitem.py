from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.widget import MDWidget
from kivy.properties import ObjectProperty,StringProperty
from kivy.clock import Clock


class CheckItem(MDBoxLayout):
    name_text = StringProperty("")
    checkbox = ObjectProperty()

    
    def __init__(self, text = "", group = None, **kwargs):
        super().__init__(**kwargs)
        self.name_text = text
        if group:
            Clock.schedule_once(lambda dt: self._set_group(group))


    def _set_group(self, group):
        if self.checkbox:
            self.checkbox.group = group


    @property
    def group(self):
        return self.checkbox.group


    @group.setter
    def group(self, value):
        self.checkbox.group = value