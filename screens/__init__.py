from .home_screen import HomeScreen
from .timeclock_screen import TimeClockScreen
from .loading_screen import LoadingScreen
from .add_screen import AddScreen





SCREENS = [
    (HomeScreen, "home"),
    (TimeClockScreen, "clock"),
    (LoadingScreen, "loading"),
    (AddScreen, "add"),
    ]


__all__ = [
    "SCREENS",
    "HomeScreen",
    "TimeClockScreen",
    "LoadingScreen",
    "AddScreen",
    ]