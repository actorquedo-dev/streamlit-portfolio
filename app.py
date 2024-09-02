import streamlit as st
from menu import menu

st.set_page_config(
    page_title='◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦ ◦', 
    page_icon='images/pacman.gif'
)

menu()

st.logo(
    'images/cit-u-large-logo.png',
    link='https://cit.edu',
    icon_image='images/cit-u-small-logo.png'
)

with st.columns(3)[1]:
    st.header('Welcome! :wave:')
    st.image('images/bocchi.gif')
    st.write("Here's a dancing bocchi (idk why)")

st.write('Bocchi aside, to start exploring this app, just navigate using the sidebar! (Left side) (also pacman is eating orbs up top)')
