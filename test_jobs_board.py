import streamlit as st
from charts import(
    create_charts, 
    display_charts, 
    create_line_chart
)
from config import set_title, set_table_title
from style import style_df
from data_utils import load_json_data, create_job_table
from sidebars import sidebar

data = load_json_data()

# CREATE SESSION STATE
if "job_data" not in st.session_state:
    st.session_state["job_data"] = load_json_data()

#SET TITLES
main_title = set_title()
table_title = set_table_title()

#INIT DF
df = create_job_table()
styled_df = style_df(df=df)

# AUTO RESIZE DF
st.dataframe(styled_df, use_container_width=True)

# SIDEBARS
sidebar(df=df)

#CREATE/SHOW CHARTS
test_pie_chart, test_bar_chart1, test_bar_chart2 = create_charts(df=df)
line_chart1 = create_line_chart(df=df)
display_charts(
    test_pie_chart, 
    test_bar_chart1, 
    line_chart1
)
