#               ##DONT USE ANYMORE##
# #TEST TIMELINE CHART
# import plotly.express as px

# fig = px.timeline(df, x_start="Applied Date", x_end="Applied Date", y="Company", color="Status", title='Job Application Timeline')
# st.plotly_chart(fig)

# #INTERACTIVE MAP
# m = folium.Map(location=[20,0], zoom_start=2)
# for i, row in df.iterrows():
#     folium.Marker([row['Latitude'], row['Longitude']], popup=row['Company']).add_to(m)
# st_folium(m)

# #TEST HEAT MAP
# fig, ax = plt.subplots()
# sns.heatmap(df.pivot_table(index='Company', columns='Status', aggfunc='size', fill_value=0), cmap='coolwarm', ax=ax)
# st.pyplot(fig)