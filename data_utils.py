import json
import pandas as pd
import streamlit as st

# LOAD DATA
def load_json_data():
    try:
        with open("job_data.json", "r") as f:
            st.session_state["job_data_first_page"] = json.load(f)
    except FileNotFoundError:
        st.session_state["job_data_first_page"] = []

# SAVE DATA
def save_json_data(data):
    with open("job_data.json", "w") as f:
        json.dump(data, f, indent=4)

# CREATE DF
def create_job_table():
    df = pd.DataFrame(st.session_state["job_data_first_page"])
    return df

# CREATE NEW JOB
def create_new_job(app_date, co, pos, status):
    job = {
        'Applied Date': str(app_date),
        'Company': co,
        'Position': pos,
        'Status': status
    }
    return job

# CREATE NEW SECOND PAGE JOB
def create_second_page_job_entry(app_date, co, pos, status, response_date=None):
    job = {
        'Applied Date': str(app_date),
        'Company': co,
        'Position': pos,
        'Status': status,
        'Response Date': str(response_date) if response_date else None,
        'Days to Response': None
    }
    return job

# CREATE SECOND DF
def create_second_page_job_table():
    df = pd.DataFrame(st.session_state['second_page_job_data'])
    df = convert_to_datetime(df, ['Applied Date', 'Response Date'])
    if 'Days to response' in df.columns:
        df['Days to response'] = (df['Response Date'] - df['Applied Date']).dt.days
    return df

def convert_to_datetime(df, columns):
    for column in columns:
        df[column] = pd.to_datetime(df[column], format='%Y-%m-%d', errors='coerce')
    return df

def convert_to_string(df, columns):
    for c in columns:
        df[c] = df[c].dt.strftime('%Y-%m-%d')
    return df



# LOAD SECOND JSON DATA
def load_second_page_json_data(filename='job_data_second_page.json'):
    try:
        with open(filename, 'r') as f:
            st.session_state["second_page_job_data"] = json.load(f)
    except FileNotFoundError:
        st.session_state["second_page_job_data"] = []

# SAVE SECOND JSON DATA
def save_second_page_json_data(data, filename='job_data_second_page.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
