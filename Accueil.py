import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(layout="wide")

# Personnalisez le titre de la page
st.title("DATAMINDS DashBoard")
st.write("Bienvenue sur mon tableau de bord interactif Forest Inovation !")
# Charger mes données 
carbon_data = pd.read_excel('carbon_data_imputed2.xlsx')
carbon_data1 = pd.read_excel('gross_emission.xlsx')
tc_data = pd.read_excel('tree-cover dataset.xlsx', sheet_name=5)
tc_data1 = pd.read_excel('tree_cover_loss.xlsx')
col1,col2 = st.columns(2)
with col1:
    st.subheader("Données d'émission carbone")
    st.write(carbon_data)
with col2:
    st.subheader("Données Perte couverture forestiere"   )
    st.write(tc_data)

st.subheader("Les indicateurs clés de performance")

col1_1,col2_1 = st.columns(2)
with col1_1:
    # moy_emi = carbon_data['taux_emissions_co2'].means(axis=0)
    st.subheader("Émission carbone")
    # st.write(f"emission moyenne départementale:{moy_emi}")
    
with col2_1:
    st.subheader("Perte couverture Forestiére")

# # Coordonnées du centre du Sénégal
# senegal_center = [14.4974, -14.4524]

# # Créez une carte centrée sur le Sénégal
# m = leafmap.Map(center=senegal_center, minimap_control=True)
# m.add_basemap("OpenTopoMap")
# m.to_streamlit(height=500)
