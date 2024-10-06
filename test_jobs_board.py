import streamlit as st
import pandas as pd
import altair as alt
import json
import requests
from datetime import datetime
import base64
from dotenv import load_dotenv
import os

#LOAD ENV VARS
load_dotenv()
GITHUB_REPO = os.getenv('repo')
GITHUB_FILE_PATH = os.getenv('file_path')
GITHUB_TOKEN = os.getenv('token')




##LOAD DATA
def load_json_data():
    try:
        with open('job_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


#SAVE DATA
def save_json_data(data):
    with open('job_data.json', 'w') as f:
        json.dump(data, f, indent=4)

#CONNECT TO GITHUB
def commit_to_github(data):
    url = f'https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url=url, headers=headers)
    response_json = response.json()
    sha = response_json['sha']

    content = base64.b64encode(
        json.dumps(data).encode('utf-8').decode('utf-8')
    )

    commit_data = {
        'message': f'Update job data {datetime.now().isoformat()}',
        'content': content,
        'sha': sha
    }
    response = requests.put(url, 
                            headers=headers, 
                            data=json.dumps(commit_data)
    )
    if response.status_code == 200:
        st.success('Changes committed to GitHub successfully')
    else:
        st.error('Failed to commit changes to GitHub.')
    
# CREATE DATA STRUCTURE
if 'job_data' not in st.session_state:
    st.session_state['job_data'] = load_json_data()

def create_job_table():
    """
    Create a DataFrame displaying job application details.
    """
    df = pd.DataFrame(st.session_state['job_data'])
    return df



# SET TITLE
def set_title():
    title = st.markdown(
        """
        <style>
        .title {text-align: center; padding: 20px;}
        </style>
        
        <h1 class="title">🎯 Job Application Tracker</h1>
        """,
        unsafe_allow_html=True
    )
    return title

st.subheader("📋 Job Applications:")

# CREATE DF 
df = create_job_table()

# COLORS FOR DF
def status_color(val):
    """Function to return the background color based on job status."""
    if val == 'Offer':
        return 'background-color: green;'
    elif val == 'Rejected':
        return 'background-color: red;'
    elif val == 'Interviewing':
        return 'background-color: coral;'
    elif val == 'Applied':
        return 'background-color: blue;'
    else:
        return ''

# DATAFRAME STYLES
styled_df = (
    df.style
    .map(lambda x: 'background-color: gray;', subset=['Company'])
    .map(lambda x: 'background-color: darkcyan;', subset=['Position'])
    .map(status_color, subset=['Status'])
    # .map(lambda x: 'background-color: purple;', subset=['Website URL'])
    .map(lambda x: 'background-color: darkgreen;', subset=['Applied Date'])
)

#AUTO RESIZE DF
st.dataframe(styled_df, use_container_width=True)

# REFRESH PAGE BUTTON
if st.sidebar.button('Refresh Page'):
    st.session_state.update()

# ADD NEW JOB TO TABLE
st.sidebar.subheader("➕ Add New Job Application")
company = st.sidebar.text_input("Company")
position = st.sidebar.text_input("Position")
status = st.sidebar.selectbox("Status", ['Applied', 'Interviewing', 'Offer', 'Rejected'])
# website_url = st.sidebar.text_input('Website URL')
applied_date = st.sidebar.date_input('Applied Date')

# ADD JOB BUTTON
if st.sidebar.button("Add Job"):
    new_job = {
        "Applied Date": str(applied_date),
        "Company": company,
        "Position": position,
        "Status": status
    }
    # st.session_state['job_data']['Website URL'].append(website_url)
    st.session_state['job_data'].append(new_job)
    save_json_data(st.session_state['job_data'])
    st.success(f'Job added: {company} - {position} - {status}')



#UPDATE JOB STATUS
st.sidebar.subheader('🔄 Update Job Status')
job_to_update = st.sidebar.selectbox('Select Job to Update', df['Position'].unique())
new_status = st.sidebar.selectbox('New Status', [
    'Applied', 'Interviewing', 'Offer', 'Rejected'
])

if st.sidebar.button("Update Status"):
    index_to_update = df[df['Position'] == job_to_update].index[0]
    st.session_state['job_data'][index_to_update]['Status'] = new_status
    save_json_data(st.session_state['job_data'])
    st.success(f'Status updated for {job_to_update} to {new_status}')

#DELETE JOB LISTING
st.sidebar.subheader('🗑️ Delete a Job Listing')
job_to_del = st.sidebar.selectbox(
    'Select Job to Delete', df['Position'].unique()
)

if st.sidebar.button('Delete a Job'):
    i_to_del = df[df['Position'] == job_to_del].index[0]
    st.session_state['job_data'].pop(i_to_del)
    save_json_data(st.session_state['job_data'])
    st.success(f'Job "{job_to_del}" deleted')

# TEST PIE CHART
status_counts = df['Status'].value_counts().reset_index()
status_counts.columns = ['Status', 'Count']
chart1 = alt.Chart(status_counts).mark_arc().encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="Status", type="nominal"),
    tooltip=['Status', 'Count']
).properties(title='Job Application Status')
st.altair_chart(chart1)

# CREATE TEST BAR CHART 1
chart = alt.Chart(df).mark_bar().encode(
    x='Company',
    y='count()',
    color='Status',
    tooltip=['Company', 'Position', 'Status']
).properties(title='Job Application Status')
st.altair_chart(chart)

# TEST BAR CHART 2
chart2 = alt.Chart(df).mark_bar().encode(
    x='Status',
    y='count()',
    color='Status',
    tooltip=['Company', 'Position', 'Status']
).properties(title='Job Application Status')
st.altair_chart(chart2)















###DONT USE FOR NOW
# #TEST TIMELINE CHART
# import plotly.express as px

# fig = px.timeline(df, x_start="Applied Date", x_end="Applied Date", y="Company", color="Status", title='Job Application Timeline')
# st.plotly_chart(fig)

# #INTERACTIVE MAP
# m = folium.Map(location=[20,0], zoom_start=2)
# for i, row in df.iterrows():
#     folium.Marker([row['Latitude'], row['Longitude']], popup=row['Company']).add_to(m)
# st_folium(m)

# #TEST HEAT MAP
# fig, ax = plt.subplots()
# sns.heatmap(df.pivot_table(index='Company', columns='Status', aggfunc='size', fill_value=0), cmap='coolwarm', ax=ax)
# st.pyplot(fig)