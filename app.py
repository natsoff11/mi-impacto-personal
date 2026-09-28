
import streamlit as st
from src.load_data import cargar_datos
st.title("Mi Impacto Personal")
st.write("Estos son tus habitos registrados:")
df = cargar_datos("data/raw/habitos.csv")
st.dataframe(df)
st.line_chart(df.set_index("fecha"))