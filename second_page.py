import streamlit as st
from second_page_sidebars import second_page_sidebar
from config import set_title_w_param
from data_utils import create_second_page_job_table, convert_to_string
import pandas as pd


def show_second_page():
    set_title_w_param(page_title='📊 Job Application Statistics')
    st.write("This page provides various statistics about your job applications.")
    
    df = create_second_page_job_table()

    # Perform calculations before formatting dates
    total_applications = len(df)
    status_counts = df['Status'].value_counts()

    # Calculate avg response time
    df['Response Time'] = (df['Response Date'] - df['Applied Date']).dt.days
    avg_response_time = df['Response Time'].dropna().mean()

    # Format dates to remove time component
    df = convert_to_string(df, ['Applied Date', 'Response Date'])

    # Display DataFrame and metrics
    st.dataframe(df)
    st.metric(label="Total Applications", value=total_applications)
    st.write("### Applications by Status")
    st.altair_chart(status_counts)

    # Display the subset of the DataFrame with formatted dates
    st.dataframe(df[['Response Date', 'Applied Date', 'Response Time']])
    st.metric(label="Average Response Time (days)", value=f"{avg_response_time:.2f}")

    second_page_sidebar(df=df)



