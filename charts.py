import altair as alt
import streamlit as st

def create_charts(df):
    # TEST PIE CHART
    status_counts = df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    chart1 = alt.Chart(status_counts).mark_arc().encode(
        theta=alt.Theta(field="Count", type="quantitative"),
        color=alt.Color(field="Status", type="nominal"),
        tooltip=['Status', 'Count']
    )

    # CREATE TEST BAR CHART
    chart = alt.Chart(df).mark_bar().encode(
        x='Company',
        y='count()',
        color='Status',
        tooltip=['Company', 'Position', 'Status']
    )

    # TEST BAR CHART 2
    chart2 = alt.Chart(df).mark_bar().encode(
        x='Status',
        y='count()',
        color='Status',
        tooltip=['Company', 'Position', 'Status']
    )

    return chart1, chart, chart2


def display_charts(chart1, chart, chart2):
    # CSS STYLE FOR CHARTS/GRAPHS
    st.markdown(
        '''
        <style>
        .center {display: flex; justify-content: center;}
        </style>
        ''',
        unsafe_allow_html=True
    )

    # DISPLAY CHARTS/GRAPHS WITH MARKDOWN/CSS APPLIED
    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.altair_chart(chart1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.altair_chart(chart, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.altair_chart(chart2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)