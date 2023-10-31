import streamlit as st
import pandas as pd

################################################################
st.title(':bar_chart: Modele de prediction:')
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
    st.write("""
             La prediction pour cette zone en perte de couverture forestiers est : 
             19293 hectars
             """)
with col2:
    st.write("""
              La prediction pour cette zone en terme d'emission de CO2 est : 
              187646 tonnes/hectar
              """)