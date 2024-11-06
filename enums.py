from enum import Enum, auto


class Colors(Enum):
    PRIMARY = "#3498db" 
    SECONDARY = "#2ecc71" 
    SUCCESS = "#28a745" 
    DANGER = "#dc3545" 
    WARNING = "#ffc107" 
    INFO = "#17a2b8" 
    LIGHT = "#f8f9fa" 
    DARK = "#343a40"
    BLUE = "blue"


class Fonts(Enum):
    HEADER = ("Helvetica", 20) 
    SUBHEADER = ("Helvetica", 16) 
    BODY = ("Helvetica", 12)







class Styles(Enum):
    TITLE_ALIGNMENT = "center"
    TITLE_PADDING = "60px"
    TITLE_COLOR = "blue"
