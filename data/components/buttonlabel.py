from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty


class ButtonLabel(BoxLayout):
    btn = ObjectProperty(None)      # Define the button as an ObjectProperty
    lbl = ObjectProperty(None)      # Define the label as an ObjectProperty

    def __init__(self, **kwargs):
        # 1. Register the event so Kivy recognizes 'on_release' as a valid property/event
        self.register_event_type('on_release')
        super().__init__(**kwargs)

    def on_btn(self, instance, value):
        """
        Automatically called when the 'btn' ObjectProperty is set.
        We bind the internal button's release to our class's release event.
        """
        if value:
            value.bind(on_release=lambda *x: self.dispatch('on_release'))

    def on_release(self, *args):
        """Default handler for the on_release event."""
        pass

    
    
    
    

        
