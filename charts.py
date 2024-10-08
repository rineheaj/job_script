import altair as alt
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def create_charts(df):
    # TEST PIE CHART
    status_counts = df["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]
    chart1 = (
        alt.Chart(status_counts)
        .mark_arc()
        .encode(
            theta=alt.Theta(field="Count", type="quantitative"),
            color=alt.Color(field="Status", type="nominal"),
            tooltip=["Status", "Count"],
        )
    )

    # CREATE TEST BAR CHART
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x="Company",
            y="count()",
            color="Status",
            tooltip=["Company", "Position", "Status"],
        )
    )

    # TEST BAR CHART 2
    chart2 = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x="Status",
            y="count()",
            color="Status",
            tooltip=["Company", "Position", "Status"],
        )
    )

    return chart1, chart, chart2


def create_line_chart(df):
    df["Applied Date"] = pd.to_datetime(
        df["Applied Date"], format="%Y-%m-%d", errors="coerce"
    )

    agg_df = df.groupby(["Applied Date", "Status"]).size().reset_index(name="Count")

    line_chart = (
        alt.Chart(agg_df)
        .mark_line()
        .encode(
            x="Applied Date:T",  # Temporal data type for dates
            y="Count:Q",  # Quantitative data type for counts
            color="Status:N",  # Nominal data type for statuses
            tooltip=["Applied Date:T", "Status:N", "Count:Q"],
        )
        .interactive()
    )
    return line_chart


def create_stacked_area_chart(df):
    df["Applied Date"] = pd.to_datetime(
        df["Applied Date"], format="%Y-%m-%d", errors="coerce"
    )
    agg_df = df.groupby(["Applied Date", "Status"]).size().reset_index(name="Count")

    stacked_area_chart = (
        alt.Chart(agg_df)
        .mark_area()
        .encode(
            x="Applied Date:T",
            y="Count:Q",
            color="Status",
            tooltip=["Applied Date:T", "Status:N", "Count:Q"],
        )
    )
    return stacked_area_chart


def create_word_cloud(df):

    text = " ".join(df["Company"].dropna().tolist())

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        text
    )

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt


def display_charts(*charts):
    # CSS STYLE FOR CHARTS/GRAPHS
    st.markdown(
        """
        <style>
        .center {display: flex; justify-content: center;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # DISPLAY CHARTS/GRAPHS WITH MARKDOWN/CSS APPLIED
    for chart in charts:
        st.markdown('<div class="center">', unsafe_allow_html=True)
        st.altair_chart(chart, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
