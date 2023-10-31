import streamlit as st
import numpy as np
import pandas as pd

st.title("New application")
st.subheader("Auteur: Almamy Camara")
st.markdown("***Ceci est un test au format gras et italic grace a mackdown***")

r_data = np.random.normal(size=1000)

st.line_chart(r_data)
data_bar = pd.DataFrame(
    [100, 80, 40,70],
    ['A', 'B', 'C', 'D']
)

st.bar_chart(data_bar)