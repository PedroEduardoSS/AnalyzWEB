import streamlit as st
import pandas as pd
from controller.data_analysis_controller import *

data_analysis_controller = DataAnalysis()

def data_analysis_tab():
    st.header("Data")
    uploaded_file= st.file_uploader("Choose a file", key="data")
    if uploaded_file is not None:
        dataframe = data_analysis_controller.load_csv_file(uploaded_file)
        
        df = st.data_editor(dataframe, num_rows="dynamic")
        st.button("Describe data", on_click=lambda: describe_place.write(data_analysis_controller.describe(df)))
        describe_place = st.container()