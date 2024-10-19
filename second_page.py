import streamlit as st
from second_page_sidebars import second_page_sidebar
from config import set_title_w_param
from data_utils import create_second_page_job_table
import pandas as pd


def show_second_page():
    set_title_w_param(page_title='📊 Job Application Statistics')
    st.write("This page provides various statistics about your job applications.")
    
    df = create_second_page_job_table()
    
    total_applications = len(df)
    st.metric(label="Total Applications", value=total_applications)
    
    status_counts = df['Status'].value_counts()
    st.write("### Applications by Status")
    st.bar_chart(status_counts)
    
    #---Convert dfs---
    df['Response Date'] = pd.to_datetime(df['Response Date'], format='%Y-%m-%d')
    df['Applied Date'] = pd.to_datetime(df['Applied Date'], format='%Y-%m-%d')

    st.write(df[['Response Date', 'Applied Date', 'Response Time']])

    #---Calculate avg response time---
    df['Response Time'] = (df['Response Date'] - df['Applied Date']).dt.days
    avg_response_time = df['Response Time'].dropna().mean()
    st.metric(label="Average Response Time (days)", value=f"{avg_response_time:.2f}")
    
    second_page_sidebar(df=df)


