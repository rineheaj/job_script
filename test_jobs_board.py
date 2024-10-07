import streamlit as st
from second_page import show_second_page
from charts import (
    create_charts,
    display_charts,
    create_line_chart,
    create_stacked_area_chart,
)
from config import(
    set_title, 
    set_table_title,
    set_title_w_param
)
from style import style_df
from data_utils import (
    load_json_data,
    create_job_table,
)
from sidebars import sidebar

data = load_json_data()

# CREATE SESSION STATE
if "job_data" not in st.session_state:
    st.session_state["job_data"] = load_json_data()

##CHECK FOR SELECTED PAGE
page = st.sidebar.selectbox("Select a page", ["Main Page", "Random"])
if page == "Main Page":

    # SET TITLES
    main_title = set_title()
    table_title = set_table_title()

    # INIT DF
    df = create_job_table()
    styled_df = style_df(df=df)

    # AUTO RESIZE DF
    st.dataframe(styled_df, use_container_width=True)

    # SIDEBARS
    sidebar(df=df)

    # CREATE/SHOW CHARTS
    test_pie_chart, test_bar_chart1, test_bar_chart2 = create_charts(df=df)
    line_chart1 = create_line_chart(df=df)
    stacked_chart1 = create_stacked_area_chart(df=df)
    display_charts(test_pie_chart, stacked_chart1)

elif page == "Second Page":
    second_page_title = set_title_w_param(
        page_title='⛔Work In Progress'
    )
    show_second_page()
