import streamlit as st
import pandas as pd
from data_utils import save_second_page_json_data, create_second_page_job_entry
from github import commit_second_page_to_github
from sidebars import check_used_mem

def refresh_page():
    if st.sidebar.button("Refresh Page"):
        st.session_state.update()

def add_mem_button():
    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: orange;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2 px;
            cursor: pointer;
            border-radius: 4px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.sidebar.button("Check Memory Usage"):
        used_memory = check_used_mem()
        if used_memory <= 200:
            st.sidebar.error(
                f"Memory Usage: {used_memory:.2f} MB\n"
                f"Use more memory"
            )
        elif used_memory >= 200:
            st.sidebar.info('That is better usage.')

def add_job():
    st.sidebar.subheader("➕ Add New Job Application")
    company = st.sidebar.text_input("Company")
    position = st.sidebar.text_input("Position")
    status = st.sidebar.selectbox(
        "Status", ["Applied", "Interviewing", "Offer", "Rejected"]
    )
    applied_date = st.sidebar.date_input("Applied Date")
    response_date = st.sidebar.date_input("Response Date", value=None)

    if st.sidebar.button("Add Job"):
        new_job = create_second_page_job_entry(
            app_date=applied_date, 
            co=company, 
            pos=position, 
            status=status, 
            response_date=response_date
        )

        if "second_page_job_data" not in st.session_state:
            st.session_state["second_page_job_data"] = []
        st.session_state["second_page_job_data"].append(new_job)
        save_second_page_json_data(st.session_state["second_page_job_data"])
        commit_second_page_to_github(st.session_state["second_page_job_data"])
        st.sidebar.success(f"Job added: {company} - {position} - {status}")
        st.write(st.session_state["second_page_job_data"])  # Debug statement

def update_job_status(df):
    st.sidebar.subheader("🔄 Update Job Status")
    job_to_update = st.sidebar.selectbox(
        "Select Job to Update", df["Position"].unique()
    )
    new_status = st.sidebar.selectbox(
        "New Status", ["Applied", "Interviewing", "Offer", "Rejected"]
    )

    if st.sidebar.button("Update Status"):
        index_to_update = df[df["Position"] == job_to_update].index[0]
        st.session_state["second_page_job_data"][index_to_update]["Status"] = new_status
        save_second_page_json_data(st.session_state["second_page_job_data"])
        commit_second_page_to_github(st.session_state["second_page_job_data"])
        st.sidebar.success(f"Status updated for {job_to_update} to {new_status}")

def update_response_date(df):
    st.sidebar.subheader("📅 Update Response Date")
    job_to_update = st.sidebar.selectbox(
        "Select Job to Update", df["Position"].unique()
    )
    new_response_date = st.sidebar.date_input("New Response Date")

    if st.sidebar.button("Update Response Date"):
        index_to_update = df[df["Position"] == job_to_update].index[0]
        st.session_state["second_page_job_data"][index_to_update]["Response Date"] = str(new_response_date)
        applied_date = pd.to_datetime(st.session_state["second_page_job_data"][index_to_update]["Applied Date"])
        days_to_response = (new_response_date - applied_date).days
        st.session_state["second_page_job_data"][index_to_update]["Days to Response"] = days_to_response
        save_second_page_json_data(st.session_state["second_page_job_data"])
        commit_second_page_to_github(st.session_state["second_page_job_data"])
        st.sidebar.success(f"Response date updated for {job_to_update} to {new_response_date}")

def delete_job(df):
    st.sidebar.subheader("🗑️ Delete a Job Listing")
    job_to_del = st.sidebar.selectbox("Select Job to Delete", df["Position"].unique())

    if st.sidebar.button("Delete a Job"):
        i_to_del = df[df["Position"] == job_to_del].index[0]
        st.session_state["second_page_job_data"].pop(i_to_del)
        save_second_page_json_data(st.session_state["second_page_job_data"])
        commit_second_page_to_github(st.session_state["second_page_job_data"])
        st.sidebar.success(f'Job "{job_to_del}" deleted')

def second_page_sidebar(df):
    refresh_page()
    add_mem_button()
    add_job()
    update_job_status(df)
    update_response_date(df)
    delete_job(df)
