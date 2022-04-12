import streamlit as st
import pandas as pd

batting = pd.read_csv("Batting.csv")

data = batting[["H","G"]].iloc[0:20]
chart= st.bar_chart(data)
