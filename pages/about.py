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
    col1, col2 = st.columns(2)
    with col1:                  
        st.title("I'm Adrian Carlo Torquedo")
        st.subheader("4th Year BSIT Student")
        st.write('At Cebu Institute of Technology - University.')
    with col2:
        st.image('images/me.jpeg')

st.write('---')

with st.container():
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("""
            Education
            - Cebu Institute of Technology - University
                - Bachelor of Science in Information Technology (2018 - Present)
                - Senior High School (2016 - 2018)
                - Junior High School (2012 - 2016)
            - Tisa II Elementary School
                - Grade 4 - 6 (2010 - 2012)
                - Grade 2 (2008 - 2009)
            - Little Angels Montessori School
                - Grade 3 (2009 - 2010)
            - Southwestern University
                - Grade 1 (2007 - 2008)       
        """)
    with col4:
        st.subheader("""
            Experiences
            - Farmtri - UI / UX Intern (September 2024 - December 2024)
            - Freelance Coding Tutor Online (2020 - Present)          
        """)
        st.subheader("""
            Coding Languages
            - Low Level
                - Assembly
                - C, C++
            - High Level
                - C#
                - Java, JavaScript
                - Python                          
        """)