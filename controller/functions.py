import streamlit as st
import pandas as pd

@st.cache_data
def load_csv_file(csv_file):
    return pd.read_csv(csv_file)
