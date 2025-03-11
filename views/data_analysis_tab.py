import streamlit as st
import pandas as pd
from controller.functions import *

def data_analysis_tab():
    st.header("Data")
    uploaded_file= st.file_uploader("Choose a file", key="data")
    if uploaded_file is not None:
        dataframe = load_csv_file(uploaded_file)
        
        df = st.data_editor(dataframe, num_rows="dynamic")

