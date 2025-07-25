from nicegui import events, ui
import pandas as pd
from controller.data_analysis_controller import *

data_analysis_controller = DataAnalysis()

def data_analysis_tab():
    ui.html("<h1>Data</h1>")

    ui.upload(label="Choose a file", on_upload=data_analysis_controller.load_csv_file, auto_upload=True).classes('max-w-full')
    
    
    """
    df = st.data_editor(dataframe, num_rows="dynamic")
    st.button("Describe data", on_click=lambda: describe_place.write(data_analysis_controller.describe(df)))
    describe_place = st.container()

    
    st.area_chart(df)
    st.bar_chart(df)
    st.line_chart(df)
    st.scatter_chart(df)
    """