from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd

def dataframes(sender, data):
    with window("DataFrame", width=400, height=300, no_close=True):
        with tab_bar("tabbar ##dataframes"):
            with tab("Management ##dataframes"):
                add_text("Create/manipulate dataframes here", bullet=True)
                add_listbox("columns", items=["col1", "col2", "col3", "col4", "col5", "col6"])
                add_separator()
                add_table("Default", ["col1", "col2", "col3"])
            with tab("Settings ##dataframes"):
                add_text("Test", bullet=True)
            with tab("Help ##dataframes"):
                add_text("It is your place to create or manipulate dataframes", bullet=True)
                add_text("You can use Series instead dataframes here", bullet=True)
                add_button("Close ##DataFrame", small=True, callback=lambda:delete_item("DataFrame"), tip="You must close the window here", label="Close Window")