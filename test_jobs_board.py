import streamlit as st
from charts import create_charts, display_charts
from config import set_title, set_table_title
from style import style_df
from data_utils import load_json_data, create_job_table
from sidebars import sidebar

data = load_json_data()

# CREATE SESSION STATE
if "job_data" not in st.session_state:
    st.session_state["job_data"] = load_json_data()

# SET TITLE
main_title = set_title()

# TABLE TITLE
table_title = set_table_title()

# CREATE DF
df = create_job_table()

styled_df = style_df(df=df)

# AUTO RESIZE DF
st.dataframe(styled_df, use_container_width=True)

# SIDEBARS
sidebar(df=df)

pie_chart, bar_chart1, bar_chart2 = create_charts(df=df)
display_charts(pie_chart, bar_chart1, bar_chart2)
