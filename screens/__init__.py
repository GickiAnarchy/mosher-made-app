from .home_screen import HomeScreen
from .timeclock_screen import TimeClockScreen
from .loading_screen import LoadingScreen
from .add_screen import AddScreen
from .punch_screen import PunchScreen




SCREENS = [
    (HomeScreen, "home"),
    (PunchScreen, "punch"),
    (LoadingScreen, "loading"),
    (AddScreen, "add"),
    ]


__all__ = [
    "SCREENS",
    "HomeScreen",
    "PunchScreen",
    "LoadingScreen",
    "AddScreen",
    ]