import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
st.set_page_config(layout="wide")
data_name_1 = "marine_long_sample_0"
data_name_2 = "marine_short_sample_0"
# Sample DataFrame (Replace this with your actual data)
data_name = st.selectbox("Select sample:", [data_name_1, data_name_2])
df = pd.read_csv(f"{data_name}.csv")

# Streamlit UI
st.title(f"Interactive Scatter Plot for {data_name}")
df["labels"] = df["labels"].apply(lambda l: str(l))
df["short_taxa"] = df["TAXPATHSN"].apply(lambda l: l.split("|")[0])
df["medium_taxa"] = df["TAXPATHSN"].apply(lambda l: ','.join(l.split("|")[:2]))
df["log_length"] = df["_LENGTH"].apply(lambda l: np.log(l))
color_feature = st.selectbox("Select feature to color by:", ["genome_id", "RANK", "short_taxa", "medium_taxa", "log_length", "coverage", "Purity (bp) vamb", "Completeness (bp) vamb", "Purity (bp) prokbert", "Completeness (bp) prokbert"])
# Plotly Scatter Plot
fig = px.scatter(
    df, x="umap_1", y="umap_2",color=color_feature,
    hover_data=["genome_id", "RANK", "TAXPATHSN","_LENGTH"],
)

# Customize layout
fig.update_traces(marker=dict(size=1, opacity=0.8))
fig.update_layout(
    title="Scatter Plot with Hover Info",
    xaxis_title="UMAP_1 Coordinate",
    yaxis_title="UMAP_2 Coordinate",
    hovermode="closest",
)

# Show plot in Streamlit
st.plotly_chart(fig, use_container_width=True)