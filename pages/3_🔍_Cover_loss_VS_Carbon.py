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

st.set_page_config(layout="wide")
st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <h3 style='color: teal; text-align: center;' >Tableau de bord interactif de correlation de la perte de couverture forestiere et emission CO2</h3>
    
</div>
""", unsafe_allow_html=True)
tableau_dashboard_code = """
        <iframe src="https://public.tableau.com/views/competion_ias/Tableaudebord1?:language=fr-FR&:display_count=n&:origin=viz_share_link&:showVizHome=no&:embed=true" width="100%" height="700" frameborder="0"></iframe>
"""

st.markdown(tableau_dashboard_code, unsafe_allow_html=True)



with st.expander("Voir la démo"):
    st.image("https://i.imgur.com/0SkUhZh.gif")

row1_col1, row1_col2 = st.columns([3, 1])
width = None
height = 800
tiles = None

with row1_col2:

    checkbox = st.checkbox("Rechercher les services de cartes rapides (QMS)")
    keyword = st.text_input("Entrez un mot-clé de recherche et appuyez sur Entrée :")
    empty = st.empty()

    if keyword:
        # Recherche de services XYZ liés au Sénégal
        options = leafmap.search_xyz_services(keyword=keyword + " Senegal")
        if checkbox:
            # Recherche de services QMS liés au Sénégal
            options = options + leafmap.search_qms(keyword=keyword + " Senegal")

        tiles = empty.multiselect("Sélectionnez les fonds de carte XYZ à ajouter à la carte :", options)

    with row1_col1:
        m = leafmap.Map()

        if tiles is not None:
            for tile in tiles:
                m.add_xyz_service(tile)

        m.to_streamlit(width, height)

# Relation entre la densité de couverture arborée et les émissions de carbone (nuage de points)
st.header("Relation entre la densité de couverture arborée et les émissions de carbone")
fig_scatter = px.scatter(carbon_data, x="umd_tree_cover_density_2000__threshold",
                         y="gfw_forest_carbon_gross_emissions__Mg_CO2e_yr-1", color="region",
                         labels={"umd_tree_cover_density_2000__threshold": "Densité de couverture arborée 2000",
                                 "gfw_forest_carbon_gross_emissions__Mg_CO2e_yr-1": "Émissions de CO2 (Mg_CO2e/année)"})
st.plotly_chart(fig_scatter)
st.write("Tableau")