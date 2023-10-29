import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title("Recherche de fonds de carte")

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
