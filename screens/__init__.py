from .basescreen import BaseScreen
from .homescreen import HomeScreen
from .createscreen import CreateScreen



SCREENS = [
    (HomeScreen, "home"),
    (CreateScreen,  "create"),
    ]



__all__ = [
    "BaseScreen",
    "HomeScreen",
    "CreateScreen"
    ]