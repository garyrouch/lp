import streamlit as st

# Titre de la page
st.title("Notre Site est en construction...")

# Bouton "Nous Contacter" qui redirige vers le lien Calendly
url = "https://calendly.com/jonathan-yana-qolaig"
st.link_button("Nous Contacter", url = url)
