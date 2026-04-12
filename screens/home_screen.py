from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty


class HomeScreen(MDScreen):
    clocked_in_box = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self):
        Clock.schedule_once(self.setup_ui)

    def setup_ui(self, dt=None):
        # Safely check if rc exists before using it
        if hasattr(self.app, 'rc') and self.app.rc:
            clocked_in = self.app.rc.get_clocked_in()

    @property
    def app(self):
        return MDApp.get_running_app()