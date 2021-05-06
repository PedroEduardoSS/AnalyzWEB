from dearpygui.core import *
from dearpygui.simple import * 

def dataframes(sender, data):
    with window("Table"):
        with tab_bar("tabbar"):
            with tab("help"):
                add_text("Welcome test")
                add_color_picker4("Picker 1")
            with tab("Settings"):
                add_text("Test")
                add_radio_button("items", items=["item 1", "item 2", "item 3"])