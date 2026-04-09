from .home_screen import HomeScreen
from .timeclock_screen import TimeClockScreen
from .loading_screen import LoadingScreen
from .getcreds_screen import InputKeyScreen



SCREENS = [
    (HomeScreen, "home"),
    (TimeClockScreen, "clock"),
    (LoadingScreen, "loading"),
    (InputKeyScreen, "needkey"),
    ]


__all__ = [
    "HomeScreen",
    "TimeClockScreen",
    "LoadingScreen",
    "InputKeyScreen",
    ]