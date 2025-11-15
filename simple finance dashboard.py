import streamlit as st
import pandas as pd

st.title("Simple Finance Dashboard")

# Upload Excel or CSV
file = st.file_uploader("Upload your finance file (Excel/CSV)", type=["xlsx", "csv"])

if file:
    # Read file
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.write("### Your Data")
    st.dataframe(df)

    # Check required columns
    if "Revenue" in df.columns and "Expense" in df.columns:
        total_revenue = df["Revenue"].sum()
        total_expense = df["Expense"].sum()
        profit = total_revenue - total_expense

        st.write("### Summary")
        st.write("*Total Revenue:* ₹", total_revenue)
        st.write("*Total Expense:* ₹", total_expense)
        st.write("*Profit:* ₹", profit)
    else:
        st.warning("Your file must contain columns: Revenue, Expense")
else:
    st.info("Please upload a file to start")
