import os
import subprocess


readme_content = """
# 🎯 Job Application Tracker

**Job Application Tracker** is a Streamlit app designed to help you manage and track your job applications efficiently. The app allows you to add new job listings, update the status of existing applications, and visualize application data using charts and graphs.

## ✨ Features

- **Add New Job Applications**: Easily add new job listings with details such as company, position, status, and applied date.
- **Update Job Status**: Update the status of your job applications as you progress through the hiring process.
- **Delete Job Listings**: Remove job listings that are no longer relevant.
- **Visualize Application Data**: View your job application data using interactive charts and graphs.
- **GitHub Integration**: Automatically commit changes to your job data file in your GitHub repository.

## 🛠️ Installation

1. **Clone the repository**:
   \`\`\`sh
   git clone https://github.com/yourusername/job_script.git
   cd job_script
   \`\`\`

2. **Install the required dependencies**:
   \`\`\`sh
   pip install -r requirements.txt
   \`\`\`

3. **Set up Streamlit credentials**:
   If you are running the app locally, no credentials are required. If you are deploying the app, use the Streamlit interface to add your GitHub credentials.

## 🚀 Usage

1. **Run the Streamlit app**:
   \`\`\`sh
   streamlit run test_jobs_board.py
   \`\`\`

2. **Add New Job Application**:
   - Fill in the company, position, status, and applied date in the sidebar.
   - Click the "Add Job" button to add the job listing.

3. **Update Job Status**:
   - Select the job to update from the dropdown menu in the sidebar.
   - Choose the new status and click the "Update Status" button.

4. **Delete Job Listing**:
   - Select the job to delete from the dropdown menu in the sidebar.
   - Click the "Delete a Job" button to remove the job listing.

## 📊 Charts and Graphs

The app includes the following visualizations:

- **Pie Chart**: Displays the distribution of job application statuses.
- **Bar Chart 1**: Shows the count of applications per company.
- **Bar Chart 2**: Displays the count of applications per status.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
"""

# Write the README file
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)


subprocess.run(["git", "add", "README.md"])


subprocess.run(["git", "commit", "-m", "Add README file"])


subprocess.run(["git", "push", "origin", "master"])
