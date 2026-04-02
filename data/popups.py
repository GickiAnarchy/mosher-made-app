from .models import Employer, Employee
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog,MDDialogContentContainer,MDDialogButtonContainer
from kivymd.uix.button import MDButton,MDButtonText
from kivymd.uix.textfield import MDTextField,MDTextFieldHelperText,MDTextFieldHintText
from kivy.properties import StringProperty, ObjectProperty
from kivy.animation import Animation


class CreateDialog(MDDialog):
txt = StringProperty("Create")
on_confirm = ObjectProperty(None) #the callback
message = ObjectProperty()
create_type = StringProperty("")
create_field = ObjectProperty()


# Fade in
def open(self, *args, **kwargs):
super().open(*args, **kwargs)
Animation(opacity = 1, duration = 0.3).start(self)

# Fade out
def fade_dismiss(self, *args):
anim = Animation(opacity = 0, duration = 0.6)
anim.bind(on_complete = lambda *x: self.dismiss)
anim.start(self)

def _yes_pressed(self, *args):
if self.on_confirm:
self.on_confirm()
self.fade_dismiss()



"""
def __init__(self, **kwargs):
#        super().__init__(**kwargs)

#        self.size_hint = (0.8, 0.4)
#        self.title = "Create"
#        self.opacity = 0  # start invisible

        #layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)

#        message = MDLabel(
#        text=self.txt,
#        halign="center",
#        valign="middle"
#        )
#
#    # Force wrapping inside the popup width
#        message.bind(
#            size=lambda instance, value: setattr(instance, 'text_size', (instance.width, None))
#        )

#        button_layout = MDBoxLayout(spacing=20, size_hint_y=None, height=50)

#        yes_button = MDFlatButton(text="Yes")
#        no_button = MDFlatButton(text="No")

#        yes_button.bind(on_release=self._yes_pressed)
#        no_button.bind(on_release=self.fade_dismiss)

#        button_layout.add_widget(yes_button)
#        button_layout.add_widget(no_button)

#        layout.add_widget(message)
#        layout.add_widget(button_layout)

#        self.content = layout
"""