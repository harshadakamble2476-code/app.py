import streamlit as st
import pandas as pd

st.title("📊 Simple Finance Dashboard")

file = st.file_uploader("Upload your Excel or CSV file", type=["xlsx", "csv"])

if file is not None:

    # For CSV files
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)

    # For Excel files (safe, no engine required)
    else:
        df = pd.read_excel(file)

    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Basic Summary")
    st.write(df.describe(include="all"))
