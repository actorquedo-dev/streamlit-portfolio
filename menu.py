import streamlit as st

def menu():
    st.sidebar.page_link('app.py', label='Home', icon='🏠')
    st.sidebar.page_link('pages/about.py', label='About Me', icon='🧑‍💻')
    st.sidebar.page_link('pages/project.py', label='Projects', icon='💻')