import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="BioPatent Radar", layout="wide")

st.title("BioPatent Radar")
st.caption("Patent Landscape Analysis — Bio-based Adhesives (2011-2026)")

df = pd.read_csv("data/bio_adhesive_patents_clustered.csv")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Patents", len(df))
col2.metric("Technology Clusters", df["cluster"].nunique())
col3.metric("Jurisdictions", df["jurisdiction"].nunique())
col4.metric("Date Range", f"{df['date_published'].min()[:4]}–{df['date_published'].max()[:4]}")

st.subheader("Patent Landscape Map")
fig_map = px.scatter(
    df,
    x="pca_x",
    y="pca_y",
    color="cluster_name",
    hover_data=["title", "jurisdiction", "date_published"],
    labels={"pca_x": "PCA Dimension 1", "pca_y": "PCA Dimension 2", "cluster_name": "Cluster"},
    height=550
)
st.plotly_chart(fig_map, use_container_width=True)

st.subheader("Cluster Distribution")
cluster_counts = df["cluster_name"].value_counts().reset_index()
cluster_counts.columns = ["cluster_name", "count"]
fig_bar = px.bar(
    cluster_counts,
    x="count",
    y="cluster_name",
    orientation="h",
    labels={"count": "Number of Patents", "cluster_name": "Cluster"},
    height=400
)
fig_bar.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("Patent Data")
selected_clusters = st.multiselect(
    "Filter by cluster",
    options=df["cluster_name"].unique(),
    default=None
)
filtered_df = df[df["cluster_name"].isin(selected_clusters)] if selected_clusters else df
st.dataframe(filtered_df[["title", "date_published", "jurisdiction", "cluster_name"]], use_container_width=True)