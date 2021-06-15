from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd

def add_rows_creation(sender, data):
    row_datas = get_value("Row data ##creation")
    row_data_list = row_datas.split(",")
    add_row("Table ##creation", row_data_list)

def add_headers_creation(sender, data):
    column_name = get_value("Column name ##creation")
    columns_list = column_name.split(",")
    set_headers("Table ##creation", columns_list)

def add_rows_manipulation(sender, data):
    row_datas = get_value("Row data ##manipulation")
    row_data_list = row_datas.split(",")
    add_row("Table ##manipulation", row_data_list)

def add_headers_manipulation(sender, data):
    column_name = get_value("Column name ##manipulation")
    columns_list = column_name.split(",")
    set_headers("Table ##manipulation", columns_list)

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

#ATENTION
def save_as_csv_creation(sender, data):
    rows = get_table_data("Table ##creation")
    data = pd.DataFrame(rows)
    data.to_csv("CSV-Files\Sample1.csv", index=False)

def save_as_csv_manipulation(sender, data):
    rows = get_table_data("Table ##manipulation")
    data = pd.DataFrame(rows)
    data.to_csv("CSV-Files\Sample2.csv", index=False)

#ATENTION end

def dataframes(sender, data):
    with window("DataFrame", width=400, height=300, no_close=True):
        with tab_bar("tabbar ##dataframes"):
            with tab("Creation ##dataframes"):
                add_text("Create dataframes here", bullet=True)
                add_separator()

                add_text("Add the columns names below", bullet=True)
                add_input_text("Column name ##creation", hint="col name1,col name2", tip="Each column name\nmust be separated by comma")
                add_button("Add columns ##creation", callback=add_headers_creation)
                add_spacing(count=5)

                add_text("Add data for each cell of a row", bullet=True)
                add_input_text("Row data ##creation", hint="data col1,data col2", tip="Each row data\nmust be separated by comma")
                add_button("Add row ##creation", callback=add_rows_creation)
                add_spacing(count=5)

                add_text("ATTENTION! You can only save the tables data", bullet=True)
                add_button("Save as CSV ##creation", callback=save_as_csv_creation)
                add_table("Table ##creation", ["col1", "col2", "col3"])

            with tab("Manipulation ##dataframes"):
                add_text("Manipulate dataframes here", bullet=True)
                add_separator()
                
                add_text("Pay attention to the hint below\nMore information on 'Help' tab", bullet=True)
                add_input_text("CSV file path", hint="CSV-Files\File.csv")
                add_button("Add CSV file", callback=add_csv_file)
                add_spacing(count=5)

                add_text("Add the columns names below", bullet=True)
                add_input_text("Column name ##manipulation", hint="col name1,col name2", tip="Each column name\nmust be separated by comma")
                add_button("Add columns ##manipulation", callback=add_headers_manipulation)
                add_spacing(count=5)
                
                add_text("Add data for each cell of a row", bullet=True)
                add_input_text("Row data ##manipulation", hint="data col1,data col2", tip="Each row data\nmust be separated by comma")
                add_button("Add row ##manipulation", callback=add_rows_manipulation)
                add_spacing(count=5)
                
                add_text("ATTENTION! You can only save the tables data", bullet=True)
                add_button("Save as CSV ##manipulation", callback=save_as_csv_manipulation)
                add_table("Table ##manipulation", ["Wait", "Wait"], show=False)
            
            with tab("Help ##dataframes"):
                add_text("It is your place to create or manipulate dataframes", bullet=True)
                add_text("To open a CSV file on Manipulation tab,\n you must firstly add the csv file on 'CSV-Files' folder", bullet=True)
                add_separator()
                add_button("Close ##DataFrame", small=True, callback=lambda:delete_item("DataFrame"), tip="You must close the window here", label="Close Window")