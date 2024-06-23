import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

# Set the title of the Streamlit app
st.title("This is the Data App Assignment, on June 20th")

# Display a header and read in the CSV file
st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)

# Add a dropdown menu for category selection
categories = df['Category'].unique()
selected_category = st.selectbox("Select a Category", categories)

# Filter the dataframe based on the selected category
filtered_df = df[df['Category'] == selected_category]

# Display the filtered data
st.write(f"### Data for {selected_category}")
st.dataframe(filtered_df)

# Plot a bar chart of sales by sub-category within the selected category
st.bar_chart(filtered_df, x="Sub-Category", y="Sales")

# Aggregate sales by sub-category and display as a dataframe
aggregated_df = filtered_df.groupby("Sub-Category").sum().reset_index()
st.dataframe(aggregated_df)

# Plot a bar chart with aggregated sales by sub-category
st.bar_chart(aggregated_df, x="Sub-Category", y="Sales", color="#04f")

# Ensure the Order_Date column is in datetime format and set it as the index
filtered_df["Order_Date"] = pd.to_datetime(filtered_df["Order_Date"])
filtered_df.set_index('Order_Date', inplace=True)

# Group sales by month
sales_by_month = filtered_df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

# Display the monthly sales data
st.dataframe(sales_by_month)

# Plot a line chart of monthly sales
st.line_chart(sales_by_month, y="Sales")

