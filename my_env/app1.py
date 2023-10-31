import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


st.title("Application de distribution")
st.subheader("Auteur: Almamy Camara")
st.write("Cette application permet d'afficher la distribution normale"
         "Elle perment a l'utilisateur de saisir le titre et les bins ")
data = np.random.normal(size=100)
df = pd.DataFrame(data, columns= ["serienormale"])
st.write(df.head())
bins_data = st.number_input(
    label= "Saisir un bin",
    min_value=10,
    value=20
)
my_title = st.text_input(
    label="Saisir titre de l'histogramme"
)
fig, ax = plt.subplots()
ax.hist(df.serienormale, bins=bins_data)
plt.title(my_title)
st.pyplot(fig)