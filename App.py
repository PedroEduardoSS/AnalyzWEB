import streamlit as st
import pandas as pd
from views.data_analysis_tab import *

# Função para carregar o DataFrame (pode ser substituída por sua fonte de dados)
def load_data():
    data = {'Nome': ['Alice', 'Bob', 'Charlie'],
            'Idade': [25, 30, 28],
            'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']}
    return pd.DataFrame(data)

# Função para criar um novo registro

    
st.title("Data Analysis workplace")

tab1, tab2, tab3 = st.tabs(["Data Analysis", "Machine Learning", "Scraping"])

with tab1:
    data_analysis_tab()

with tab2:
    pass

with tab3:
    pass