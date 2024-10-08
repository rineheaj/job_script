import streamlit as st
from second_page_sidebars import second_page_sidebar
from config import set_title_w_param
import pandas as pd


def show_second_page(df):
    set_title_w_param(page_title='📊 Job Application Statistics')
    st.write("This page provides various statistics about your job applications.")
    
    # Total number of applications
    total_applications = len(df)
    st.metric(label="Total Applications", value=total_applications)
    
    # Number of applications by status
    status_counts = df['Status'].value_counts()
    st.write("### Applications by Status")
    st.bar_chart(status_counts)
    
    # Average time between application and response
    df['Applied Date'] = pd.to_datetime(df['Applied Date'], errors='coerce')
    df['Response Date'] = pd.to_datetime(df['Response Date'], errors='coerce')
    df['Response Time'] = (df['Response Date'] - df['Applied Date']).dt.days
    avg_response_time = df['Response Time'].mean()
    st.metric(label="Average Response Time (days)", value=f"{avg_response_time:.2f}")
    
    second_page_sidebar()


