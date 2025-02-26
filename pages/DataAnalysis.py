import streamlit as st
import pandas as pd
from components.functions import *

st.title("Data Analysis workplace")

tab1, tab2 = st.tabs(["Create your data", "Upload your data"])

with tab1:
    pass

with tab2:
    st.header("Static data")
    uploaded_file_static = st.file_uploader("Choose a file", key="static_data")
    if uploaded_file_static is not None:
        dataframe_static = load_csv_file(uploaded_file_static)
                
        df_static = st.dataframe(dataframe_static)

    st.header("Dynamic data")
    uploaded_file_dynamic = st.file_uploader("Choose a file", key="dynamic_data")
    if uploaded_file_dynamic is not None:
        dataframe_dynamic = load_csv_file(uploaded_file_dynamic)
        
        df_dynamic = st.data_editor(dataframe_dynamic, num_rows="dynamic")
        