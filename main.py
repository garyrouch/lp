import streamlit as st

# Titre de la page
st.title("Notre Site est en construction...")

# Centre le contenu en utilisant une colonne
col1, col2, col3 = st.columns([1, 1, 1])

# Le bouton "Nous Contacter" se trouve dans la colonne du milieu (col2)
with col2:
  # Bouton "Nous Contacter" qui redirige vers le lien Calendly
  url = "https://calendly.com/jonathan-yana-qolaig"
  st.link_button("Nous Contacter", url = url, type = "primary")
