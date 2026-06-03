import streamlit as st
from analyzers.dtype_analyzer import analyze_dtypes
from analyzers.null_analyzer import null_analyzer
from analyzers.duplicate_analyzer import duplicate_analyzer

from visualizations.histogram import histogram_plot
from visualizations.heatmap import heatmap_plot

# Prevent crashes if no upload
if "original_df" not in st.session_state:

    st.warning("Please upload a dataset first.")

    st.stop()

df = st.session_state["original_df"]

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Dataset Shape
st.subheader("Dataset Shape")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1]) 

#Datatype analysis
dtype_df = analyze_dtypes(df)
st.subheader("Datatype Analysis")
st.dataframe(dtype_df)

#Null value finding
nullval_df = null_analyzer(df)
st.subheader("Null Value Analysis")
st.dataframe(nullval_df)

#Duplicates finding
dupe_df = duplicate_analyzer(df)
st.subheader("Duplicate Analysis")
st.dataframe(dupe_df)

col1, col2 = st.columns(2)

# ---------------- HISTOGRAM ----------------
with col1:
    st.subheader("Histogram Plotting")

    numeric_cols = [
    col for col in df.select_dtypes(include="number").columns
    if "Unnamed" not in col
]

    selected_column = st.selectbox(
        "Select Column",
        ["Select a column"] + list(numeric_cols)
    )

    if selected_column != "Select a column":

        fig = histogram_plot(df, selected_column)

        st.pyplot(fig)

# ---------------- HEATMAP ----------------
with col2:
    st.subheader("Correlation Heatmap")

    selected_heatmap_cols = st.multiselect(
        "Select Columns for Heatmap",
        numeric_cols
    )

    if len(selected_heatmap_cols) >= 2:

        heatmap_fig = heatmap_plot(
            df,
            selected_heatmap_cols
        )

        st.pyplot(heatmap_fig)

    else:
        st.warning("Please select at least 2 columns.")