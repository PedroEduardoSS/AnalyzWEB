import streamlit as st
import pandas as pd
from views.data_analysis_tab import *

st.title("Data Analysis workplace")

tab1, tab2 = st.tabs(["Data Analysis", "extraTab"])

with tab1:
    data_analysis_tab()

with tab2:
    pass