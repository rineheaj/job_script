import altair as alt
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import plotly.express as px
import matplotlib.pyplot as plt
import networkx as nx
import plotly.graph_objects as go


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

    # APPLICATIONS OVER TIME BAR CHART
    df["Applied Date"] = pd.to_datetime(df["Applied Date"])
    applications_over_time = df.groupby([df["Applied Date"].dt.to_period("M"), "Status"]).size().reset_index(name="Count")
    applications_over_time.columns = ["Applied Date", "Status", "Count"]
    chart2 = (
        alt.Chart(applications_over_time)
        .mark_bar()
        .encode(
            x="Applied Date",
            y="Count",
            color="Status",
            tooltip=["Applied Date", "Status", "Count"],
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

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        text
    )

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)


def create_3d_scatter_plot(df):
    fig = px.scatter_3d(df, x="Applied Date", y="Company", z="Status", color="Status")
    return fig


def create_network_graph(df):
    G = nx.Graph()

    # Add nodes and edges (example: companies and positions)
    for _, row in df.iterrows():
        G.add_node(row["Company"], type="company")
        G.add_node(row["Position"], type="position")
        G.add_edge(row["Company"], row["Position"])

    pos = nx.spring_layout(G)
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        hoverinfo="text",
        marker=dict(
            showscale=True,
            colorscale="YlGnBu",
            size=10,
            colorbar=dict(
                thickness=15,
                title="Node Connections",
                xanchor="left",
                titleside="right",
            ),
        ),
    )

    node_text = []
    for node in G.nodes():
        node_text.append(node)
    node_trace.text = node_text

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title="Network Graph",
            titlefont_size=16,
            showlegend=False,
            hovermode="closest",
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
        ),
    )
    return fig


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
