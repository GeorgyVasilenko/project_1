import streamlit as st
import pandas as pd
from scripts.visualization import plot_girls_distribution

st.title("Анализ русских рэп-клипов")
df = pd.read_csv('../data/rap_videos.csv')

st.header("Основные статистики")
st.dataframe(df.describe())

st.header("Распределение девушек по клипам")
plot_girls_distribution(df)
st.pyplot()
