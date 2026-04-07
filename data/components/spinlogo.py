from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.uix.image import Image

class SpinningLogo(Image):
    angle = NumericProperty(0)

    def spin(self, dt=None):
        r1 = Animation(angle=360, duration=3)
        
        def reset(*args):
            self.angle = 0
            self.spin()
        
        r1.bind(on_complete=reset)
        r1.start(self)
