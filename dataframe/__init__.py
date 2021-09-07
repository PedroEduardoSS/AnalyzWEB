from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd

#Handling tab
def add_headers_data(sender, data):
    column_name = get_value("Column name ##handling")
    column_index = get_value("Column index ##handling")
    column_datas = get_value("Column values").split(",")
    insert_column("Table ##handling", column_index, column_name, column_datas)

def update_headers_data(sender, data):
    columns = get_value("Columns ##handling").split(",")
    set_headers("Table ##handling", columns)

def remove_column(sender, data):
    column_index = get_value("Column index")
    delete_column("Table ##handling", column_index)

def add_row_datas(sender, data):
    row_datas = get_value("Row data ##handling").split(",")
    add_row("Table ##handling", row_datas)

def remove_row(sender, data):
    row_index = get_value("Row index ##handling")
    delete_row("Table ##handling", row_index)

def update_cell_data(sender, data):
    coordinates = get_table_selections("Table ##handling")
    value = get_value("Cell data ##handling")
    for coord in coordinates:
        set_table_item("Table ##handling", coord[0], coord[1], value)

#Table tab
def create_table(sender, data):
    configure_item("Table ##handling", show=True)

def delete_table(sender, data):
    set_headers("Table ##handling", ["Header", "Header", "Header"])
    clear_table("Table ##handling")

#csv file-handling
def add_csv_file(sender, data):
    file_name = get_value("CSV file path")
    dataframe = pd.read_csv(f"CSV-Files\{file_name}")
    columns = dataframe.columns
    columns_list = []
    for column in columns:
        columns_list.append(column)
    set_headers("Table ##handling", columns_list)

    rows = dataframe.index
    for row in rows:
        id_row = dataframe.loc[row].to_list()
        add_row("Table ##handling", id_row)
    configure_item("Table ##handling", show=True)

#ATENTION
def save_as_csv_data(sender, data):
    columns = get_value("Columns names").split(",")
    rows = get_table_data("Table ##handling")
    file_name = get_value("CSV file name")
    data = pd.DataFrame(rows, columns=columns)
    data.to_csv(f"CSV-Files\{file_name}.csv", index=False)

#ATENTION end

def dataframes(sender, data):
    with window("DataFrame", width=400, height=300, no_close=True):
        with tab_bar("tabbar ##dataframes"):
            with tab("Handling ##dataframes"):
                add_text("Manipulate the table here", bullet=True)
                add_separator()

                add_text("Initial commands", color=[255, 0, 0])
                add_button("Create Table", callback=create_table)
                add_same_line()
                add_button("Delete Table", callback=delete_table)
                add_spacing(count=3)
                add_input_text("CSV file path", hint="myfile.csv")
                add_button("Add CSV file", callback=add_csv_file)
                
                add_spacing(count=2)
                add_separator()
                add_spacing(count=2)

                add_text("Columns", color=[255, 0, 0])
                add_text("Add the columns names", bullet=True)
                add_input_text("Column name ##handling", hint="col name1,col name2", tip="Each column name\nmust be separated by comma")
                add_input_int("Column index ##handling")
                add_input_text("Column values")
                add_button("Add column ##handling", callback=add_headers_data)

                add_spacing(count=3)

                add_text("Update the columns names", bullet=True)
                add_input_text("Columns ##handling", hint="col name1,col name2", tip="Each column name\nmust be separated by comma")
                add_button("Update columns ##handling", callback=update_headers_data)
                
                add_spacing(count=3)

                add_text("Delete the column", bullet=True)
                add_input_int("Column index", tip="The index starts at 0")
                add_button("Delete column ##handling", callback=remove_column)
                
                add_spacing(count=2)
                add_separator()
                add_spacing(count=2)

                add_text("Rows and Cells", color=[255, 0, 0])
                add_text("Add data for each cell of a row", bullet=True)
                add_input_text("Row data ##handling", hint="data col1,data col2", tip="Each row data\nmust be separated by comma")
                add_button("Add row ##handling", callback=add_row_datas)
                
                add_spacing(count=3)

                add_text("Remove row", bullet=True)
                add_input_int("Row index ##handling")
                add_button("Remove row ##handling", callback=remove_row)
                
                add_spacing(count=3)

                add_text("Update the data from a specific cell", bullet=True)
                add_input_text("Cell data ##handling", hint="data col1,data col2", tip="Each row data\nmust be separated by comma")
                add_button("Update data ##handling", callback=update_cell_data)
                
                add_spacing(count=2)
                add_separator()
                add_spacing(count=2)

                add_text("Save", color=[255, 0, 0])
                add_text("ATTENTION! You can only save the tables data", bullet=True)
                add_input_text("Columns names")
                add_input_text("CSV file name")
                add_button("Save as CSV ##handling", callback=save_as_csv_data)
                
            with tab("Table ##dataframes"):
                add_text("Table", bullet=True)
                add_table("Table ##handling", ["Col1", "Col2", "Col3"], show=False)
            
            with tab("Help ##dataframes"):
                with collapsing_header("Handling Tab"):
                    add_text("Test")
                with collapsing_header("Table Tab"):
                    add_text("Test2")
                add_separator()
                add_button("Close ##DataFrame", small=True, callback=lambda:delete_item("DataFrame"), tip="You must close the window here", label="Close Window")