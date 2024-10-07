import streamlit as st
from github import commit_to_github
from charts import create_charts, display_charts
from config import set_title, set_table_title
from data_utils import load_json_data, save_json_data, create_job_table
from style import style_df

data = load_json_data()

# CREATE DATA STRUCTURE
if "job_data" not in st.session_state:
    st.session_state["job_data"] = load_json_data()

#SET TITLE
main_title = set_title()

#TABLE TITLE
table_title = set_table_title()

# CREATE DF
df = create_job_table()

styled_df = style_df(df=df)

# AUTO RESIZE DF
st.dataframe(styled_df, use_container_width=True)

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
    new_job = {
        "Applied Date": str(applied_date),
        "Company": company,
        "Position": position,
        "Status": status,
    }
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

pie_chart, bar_chart1, bar_chart2 = create_charts(df=df)
display_charts(pie_chart, bar_chart1, bar_chart2)