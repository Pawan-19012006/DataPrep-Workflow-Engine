import streamlit as st
import pandas as pd
from analyzers.dtype_analyzer import analyze_dtypes

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