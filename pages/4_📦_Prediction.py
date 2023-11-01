import streamlit as st
import pandas as pd

################################################################
st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <h2 style='color: teal; text-align: center;' >Modele de prediction</h2>
    
</div>
""", unsafe_allow_html=True)
CO2_df = pd.read_excel("gross_emission.xlsx")
TCL_df = pd.read_excel("tree_cover_loss.xlsx")
CO2_df['year'] = pd.to_datetime(CO2_df['year'], format='%Y')
TCL_df['year'] = pd.to_datetime(TCL_df['year'], format='%Y')
min_date = pd.to_datetime(TCL_df["year"]).min()
max_date = pd.to_datetime(TCL_df['year']).max()
# 

countries = CO2_df["country"].unique()
regions = CO2_df["region"].unique()
departments = CO2_df["department"].unique()
   
def user_input(country, region, departements):
   country = st.sidebar.selectbox('Country', countries)
   region= CO2_df[CO2_df["country"] == country]["region"]
   region = st.sidebar.selectbox('Région', regions)
   departement= CO2_df[CO2_df["region"] == region]["department"]
   departement = st.sidebar.selectbox('Department', departements)
   year = pd.to_datetime(st.sidebar.date_input(
        "Date de début : ", value=min_date, min_value=min_date, max_value=max_date))
   
   data = {
      'Country': country,
      'Region': region,
      'Department': departement,
      'Year': year
   }
   user_parameters = pd.DataFrame(data, index=[0])
   return user_parameters

df = user_input(countries, regions, departments)


st.write(df)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <p style='color: black;' >La prediction pour cette zone en perte de couverture forestiers est : 
             19293 hectars</h3>
    
</div>
""", unsafe_allow_html=True)
    
with col2:
      st.markdown("""
<div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px;'>
    <p style='color: black;' >La prediction pour cette zone en terme d'emission de carbone est : 
             19293 hectars</h3>
    
</div>
""", unsafe_allow_html=True)
      

# # Charger le modèle depuis le fichier pickle
# with open('model_regress.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)
# st.title('prediction')
# # Saisie utilisateur pour la prédiction
# user_input = st.number_input('Entrez une valeur :', min_value=0)
# # Prédiction avec le modèle chargé
# prediction = model.predict([[user_input]])[0]