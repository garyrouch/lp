import streamlit as st
import webbrowser

# Titre de la page
st.title("Notre Site est en construction...")

# Bouton "Nous Contacter" qui redirige vers le lien Calendly
if st.button("Nous Contacter"):
    url = "https://calendly.com/jonathan-yana-qolaig"
    webbrowser.open_new_tab(url)
