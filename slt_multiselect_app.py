import streamlit as st

st.header('st.multiselect')

# Correct options and default selections
options = st.multiselect(
     'What are your favorite colors?',
     ['Green', 'Yellow', 'Red', 'Blue'],  # Available options
     ['Green', 'Yellow'])  # Default selected options that must match the available options

st.write('You selected:', options)
