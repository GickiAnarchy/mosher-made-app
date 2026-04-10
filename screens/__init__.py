from .home_screen import HomeScreen
from .timeclock_screen import TimeClockScreen
from .loading_screen import LoadingScreen
from .getcreds_screen import InputKeyScreen
from .edittime_screen import EditTimeScreen





SCREENS = [
    (HomeScreen, "home"),
    (TimeClockScreen, "clock"),
    (LoadingScreen, "loading"),
    (InputKeyScreen, "needkey"),
    (EditTimeScreen, "edittime"),
    ]


__all__ = [
    "SCREENS",
    "HomeScreen",
    "TimeClockScreen",
    "LoadingScreen",
    "InputKeyScreen",
    "EditTimeScreen",
    ]