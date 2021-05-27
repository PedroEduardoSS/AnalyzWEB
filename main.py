from dearpygui.simple import * 
from dearpygui.core import *
from dataframe import *

#Main menu bar -> Themes
def theme_callback(sender, data):
    set_theme(sender)
    
with window("Work Space", width=1000, height=700, x_pos=0, y_pos=0, no_close=True):
    with menu_bar("Main Menu Bar"):
        with menu("DS Tools"):
            add_menu_item("DataFrames", callback=dataframes)
        with menu("Settings"):
            with menu("Themes"):
                add_menu_item("Dark", callback=theme_callback)
                add_menu_item("Light", callback=theme_callback)
                add_menu_item("Classic", callback=theme_callback)
                add_menu_item("Dark 2", callback=theme_callback)
                add_menu_item("Grey", callback=theme_callback)
                add_menu_item("Dark Grey", callback=theme_callback)
                add_menu_item("Cherry", callback=theme_callback)
                add_menu_item("Purple", callback=theme_callback)
                add_menu_item("Gold", callback=theme_callback)
                add_menu_item("Red", callback=theme_callback)

            with menu("Dev Tools"):
                add_menu_item("Documentation", callback=lambda:show_documentation())
                add_menu_item("Metrics", callback=lambda:show_metrics())
                add_menu_item("Debug", callback=lambda:show_debug())
                add_menu_item("logger", callback=lambda:show_logger())
                add_menu_item("About", callback=lambda:show_about())

    add_text("Welcome to Work Space", bullet=True)
    add_text("Use this space to manage your work", bullet=True)
    add_separator()
    
start_dearpygui(primary_window="Work Space")