import streamlit as st

# Page d'accueil
st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <h2 style='color: teal;'>FOREST INNOVATION - DATAMINDS</h2>
    <p style='color: #555;'>Bienvenue sur la page d'acceuil Forest Innovation, une solution de gestion
            de l'activite carbone et couverture forestiere de Senegal</p>
</div>
""", unsafe_allow_html=True)
# Section 1 : Source de données et Explication

st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <h3 style='color: teal;'>Source de données et Explication</h3>
    <p style='color: #555;'>Pour élaborer cette solution innovante, nous avons exploité les jeux de données disponibles sur le site Global Forest. Ces jeux de données comprennent plusieurs feuilles, mais nous avons focalisé notre attention sur les feuilles subnationnal 1 et 2. Ces dernières étaient plus désagrégées, offrant une composition variée de variables catégorielles, quantitatives, et de dates.
</p>
</div>
""", unsafe_allow_html=True)
# Section 2 : Prétraitement

st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <h3 style='color: teal;'>Prétraitement</h3>
    <p style='color: #555;'>Face à un jeu de données riche mais complexe, notre premier défi était de gérer les nombreuses valeurs manquantes et de transformer les dates pour les rendre exploitables.
</p>
</div>
""", unsafe_allow_html=True)

# Section 3 : Exploration et Visualisation des données

st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <h3 style='color: teal;'>Exploration et Visualisation des données</h3>
    <p style='color: #555;'>Pour apporter une clarté maximale, nous avons utilisé divers outils. L'outil Tableau a été choisi pour certaines visualisations approfondies, tandis que Streamlit a été notre choix pour créer une application web immersive. À travers cette application, nous avons intégré les visualisations résultantes de notre exploration, offrant ainsi une expérience interactive et informative.
</p>
</div>
""", unsafe_allow_html=True)

# Section 3 : Exploration et Visualisation des données

st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <h3 style='color: teal;'>Model d'antrainement utilise</h3>
    <p style='color: #555;'>Pour entrainer nos model a l'aide l'aide l'algorithme KNN</p>
</div>
""", unsafe_allow_html=True)

