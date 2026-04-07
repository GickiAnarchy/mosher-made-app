from .home_screen import HomeScreen
from .timeclock_screen import TimeClockScreen
from .loading_screen import LoadingScreen



SCREENS = [
    (HomeScreen, "home"),
    (TimeClockScreen, "clock"),
    (LoadingScreen, "loading"),
    ]


__all__ = [
    "HomeScreen",
    "TimeClockScreen",
    "LoadingScreen",
    ]