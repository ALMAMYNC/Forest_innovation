import streamlit as st
import leafmap.foliumap as leafmap



col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

# Center the map on Senegal
senegal_center = [14.4974, -14.4524]
zoom_level = 7

with col2:
    basemap = st.selectbox("Select a basemap:", options, index)

with col1:
    m = leafmap.Map(center=senegal_center, zoom=zoom_level, locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
    m.add_basemap(basemap)
    m.to_streamlit(height=700)

import pandas as pd

# Charger le jeu de données
data = pd.read_excel("../../../tree-cover dataset.xlsx",sheet_name=5)  # Remplacez par le chemin de votre fichier

# Filtrer les données pour le Sénégal
senegal_data = data[data["country"] == "Senegal"]
st.write(senegal_data)

# Définir les coordonnées géographiques approximatives pour les régions et départements
coordinates = {
    "Dakar": (14.6928, -17.4467),
    "Guédiawaye": (14.7113, -17.4544),
    "Pikine": (14.7634, -17.3906),
    "Rufisque": (14.7219, -17.2731),
    "Bambey": (14.6816, -16.4467),
    "Diourbel": (14.6611, -16.2339),
    "Mbacké": (14.7894, -16.6264),
    "Fatick": (14.3412, -16.4125),
    "Foundiougne": (14.1258, -16.4550),
    "Gossas": (14.5110, -16.5423),
    "Birkilane": (13.8065, -15.9225),
    "Kaffrine": (14.1044, -15.5485),
    "Koungheul": (13.9813, -15.4862),
    "Malème Hodar": (13.6409, -15.6200),
    "Guinguinéo": (13.6600, -16.2604),
    "Nioro du Rip": (13.7190, -16.3652)
}


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")


with col1:
    m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
    m.add_basemap(basemap)

    # Ajouter des marqueurs pour les coordonnées géographiques des régions et départements
    for location, (lat, lon) in coordinates.items():
        m.add_marker([lat, lon], title=location)  # Utilisez une liste pour spécifier la position

    m.to_streamlit(height=700)
