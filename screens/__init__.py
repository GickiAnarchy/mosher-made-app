from .home_screen import HomeScreen
from .logwork_screen import LogWorkScreen
from .inout_screen import InOutScreen
from .loading_screen import LoadingScreen



SCREENS = [
    (HomeScreen, "home"),
    (LogWorkScreen, "logwork"),
    (InOutScreen, "inout"),
    (LoadingScreen, "loading"),
    ]


__all__ = [
    "LogWorkScreen",
    "HomeScreen",
    "InOutScreen",
    "LoadingScreen",
    ]