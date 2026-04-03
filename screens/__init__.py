from .home_screen import HomeScreen
from .logwork_screen import LogWorkScreen



SCREENS = [
    (HomeScreen, "home"),
    (LogWorkScreen, "logwork"),
    ]


__all__ = [
    "LogWorkScreen",
    "HomeScreen",
    ]