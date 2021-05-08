from dearpygui.core import *
from dearpygui.simple import * 

def dataframes(sender, data):
    with window("DataFrame"):
        with tab_bar("tabbar"):
            with tab("Management ##dataframes"):
                add_text("For now, It is okay", bullet=True)
            with tab("Settings ##dataframes"):
                add_text("Test", bullet=True)
            with tab("Help ##dataframes"):
                add_text("It is your place to create or manipulate dataframes", bullet=True)
                add_text("You can use Series instead dataframes here", bullet=True)