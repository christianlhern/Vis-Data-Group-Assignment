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
if selected_category == 'All':
    filtered_df = df
elif selected_subcategories:
    filtered_df = df[(df['Category'] == selected_category) & (df['Sub_Category'].isin(selected_subcategories))]
else:
    filtered_df = df[df['Category'] == selected_category]

# Display the filtered data
st.write(f"### Data for {selected_category} - {', '.join(selected_subcategories)}")
st.dataframe(filtered_df)

# Calculate metrics: Total Sales, Total Profit, Overall Profit Margin (%)
if not filtered_df.empty:
    total_sales = filtered_df['Sales'].sum()
    total_profit = filtered_df['Profit'].sum()
    overall_profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

    # Display metrics
    st.write(f"**Total Sales:** ${total_sales:.2f}")
    st.write(f"**Total Profit:** ${total_profit:.2f}")
    st.write(f"**Overall Profit Margin (%):** {overall_profit_margin:.2f}%")

    # Aggregate sales by year
    filtered_df['Year'] = filtered_df['Order_Date'].dt.year
    sales_by_year = filtered_df.groupby('Year')['Sales'].sum()

    # Plot a line chart of cumulative sales over the years
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(sales_by_year.index, sales_by_year.values, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Sales')
    ax.set_title(f'Total Sales Over the Years - {selected_category}')
    st.pyplot(fig)
else:
    st.write("No data available for the selected category and sub-categories.")
