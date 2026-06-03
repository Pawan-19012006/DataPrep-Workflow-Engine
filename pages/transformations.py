import streamlit as st
import io
from transformers.missing_handler import handle_missing_values
from transformers.duplicate_handler import remove_duplicates
from transformers.outlier_handler import remove_outliers_iqr
from transformers.scaler import scale_features
from transformers.encoder import encode_features

if "original_df" not in st.session_state:

    st.warning("Please upload a dataset first.")

    st.stop()

df = st.session_state["original_df"]

if "working_df" not in st.session_state:

    st.session_state["working_df"] = (
        st.session_state["original_df"].copy()
    )

if "history" not in st.session_state:
    st.session_state["history"] = []

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

        history_message = {

            "mean":
            f"Applied Mean Imputation on {selected_columns}",

            "median":
            f"Applied Median Imputation on {selected_columns}",

            "mode":
            f"Applied Mode Imputation on {selected_columns}",

            "drop_rows":
            f"Dropped Rows with Missing Values in {selected_columns}"

         }

        st.session_state["history"].append(
            history_message[selected_method]
        )

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

        st.session_state["history"].append(
            "Removed Duplicate Rows"
        )

        st.success(
            "Duplicate Rows Removed!"
        )

        st.subheader(
            "Updated Dataset Preview"
        )
        st.dataframe(
            working_df.head()
        )

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

        st.session_state["history"].append(
            f"Removed Outliers using IQR on {selected_outlier_cols}"
        )

        st.success(
            "Outliers Removed Successfully!"
        )

        st.subheader(
            "Updated Dataset Preview"
        )

        st.dataframe(
            transformed_df.head()
        )

# Feature Scaling
with st.expander("Feature Scaling"):

    st.subheader("Scale Numerical Features")

    numeric_cols = [
        col for col in working_df.select_dtypes(
            include="number"
        ).columns
        if "Unnamed" not in col
    ]

    selected_scale_cols = st.multiselect(
        "Select Columns for Scaling",
        numeric_cols
    )

    scaling_method = st.selectbox(
        "Select Scaling Method",
        [
            "minmax",
            "standard"
        ]
    )

    apply_scaling = st.button(
        "Apply Feature Scaling"
    )

    if apply_scaling:

        transformed_df = scale_features(
            st.session_state["working_df"],
            selected_scale_cols,
            scaling_method
        )

        st.session_state[
            "working_df"
        ] = transformed_df

        history_message = {

            "minmax":
            f"Applied MinMax Scaling on {selected_scale_cols}",

            "standard":
            f"Applied Standard Scaling on {selected_scale_cols}"

        }

        st.session_state["history"].append(
            history_message[scaling_method]
        )

        st.success(
            "Feature Scaling Applied!"
        )

        st.subheader(
            "Updated Dataset Preview"
        )

        st.dataframe(
            transformed_df.head()
        )

# Feature Encoding
with st.expander("Feature Encoding"):

    st.subheader("Encode Categorical Features")

    categorical_cols = [
        col for col in working_df.select_dtypes(
            exclude="number"
        ).columns
        if "Unnamed" not in col
    ]

    selected_encode_cols = st.multiselect(
        "Select Columns for Encoding",
        categorical_cols
    )

    encoding_method = st.selectbox(
        "Select Encoding Method",
        [
            "label",
            "onehot"
        ]
    )

    apply_encoding = st.button(
        "Apply Encoding"
    )

    if apply_encoding:

        transformed_df = encode_features(
            st.session_state["working_df"],
            selected_encode_cols,
            encoding_method
        )

        st.session_state[
            "working_df"
        ] = transformed_df

        history_message = {

            "label":
            f"Applied Label Encoding on {selected_encode_cols}",

            "onehot":
            f"Applied One-Hot Encoding on {selected_encode_cols}"

        }

        st.session_state["history"].append(
            history_message[encoding_method]
        )

        st.success(
            "Encoding Applied Successfully!"
        )

        st.subheader(
            "Updated Dataset Preview"
        )

        st.dataframe(
            transformed_df.head()
        )

#History
st.subheader("Transformation History")

if st.session_state["history"]:

    for step in st.session_state["history"]:

        st.write(f"✓ {step}")

else:

    st.info("No transformations applied yet.")

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

buffer = io.BytesIO()

st.session_state["working_df"].to_excel(
    buffer,
    index=False,
    engine="openpyxl"
)

st.download_button(
    label="Download Final Cleaned Excel",
    data=buffer,
    file_name="cleaned_dataset.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    key="excel_download"
)

if st.button("Reset All Transformations"):

    st.session_state["working_df"] = (
        st.session_state["original_df"].copy()
    )
    st.session_state["history"] = []

    st.success(
        "Pipeline Reset Successfully!"
    )
