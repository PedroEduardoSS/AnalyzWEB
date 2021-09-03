from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd

#Data tab
def add_rows_data(sender, data):
    row_datas = get_value("Row data ##data")
    row_data_list = row_datas.split(",")
    add_row("Table ##data", row_data_list)

def add_headers_data(sender, data):
    column_name = get_value("Column name ##data")
    columns_list = column_name.split(",")
    set_headers("Table ##data", columns_list)

def update_cell_data(sender, data):
    coordinates = get_table_selections("Table ##data")
    value = get_value("Cell data ##data")
    for coord in coordinates:
        set_table_item("Table ##data", coord[0], coord[1], value)

#csv file-handling
def add_csv_file(sender, data):
    dataframe = pd.read_csv(get_value("CSV file path"))
    columns = dataframe.columns
    columns_list = []
    for column in columns:
        columns_list.append(column)
    set_headers("Table ##data", columns_list)

    rows = dataframe.index
    for row in rows:
        id_row = dataframe.loc[row].to_list()
        add_row("Table ##data", id_row)
    configure_item("Table ##data", show=True)

#ATENTION
def save_as_csv_data(sender, data):
    rows = get_table_selections("Table ##data")
    data = pd.DataFrame(rows)
    data.to_csv("CSV-Files\Sample2.csv", index=False)

#ATENTION end

def dataframes(sender, data):
    with window("DataFrame", width=400, height=300, no_close=True):
        with tab_bar("tabbar ##dataframes"):
            with tab("Data ##dataframes"):
                add_text("Manipulate dataframes here", bullet=True)
                add_separator()
                
                add_text("Pay attention to the hint below\nMore information on 'Help' tab", bullet=True)
                add_input_text("CSV file path", hint="CSV-Files\File.csv")
                add_button("Add CSV file", callback=add_csv_file)
                add_spacing(count=5)

                add_text("Add the columns names below", bullet=True)
                add_input_text("Column name ##data", hint="col name1,col name2", tip="Each column name\nmust be separated by comma")
                add_button("Add columns ##data", callback=add_headers_data)
                add_spacing(count=5)
                
                add_text("Add data for each cell of a row", bullet=True)
                add_input_text("Row data ##data", hint="data col1,data col2", tip="Each row data\nmust be separated by comma")
                add_button("Add row ##data", callback=add_rows_data)
                add_spacing(count=5)

                add_text("Update the data from a specific cell", bullet=True)
                add_input_text("Cell data ##data", hint="data col1,data col2", tip="Each row data\nmust be separated by comma")
                add_button("Update data ##data", callback=update_cell_data)
                add_spacing(count=5)
                
                add_text("ATTENTION! You can only save the tables data", bullet=True)
                add_button("Save as CSV ##data", callback=save_as_csv_data)
                add_table("Table ##data", ["Wait", "Wait"], show=False)
            
            with tab("Help ##dataframes"):
                add_text("It is your place to create or manipulate dataframes", bullet=True)
                add_text("To open a CSV file on Manipulation tab,\n you must firstly add the csv file on 'CSV-Files' folder", bullet=True)
                add_separator()
                add_button("Close ##DataFrame", small=True, callback=lambda:delete_item("DataFrame"), tip="You must close the window here", label="Close Window")