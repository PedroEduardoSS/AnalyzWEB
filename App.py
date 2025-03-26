import streamlit as st
import pandas as pd
from views.data_analysis_tab import *

st.title("Data Analysis workplace")

tab1 = st.tabs(["Data Analysis"])

with tab1:
    data_analysis_tab()
