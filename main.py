import streamlit as st

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# Titre de la page
st.title("Notre site est en construction...")

# Centre le contenu en utilisant une colonne
col1, col2, col3 = st.columns([1, 1, 1])

# Le bouton "Nous Contacter" se trouve dans la colonne du milieu (col2)
with col2:
  st.write("")
  # Bouton "Nous Contacter" qui redirige vers le lien Calendly
  url = "https://calendly.com/jonathan-yana-qolaig"
  st.link_button("Nous Contacter", url = url, type = "primary")
