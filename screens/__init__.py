from .home_screen import HomeScreen
from .logwork_screen import LogWorkScreen
from .inout_screen import InOutScreen



SCREENS = [
    (HomeScreen, "home"),
    (LogWorkScreen, "logwork"),
    (InOutScreen, "inout"),
    ]


__all__ = [
    "LogWorkScreen",
    "HomeScreen",
    "InOutScreen",
    ]