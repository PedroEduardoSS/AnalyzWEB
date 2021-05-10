from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd

def dataframes(sender, data):
    with window("DataFrame"):
        with tab_bar("tabbar"):
            with tab("Management ##dataframes"):
                add_text("For now, It is okay", bullet=True)
                add_separator()
                add_table("Default", ["col1", "col2", "col3"])
            with tab("Settings ##dataframes"):
                add_text("Test", bullet=True)
            with tab("Help ##dataframes"):
                add_text("It is your place to create or manipulate dataframes", bullet=True)
                add_text("You can use Series instead dataframes here", bullet=True)