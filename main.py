from dearpygui.core import *
from dearpygui.simple import * 
from apps import *

#Main menu bar -> Themes
def theme_callback(sender, data):
    set_theme(sender)
    
with window("Primary"):
    with menu_bar("Main Menu Bar"):
        with menu("Home"):
            add_menu_item("WorkSpace", callback=workspace)
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

    with window("Work Space", no_close=True):
        add_text("Welcome to Work Space")
        add_color_edit4("name1")

start_dearpygui(primary_window="Primary")