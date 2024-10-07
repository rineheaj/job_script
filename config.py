import streamlit as st

GITHUB_REPO = st.secrets['github']['repo']
GITHUB_FILE_PATH = st.secrets['github']['file_path']
GITHUB_TOKEN = st.secrets['github']['token']


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
def set_title_w_param():
    title = st.markdown(
        '''
        <style>
        .title {{text-align: center; padding: 60px}}
        </style>
        <h1 class="title">⛔ Work In Progress</h1>
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
