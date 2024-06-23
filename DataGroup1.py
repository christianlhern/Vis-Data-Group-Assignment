import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the Streamlit app
st.title("Sales Analysis App")

# Display a header and read in the CSV file
st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=['Order_Date'])

# Define categories and sub-categories
categories = {
    'Furniture': ['Bookcases', 'Chairs', 'Furnishings', 'Tables'],
    'Office Supplies': ['Appliances', 'Art', 'Binders', 'Envelopes', 'Fasteners', 'Labels', 'Paper', 'Storage', 'Supplies'],
    'Technology': ['Accessories', 'Copiers', 'Machines', 'Phones']
}

# Add a multi-select dropdown menu for sub-category selection
selected_category = st.selectbox("Select a Category", list(categories.keys()))
selected_subcategories = st.multiselect("Select Sub-categories", categories[selected_category])

# Filter the dataframe based on the selected category and sub-categories
filtered_df = df[(df['Category'] == selected_category) & (df['Sub_Category'].isin(selected_subcategories))]

# Display the filtered data
st.write(f"### Data for {selected_category} - {', '.join(selected_subcategories)}")
st.dataframe(filtered_df)

# Plot a line chart of sales for the selected items
if not filtered_df.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    for sub_category in selected_subcategories:
        sub_df = filtered_df[filtered_df['Sub_Category'] == sub_category]
        ax.plot(sub_df['Order_Date'], sub_df['Sales'], marker='o', linestyle='-', label=sub_category)
    ax.set_xlabel('Order Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Trend')
    ax.legend()
    st.pyplot(fig)
else:
    st.write("No data available for the selected category and sub-categories.")


