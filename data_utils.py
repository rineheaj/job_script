import json
import pandas as pd
import streamlit as st

def create_job_table():
    df = pd.DataFrame(st.session_state["job_data"])
    return df

##LOAD DATA
def load_json_data():
    try:
        with open("job_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# SAVE DATA
def save_json_data(data):
    with open("job_data.json", "w") as f:
        json.dump(data, f, indent=4)

#CREATE DF
def create_job_table():
    df = pd.DataFrame(st.session_state["job_data"])
    return df

def create_new_job(app_date, co, pos, status):
    job = {
        'Applied Date': str(app_date),
        'Company': co,
        'Position': pos,
        'Status': status
    }
    return job

def check_used_mem():
    pass