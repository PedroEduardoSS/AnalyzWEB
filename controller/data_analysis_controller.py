import streamlit as st
import pandas as pd

class DataAnalysis:
    dataframe = pd.DataFrame()

    @st.cache_data
    def load_csv_file(_self, csv_file):
        _self.dataframe = pd.read_csv(csv_file) 
        return _self.dataframe

    def describe(_self, dataframe: pd.DataFrame):
        describe = dataframe.describe()
        return describe