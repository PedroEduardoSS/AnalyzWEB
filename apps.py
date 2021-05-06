from dearpygui.core import *
from dearpygui.simple import * 

def workspace(sender, data):
    with window("Table"):
        with tab_bar("tabbar"):
            with tab("help"):
                add_text("Welcome to mad house")
                add_color_picker4("Picker 1")
            with tab("Settings"):
                add_text("Choose one")
                add_radio_button("items", items=["item 1", "item 2", "item 3"])