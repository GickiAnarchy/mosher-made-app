from rootcontroller import RootController

from kivymd.app import MDApp



class MosherMadeApp(MDApp):
    def build(self):
        self.root_controller = RootController()
        
        return self.root_controller