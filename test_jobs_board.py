import streamlit as st
from second_page import show_second_page
from charts import(
    create_charts,
    display_charts,
    create_line_chart,
    create_stacked_area_chart,
    create_word_cloud,
    create_3d_scatter_plot,
    create_network_graph,
    create_test_line_chart,
)
from config import set_title, set_table_title
from style import style_df
from data_utils import(
    load_json_data, 
    load_second_page_json_data, 
    create_job_table,
)
from sidebars import sidebar

# PAGE 1 DATA
data = load_json_data()

# PAGE 2 DATA
second_page_data = load_second_page_json_data(filename="job_data_second_page.json")

# CREATE SESSION STATE
if "job_data_first_page" not in st.session_state:
    st.session_state["job_data_first_page"] = load_json_data()

if "second_page_job_data" not in st.session_state:
    st.session_state["second_page_job_data"] = second_page_data

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

    if st.button('Gen Line Chart'):
        create_test_line_chart(df=df)

    if st.button('Gen 3D Scatter Plat'):
        three_dee_fig = create_3d_scatter_plot(df=df)
        st.plotly_chart(three_dee_fig)

    if st.button('Gen Network Graph'):
        net_fig = create_network_graph(df=df)
        st.plotly_chart(net_fig)

    if st.button('Gen Word Cloud'):
        create_word_cloud(df=df)

elif page == "Random":
    show_second_page()
