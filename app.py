import streamlit as st
import pandas as pd
from analyzers.dtype_analyzer import analyze_dtypes
from analyzers.null_analyzer import null_analyzer
from analyzers.duplicate_analyzer import duplicate_analyzer
from visualizations.histogram import histogram_plot
from visualizations.heatmap import heatmap_plot

st.set_page_config(page_title="Agentic EDA System", layout="wide")

st.title("Agentic EDA + Data Cleaning System")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    #If the file is csv
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.success("File Uploaded Successfully!")

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

    dtype_df = analyze_dtypes(df)
    st.subheader("Datatype Analysis")
    st.dataframe(dtype_df)

    nullval_df = null_analyzer(df)
    st.subheader("Null Value Analysis")
    st.dataframe(nullval_df)

    dupe_df = duplicate_analyzer(df)
    st.subheader("Duplicate Analysis")
    st.dataframe(dupe_df)

    st.subheader("Histogram Plotting")
    numeric_cols = df.select_dtypes(include="number").columns
    selected_column = st.selectbox(
    "Select Column",
    numeric_cols
)
    fig = histogram_plot(df, selected_column)
    st.pyplot(fig)

    st.subheader("Correlation Heatmap")

    numeric_cols = df.select_dtypes(include="number").columns

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