from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class BaseScreen(MDScreen):
    @property
    def app(self):
        return MDApp.get_running_app()
    
    @property
    def root_controller(self):
        return self.app.root_manager