'''
Project: AnalyzOS
Author: Pedro Eduardo

File summary:
1 - Imported libraries

2 - theme_callback(): sets the aplication theme

3 - Main Window

4 - Main Function
'''

from dearpygui.simple import * 
from dearpygui.core import *
from dataframe import *

def theme_callback(sender, data):
    set_theme(sender)
    
with window("Main Window", width=1000, height=700, x_pos=0, y_pos=0, no_close=True):
    with menu_bar("Main Menu Bar"):
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

if __name__ == "__main__":
    start_dearpygui(primary_window="Main Window")