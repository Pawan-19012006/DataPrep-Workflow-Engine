import streamlit as st
from transformers.missing_handler import handle_missing_values
from transformers.duplicate_handler import remove_duplicates

if "original_df" not in st.session_state:

    st.warning("Please upload a dataset first.")

    st.stop()

df = st.session_state["original_df"]

if "working_df" not in st.session_state:

    st.session_state["working_df"] = (
        st.session_state["original_df"].copy()
    )

working_df = st.session_state["working_df"]

st.title("Data Transformations")

# Missing Value Handling
with st.expander("Missing Value Handling"):
    st.subheader("Handle Missing Values")

    #Numerical cols only
    numeric_cols = [
        col for col in df.select_dtypes(include="number").columns
        if "Unnamed" not in col
    ]

    selected_columns = st.multiselect(
        "Selected Columns",
        numeric_cols
    )

    selected_method = st.selectbox(
        "Select Imputation Method",
        [
            "mean",
            "median",
            "mode",
            "drop_rows"
        ]
    )

    apply_missing = st.button(
        "Apply Missing Value Handling"
    )

    if apply_missing:
        transformed_df = handle_missing_values(
            working_df,
            selected_columns,
            selected_method
        )

        st.success(
            "Missing Value Handling Applied!"
        )

        st.subheader("Transformed Dataset Preview")

        st.dataframe(
            transformed_df.head()
        )

        # Session state allows sequential processing of each stage by temporarily storing the dataframe and to give it to the next process 
        st.session_state[
            "working_df"
        ] = transformed_df

# Duplicate Removal
with st.expander("Duplicate Removal"):
    st.subheader("Remove Duplicate Rows")

    apply_duplicates = st.button(
        "Remove Duplicates"
    )

    if apply_duplicates:
        working_df = remove_duplicates(
            st.session_state["working_df"]
        )
        st.session_state[
            "working_df"
        ]=working_df

        st.success(
            "Duplicate Rows Removed!"
        )

        st.subheader(
            "Updated Dataset Preview"
        )
        st.dataframe(
            working_df.head()
        )

#CSV export
if "working_df" in st.session_state:

    csv_data = st.session_state[
        "working_df"
    ].to_csv(index=False)

    st.download_button(
        label="Download Cleaned CSV",
        data=csv_data,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )