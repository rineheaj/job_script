import requests
import json
import base64
from test_jobs_board import GITHUB_FILE_PATH, GITHUB_REPO, GITHUB_TOKEN
import streamlit as st
from datetime import datetime


#CONNECT TO GITHUB
def commit_to_github(data):
    url = f'https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url=url, headers=headers)
    response_json = response.json()
    
    # Check if 'sha' key exists in the response
    if 'sha' in response_json:
        sha = response_json['sha']
    else:
        st.error('SHA key not found in the response.')
        return
    
    # B64ENCODED
    content = base64.b64encode(
        json.dumps(data).encode('utf-8')
    ).decode('utf-8')

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
    