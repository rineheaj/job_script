import streamlit as st
from enums import Colors

GITHUB_REPO = st.secrets['github']['repo']
GITHUB_FILE_PATH = st.secrets['github']['file_path']
GITHUB_TOKEN = st.secrets['github']['token']
GITHUB_FILE_PATH_SECOND_JSON = st.secrets['github']['second_page_json_path']



# SET TITLE
def set_title():
    title = st.markdown(
        """
        <style>
        .title {text-align: center; padding: 60px;}
        </style>
        
        <h1 class="title">🎯 Job Application Tracker</h1>
        """,
        unsafe_allow_html=True,
    )
    return title

#SET TITLE WITH PARAM
def set_title_w_param(page_title, color):
    title = st.markdown(
        f'''
        <style>
        .title {{text-align: center; padding: 60px}}
        color: {Colors.BLUE.value};
        </style>
        <h1 class="title">{page_title}</h1>
        ''',
        unsafe_allow_html=True
    )
    return title


    

# DF TABLE TITLE
def set_table_title():
    title2 = st.markdown(
        """
        <style> .title2 {text-align: center; padding: 25px;}
        </style>

        <h1 class="title2">📋 Job Applications</h1>
        """,
        unsafe_allow_html=True,
    )
    return title2
