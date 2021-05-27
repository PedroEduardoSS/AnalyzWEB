from dearpygui.core import *
from dearpygui.simple import *

def add_rows():
    row_datas = get_value("Row data")
    row_data_list = row_datas.split(",")
    add_row("Table", row_data_list)

def add_headers(sender, data):
    column_name = get_value("Column name")
    columns_list = column_name.split(",")
    set_headers("Table", columns_list)

def dataframes(sender, data):
    with window("DataFrame", width=400, height=300, no_close=True):
        with tab_bar("tabbar ##dataframes"):
            with tab("Management ##dataframes"):
                add_text("Create/manipulate dataframes here", bullet=True)
                add_separator()
                add_input_text("Column name", hint="col name1,col name2", tip="Each column name\nmust be separated by comma")
                add_button("Add columns", callback=add_headers)
                add_input_text("Row data", hint="data col1,data col2", tip="Each row data\nmust be separated by comma")
                add_button("Add row", callback=add_rows)
                add_button("tabledata", callback=lambda:print(get_table_data("Table")))
                add_table("Table", ["col1", "col2", "col3"])
                add_separator()

            with tab("Settings ##dataframes"):
                add_text("Test", bullet=True)
            
            with tab("Help ##dataframes"):
                add_text("It is your place to create or manipulate dataframes", bullet=True)
                add_text("You can use Series instead dataframes here", bullet=True)
                add_separator()
                add_button("Close ##DataFrame", small=True, callback=lambda:delete_item("DataFrame"), tip="You must close the window here", label="Close Window")