from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.widget import MDWidget
from kivy.properties import ObjectProperty,StringProperty



class CheckItem(MDBoxLayout):
    name_text = StringProperty()
    cb_group = StringProperty()
    checkbox = ObjectProperty()

    