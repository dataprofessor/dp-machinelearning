import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is app builds a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
