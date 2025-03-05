import streamlit as st
import pandas as pd
from components.functions import *

st.title("Data Analysis workplace")

tab1, tab2, tab3 = st.tabs(["Data Analysis", "Machine Learning", "Scraping"])

with tab1:
    st.header("Data")
    uploaded_file= st.file_uploader("Choose a file", key="data")
    if uploaded_file is not None:
        dataframe = load_csv_file(uploaded_file)
        
        df = st.data_editor(dataframe, num_rows="dynamic")

with tab2:
    pass

with tab3:
    pass