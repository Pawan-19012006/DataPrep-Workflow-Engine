import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Agentic EDA System",
    layout="wide"
)

st.title("Agentic EDA + Data Cleaning System")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    # Store globally in session
    st.session_state["original_df"] = df
    
    #Resets the working df
    st.session_state["working_df"] = df.copy()

    st.success("File Uploaded Successfully!")

    st.info(
        "Use the sidebar to navigate "
        "to Analysis or Transformations."
    )