import streamlit as st
import pandas as pd
from data_utils import save_json_data, create_new_job
from github import commit_to_github




def sidebar(df):
    # REFRESH PAGE BUTTON
    if st.sidebar.button("Refresh Page"):
        st.session_state.update()

    # ADD NEW JOB TO TABLE
    st.sidebar.subheader("➕ Add New Job Application")
    company = st.sidebar.text_input("Company")
    position = st.sidebar.text_input("Position")
    status = st.sidebar.selectbox(
        "Status", ["Applied", "Interviewing", "Offer", "Rejected"]
    )
    # website_url = st.sidebar.text_input('Website URL')
    applied_date = st.sidebar.date_input("Applied Date")

    # ADD JOB BUTTON
    if st.sidebar.button("Add Job"):
        new_job = create_new_job(
            app_date=applied_date,
            co=company,
            pos=position,
            status=status
        )
        # st.session_state['job_data']['Website URL'].append(website_url)
        st.session_state["job_data"].append(new_job)
        save_json_data(st.session_state["job_data"])
        commit_to_github(st.session_state["job_data"])
        st.success(f"Job added: {company} - {position} - {status}")


    # UPDATE JOB STATUS
    st.sidebar.subheader("🔄 Update Job Status")
    job_to_update = st.sidebar.selectbox("Select Job to Update", df["Position"].unique())
    new_status = st.sidebar.selectbox(
        "New Status", ["Applied", "Interviewing", "Offer", "Rejected"]
    )

    if st.sidebar.button("Update Status"):
        index_to_update = df[df["Position"] == job_to_update].index[0]
        st.session_state["job_data"][index_to_update]["Status"] = new_status
        save_json_data(st.session_state["job_data"])
        commit_to_github(st.session_state["job_data"])
        st.success(f"Status updated for {job_to_update} to {new_status}")

    # DELETE JOB LISTING
    st.sidebar.subheader("🗑️ Delete a Job Listing")
    job_to_del = st.sidebar.selectbox("Select Job to Delete", df["Position"].unique())

    if st.sidebar.button("Delete a Job"):
        i_to_del = df[df["Position"] == job_to_del].index[0]
        st.session_state["job_data"].pop(i_to_del)
        save_json_data(st.session_state["job_data"])
        commit_to_github(st.session_state["job_data"])
        st.success(f'Job "{job_to_del}" deleted')