import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset (replace 'your_dataset.csv' with the actual file name)
data_file = "Superstore.csv"
df = pd.read_csv(data_file, encoding="latin1")

# Streamlit app
st.title("Sales Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

# Region filter
regions = st.sidebar.multiselect("Select Region(s):", options=df["Region"].unique(), default=df["Region"].unique())

# Category filter
categories = st.sidebar.multiselect("Select Category(s):", options=df["Category"].unique(), default=df["Category"].unique())

# Date range filter
df["Order Date"] = pd.to_datetime(df["Order Date"])
date_range = st.sidebar.date_input(
    "Select Date Range:",
    [df["Order Date"].min().date(), df["Order Date"].max().date()]
)

# Filter data based on user selections
filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories)) &
    (df["Order Date"] >= pd.Timestamp(date_range[0])) &
    (df["Order Date"] <= pd.Timestamp(date_range[1]))
]

# Main dashboard
st.header("Overview")

# KPI Cards
st.subheader("Key Metrics")
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", total_orders)

# Yearly Sales Trend
st.header("Yearly Sales Trend")
df["Year"] = df["Order Date"].dt.year
yearly_sales = df.groupby("Year")["Sales"].sum().reset_index()

fig_yearly_sales = px.bar(
    yearly_sales,
    x="Year",
    y="Sales",
    text="Sales",
    template="plotly_dark",
    title="Yearly Sales Trend",
    color_discrete_sequence=["#b1e7cd"]
)

fig_yearly_sales.update_layout(
    xaxis_title="Year",
    yaxis_title="Total Sales",
    title=dict(
        text="Yearly Sales Trend",
        x=0.5,  # Center the title
        xanchor="center",
        yanchor="top"
    )
)

fig_yearly_sales.update_traces(texttemplate="%{text:.2s}", textposition="outside")
st.plotly_chart(fig_yearly_sales)

# Sales by Region
st.subheader("Sales by Region")
sales_by_region = filtered_df.groupby("Region")["Sales"].sum().reset_index()
fig_region = px.bar(sales_by_region, x="Region", y="Sales", title="Sales by Region", text="Sales")
st.plotly_chart(fig_region)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")
filtered_df["month"] = filtered_df["Order Date"].dt.to_period("M").dt.to_timestamp()
monthly_sales = filtered_df.groupby("month")["Sales"].sum().reset_index()

fig_monthly_sales = px.line(
    monthly_sales,
    x="month",
    y="Sales",
    template="plotly_dark",
    color_discrete_sequence=["#b1e7cd"],
    title="Monthly Sales Trend"
)

fig_monthly_sales.update_layout(
    xaxis_title="Months",
    yaxis_title="Total Sales",
    title=dict(
        text="Monthly Sales Trend",
        x=0.5,  # Center the title
        xanchor="center",
        yanchor="top"
    )
)

fig_monthly_sales.update_xaxes(showgrid=True, tickformat="%b %Y")
fig_monthly_sales.update_yaxes(showgrid=True)

st.plotly_chart(fig_monthly_sales)

# Top Products by Sales
st.subheader("Top Products by Sales")
top_products = filtered_df.groupby("Product Name")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False).head(10)
fig_products = px.bar(top_products, x="Sales", y="Product Name", title="Top Products by Sales", orientation="h", text="Sales")
st.plotly_chart(fig_products)

# Profit Percentage by Category
st.subheader("Profit Percentage by Category")
category_profit = filtered_df.groupby("Category")["Profit"].sum().reset_index()
total_profit = category_profit["Profit"].sum()
category_profit["Profit Percentage"] = (category_profit["Profit"] / total_profit) * 100

fig_profit_percentage = px.pie(
    category_profit,
    names="Category",
    values="Profit Percentage",
    template="plotly_dark",
    title="Profit Percentage for Each Category",
    color_discrete_sequence=px.colors.sequential.Reds
)

fig_profit_percentage.update_traces(textinfo="percent+label")
st.plotly_chart(fig_profit_percentage)


# Discount vs Total Sales Visualization
st.subheader("Total Sales with Discounts")

fig_sales_discount = px.scatter(
    df,
    x="Discount",
    y="Sales",
    template="plotly_dark",
    title="Total Sales with Discounts",
    color_discrete_sequence=["#ff7f0e"]  # Replace `colors[7]` with a fixed color
)

fig_sales_discount.update_layout(
    xaxis_title="Discount",
    yaxis_title="Total Sales",
    title=dict(
        text="Total Sales with Discounts",
        x=0.5,
        xanchor="center",
        yanchor="top"
    )
)

st.plotly_chart(fig_sales_discount)


# Grouped Discount vs Total Profit
st.subheader("Discount vs Total Profit")
discount_group = df.groupby('Discount')['Profit'].sum().reset_index()

fig_discount_group = px.scatter(
    discount_group,
    x="Discount",
    y="Profit",
    template="plotly_dark",
    title="Total Profit with Discount",
    color_discrete_sequence=["#ff7f0e"]  # Replace `colors[7]` with a fixed color
)

fig_discount_group.update_traces(
    mode="markers",
    marker=dict(size=8, opacity=0.7)
)

fig_discount_group.update_layout(
    xaxis_title="Discount",
    yaxis_title="Total Profit",
    title=dict(
        text="Total Profit with Discount",
        x=0.5,
        xanchor="center",
        yanchor="top"
    )
)

st.plotly_chart(fig_discount_group)

# Run the app using: streamlit run app.py