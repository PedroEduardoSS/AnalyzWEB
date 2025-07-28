from nicegui import events, ui
import pandas as pd
from components.data_analysis import *

data_analysis_component = DataAnalysis()

def data_analysis_tab():
    ui.html("<h1>Data</h1>").classes('text-lg')

    with ui.column(align_items="center").classes('w-full'):
        with ui.row(align_items='center').classes('w-full') as row1:
            ui.upload(label="Choose a file", on_upload=data_analysis_component.load_csv_file, auto_upload=True).classes('max-w-full')

        with ui.row(align_items="center").classes('w-full') as row2:
            ui.label('Data described').classes('text-lg')
            ui.button('Describe data', on_click=lambda: data_analysis_component.describe())

    
    """
    st.area_chart(df)
    st.bar_chart(df)
    st.line_chart(df)
    st.scatter_chart(df)
    """