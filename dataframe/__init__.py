from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd

def add_rows():
    row_datas = get_value("Row data")
    row_data_list = row_datas.split(",")
    add_row("Table ##creation", row_data_list)

def add_headers(sender, data):
    column_name = get_value("Column name")
    columns_list = column_name.split(",")
    set_headers("Table ##creation", columns_list)

def add_csv_file(sender, data):
    dataframe = pd.read_csv(get_value("CSV file path"))
    columns = dataframe.columns
    columns_list = []
    for column in columns:
        columns_list.append(column)
    set_headers("Table ##manipulation", columns_list)

    rows = dataframe.index
    for row in rows:
        id_row = dataframe.loc[row].to_list()
        add_row("Table ##manipulation", id_row)
    configure_item("Table ##manipulation", show=True)

def dataframes(sender, data):
    with window("DataFrame", width=400, height=300, no_close=True):
        with tab_bar("tabbar ##dataframes"):
            with tab("Creation ##dataframes"):
                add_text("Create dataframes here", bullet=True)
                add_separator()
                add_input_text("Column name", hint="col name1,col name2", tip="Each column name\nmust be separated by comma")
                add_button("Add columns", callback=add_headers)
                add_input_text("Row data", hint="data col1,data col2", tip="Each row data\nmust be separated by comma")
                add_button("Add row", callback=add_rows)
                add_table("Table ##creation", ["col1", "col2", "col3"])

            with tab("Manipulation ##dataframes"):
                add_text("Manipulate dataframes here", bullet=True)
                add_separator()
                add_input_text("CSV file path", hint="CSV-Files\File.csv")
                add_button("Add CSV file", callback=add_csv_file)
                add_table("Table ##manipulation", ["Wait", "Wait"], show=False)
            
            with tab("Help ##dataframes"):
                add_text("It is your place to create or manipulate dataframes", bullet=True)
                add_text("To open a CSV file on Manipulation tab,\n you must firstly add the csv file on 'CSV-Files'", bullet=True)
                add_separator()
                add_button("Close ##DataFrame", small=True, callback=lambda:delete_item("DataFrame"), tip="You must close the window here", label="Close Window")