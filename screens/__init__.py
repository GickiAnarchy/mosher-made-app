from .home_screen import HomeScreen
from .timeclock_screen import TimeClockScreen
from .loading_screen import LoadingScreen
from .getcreds_screen import InputKeyScreen
from .edittime_screen import EditTimeScreen
from .add_screen import AddScreen





SCREENS = [
    (HomeScreen, "home"),
    (TimeClockScreen, "clock"),
    (LoadingScreen, "loading"),
    (InputKeyScreen, "needkey"),
    (EditTimeScreen, "edittime"),
    (AddScreen, "add"),
    ]


__all__ = [
    "SCREENS",
    "HomeScreen",
    "TimeClockScreen",
    "LoadingScreen",
    "InputKeyScreen",
    "EditTimeScreen",
    "AddScreen",
    ]