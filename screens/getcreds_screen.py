from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ListProperty, DictProperty, BooleanProperty, ObjectProperty
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.textfield import MDTextField
import json
from data import verify_service_account


class InputKeyScreen(MDScreen):
    creds_field = ObjectProperty()
    is_valid = BooleanProperty(False)

        
    def check_creds(self):
        creds = self.creds_field.text
        self.is_valid = verify_service_account(creds)


    def on_is_valid(self, instance, value):
        if value is True:
            print("restarting, valid creds")
            # Ensure directory exists
            os.makedirs("data/security", exist_ok=True)
            with open("data/security/creds.json", "w") as f:
                # creds_field.text is already a JSON string, write it directly
                f.write(self.creds_field.text)
    

    @property
    def app(self):
        return MDApp.get_running_app()