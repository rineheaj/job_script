import requests
import json
import base64
from config import GITHUB_FILE_PATH, GITHUB_REPO, GITHUB_TOKEN
import streamlit as st
from datetime import datetime


#CONNECT TO GITHUB
def commit_to_github(data):
    url = f'https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        response_json = response.json()

        if 'sha' in response_json:
            sha = response_json['sha']
        else:
            st.error('SHA key not found in the response.')
            return

        content = base64.b64encode(
            json.dumps(data).encode('utf-8')
        ).decode('utf-8')

        commit_data = {
            'message': f'Auto-Updated job data {datetime.now().isoformat()}\n{content}',
            'content': content,
            'sha': sha
        }

        response = requests.put(url, 
                                headers=headers, 
                                data=json.dumps(commit_data))
        response.raise_for_status()

        if response.status_code == 200:
            st.success('Changes committed to GitHub successfully')
        else:
            st.error('Failed to commit changes to GitHub.')

    except requests.exceptions.RequestException as e:
        st.error(f'An error occurred: {e}')
    finally:
        st.info('GitHub action has completed.')
    