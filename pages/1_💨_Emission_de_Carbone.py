import streamlit as st
import leafmap.foliumap as leafmap
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

# Charger vos données
carbon_data = pd.read_excel('carbon_data_imputed1.xlsx')
carbon_data1 = pd.read_excel('carbon_data_imputed2.xlsx')
carbon_data_simplified = pd.read_excel('gross_emission.xlsx')

# Définir le titre et la description de la page
st.set_page_config(layout="wide")
st.title("Forest Innovation")
st.write("Bienvenue sur le tableau de bord de l'emission de CO2 !")

tableau_dashboard_code = """
        <iframe src="https://public.tableau.com/views/competion_ias/Tableau_Bord_Emission_CO2?:language=fr-FR&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true" width="100%" height="700" frameborder="0"></iframe>
"""

st.markdown(tableau_dashboard_code, unsafe_allow_html=True)



loss_columns = ['tc_loss_ha_2001', 'tc_loss_ha_2002', 'tc_loss_ha_2003', 'tc_loss_ha_2004', 'tc_loss_ha_2005', 'tc_loss_ha_2006', 'tc_loss_ha_2007', 'tc_loss_ha_2008', 'tc_loss_ha_2009', 'tc_loss_ha_2010', 'tc_loss_ha_2011', 'tc_loss_ha_2012', 'tc_loss_ha_2013', 'tc_loss_ha_2014', 'tc_loss_ha_2015', 'tc_loss_ha_2016', 'tc_loss_ha_2017', 'tc_loss_ha_2018', 'tc_loss_ha_2019', 'tc_loss_ha_2020', 'tc_loss_ha_2021', 'tc_loss_ha_2022']

# Graphique d'évolution des émissions de carbone par région
st.header("Évolution des émissions de carbone par région")
fig = px.line(carbon_data_simplified, x='region', y="co2_gross_emission", color='region',
              labels={"année": "Année", "value": "Émissions de CO2 (Mg_CO2e)"})
st.plotly_chart(fig)

# Section pour afficher la carte split-panel
st.header("Split-panel Map")
senegal_center = [14.4974, -14.4524]
zoom_level = 7
with st.expander("Voir le code source"):
    with st.echo():
        m = leafmap.Map(center=senegal_center, zoom=zoom_level)
        m.split_map(left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover')
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')
m.to_streamlit(height=700)

# Carte choroplèthe des émissions de carbone par région
st.header("Carte choroplèthe des émissions de carbone par région")
fig_map = px.choropleth(carbon_data1, locations="region", locationmode="country names", color="taux_emissions_co2")
st.plotly_chart(fig_map)

# Évolution des émissions de carbone par année (graphique linéaire)
st.header("Évolution des émissions de carbone par année")
fig_line = px.line(carbon_data_simplified, x='year', y="co2_gross_emission", color="region",
                   labels={"year": "Année", "co2_gross_emission": "Émissions de CO2 (Mg_CO2e)"})
st.plotly_chart(fig_line)

# Distribution des émissions de carbone (histogramme)
st.header("Distribution des émissions de carbone")
fig_hist = px.histogram(carbon_data_simplified, x="co2_gross_emission")
st.plotly_chart(fig_hist)



# Carte interactive des émissions de carbone par région
st.header("Carte interactive des émissions de carbone par région")
fig_map_interactive = px.scatter_geo(carbon_data_simplified, locations="region", locationmode="country names",
                                     color="co2_gross_emission", hover_name="region")
st.plotly_chart(fig_map_interactive)

# Composition des émissions de carbone par année pour chaque région (graphique à barres empilées)
st.header("Composition des émissions de carbone par année pour chaque région")
fig_stacked_bar = px.bar(carbon_data_simplified, x="year", y="co2_gross_emission", color="region", title="Composition des émissions de carbone")
st.plotly_chart(fig_stacked_bar)

