import streamlit as st
from transformers.missing_handler import handle_missing_values
from transformers.duplicate_handler import remove_duplicates
from transformers.outlier_handler import remove_outliers_iqr

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

    # Numerical columns
    numeric_cols = [
        col for col in df.select_dtypes(
            include="number"
        ).columns
        if "Unnamed" not in col
    ]

    # Categorical columns
    categorical_cols = [
        col for col in df.select_dtypes(
            exclude="number"
        ).columns
        if "Unnamed" not in col
    ]

    # Method selection
    selected_method = st.selectbox(
        "Select Imputation Method",
        [
            "mean",
            "median",
            "mode",
            "drop_rows"
        ]
    )

    # Dynamic column selection
    if selected_method in ["mean", "median"]:

        selectable_cols = numeric_cols

    else:

        selectable_cols = (
            numeric_cols + categorical_cols
        )

    # Column selection
    selected_columns = st.multiselect(
        "Select Columns",
        selectable_cols
    )

    # Apply button
    apply_missing = st.button(
        "Apply Missing Value Handling"
    )

    if apply_missing:

        transformed_df = handle_missing_values(
            working_df,
            selected_columns,
            selected_method
        )

        # Update session state
        st.session_state[
            "working_df"
        ] = transformed_df

        st.success(
            "Missing Value Handling Applied!"
        )

        st.subheader(
            "Transformed Dataset Preview"
        )

        st.dataframe(
            transformed_df.head()
        )

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

# Outlier Removal

# Outlier Handling
with st.expander("Outlier Handling"):

    st.subheader("Remove Outliers (IQR Method)")

    numeric_cols = [
        col for col in working_df.select_dtypes(
            include="number"
        ).columns
        if "Unnamed" not in col
    ]

    selected_outlier_cols = st.multiselect(
        "Select Columns for Outlier Removal",
        numeric_cols
    )

    apply_outliers = st.button(
        "Apply Outlier Removal"
    )

    if apply_outliers:

        transformed_df = remove_outliers_iqr(
            st.session_state["working_df"],
            selected_outlier_cols
        )

        st.session_state[
            "working_df"
        ] = transformed_df

        st.success(
            "Outliers Removed Successfully!"
        )

        st.subheader(
            "Updated Dataset Preview"
        )

        st.dataframe(
            transformed_df.head()
        )

#CSV export
st.subheader("Export Cleaned Dataset")

csv_data = st.session_state[
    "working_df"
].to_csv(index=False)

st.download_button(
    label="Download Final Cleaned CSV",
    data=csv_data,
    file_name="cleaned_dataset.csv",
    mime="text/csv",
    key="final_csv_download"
)