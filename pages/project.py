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

with st.container():
    st.header("My Projects")
    col1, col2 = st.columns((1, 2))
    col3, col4 = st.columns((1, 2))
    with col1:
        st.image('images/bocchi-2.gif')
    with col2:
        st.subheader('CIMP-Frontend')
        st.write('The frontend for our Capstone. It uses React and MUI. The project is about managing assets from our school property.')
        st.markdown('[Github Repo](https://github.com/rosnuker/CIMP-Frontend)')
    with col3:
        st.image('images/bocchi-3.gif')
    with col4:
        st.subheader('CIMP-Backend')
        st.write('The backend for our Capstone. It uses Springboot.')
        st.markdown('[Github Repo](https://github.com/reeyyyxd/CIMP_Backend)')
    