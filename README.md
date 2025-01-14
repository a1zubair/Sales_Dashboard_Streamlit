  # Superstore Sales Dashboard

# Overview
This project involves creating an interactive sales dashboard using the Superstore dataset from Kaggle. The dashboard was designed and deployed using Streamlit, a Python-based framework for developing web applications. The objective of this project was to analyze sales performance, explore key metrics, and visualize trends in various dimensions, such as regions, product categories, and timeframes. The dashboard serves as a tool for decision-makers to gain insights into sales and profitability while identifying key trends and opportunities.

# Dataset Overview
The dataset contains transactional data, covering aspects such as: 

Order ID: Unique Order ID for each Customer.

Order Date: Order Date of the product.

Customer ID: Unique ID to identify each Customer.

Customer Name: Name of the Customer.

Segment: The segment where the Customer belongs.

Country: Country of residence of the Customer.

City: City of residence of of the Customer.

State: State of residence of the Customer.

Region: Region where the Customer belong.

Product ID: Unique ID of the Product.

Category: Category of the product ordered.

Sub-Category: Sub-Category of the product ordered.

Product Name: Name of the Product.

Sales: Sales of the Product.

Quantity: Quantity of the Product.

Discount: Discount provided.

Profit: Profit/Loss incurred.

# Key Features of the Dashboard

## a) Interactive Filters

The dashboard has three interactive filters:

 - Region Filter: Users can filter sales data based on specific regions.
 -  Category Filter: Filters are available for selecting one or more product categories.
 -   Date Range Filter: Enables narrowing down data within a specific timeframe.

## b) Key Metrics : Total Sales, Total Profit and Total Orders

   <img width="890" alt="Screenshot 2025-01-14 at 11 02 55 PM" src="https://github.com/user-attachments/assets/fe6b4c3f-3aa4-42b1-bcb4-c2c79a306877" />

## c) Visualizations

1. Yearly Sales Trend : The total Sales are highest in 2017, following following 2016,  2014 and 2015

   <img width="996" alt="Screenshot 2025-01-14 at 11 09 06 PM" src="https://github.com/user-attachments/assets/af25a2ac-be9f-45cd-9762-bb9d0393d1af" />


##

2. Monthly Sales Trend : The Montly Sales have been strong in June 2017

   <img width="985" alt="Screenshot 2025-01-14 at 11 11 59 PM" src="https://github.com/user-attachments/assets/ab326c33-2753-4d30-8c7a-ddb20fc2ff7d" />

##

3. Sales by Region : The West region has the highest sales, followed by East, Central and South regions.

    <img width="938" alt="Screenshot 2025-01-14 at 11 11 37 PM" src="https://github.com/user-attachments/assets/127b5962-6be1-4f20-b503-631823b90906" />


##

4. Top Produts by Sales : The image displays the top ten best-selling products based on the highest sales revenue.
   
    <img width="975" alt="Screenshot 2025-01-14 at 11 12 21 PM" src="https://github.com/user-attachments/assets/1ecb95c6-9745-474c-b73f-def94de03a0f" />

##

5. Profit Percentage by Category : Technology sales generate the highest amount of profit, followed by offfice sales and then furniture.

    <img width="955" alt="Screenshot 2025-01-14 at 11 12 40 PM" src="https://github.com/user-attachments/assets/886f1b7c-acf4-40ce-976f-d6c2456bc8e8" />

##

6. Discount Vs Total Sales :  The figure shows a significant concentration of sales is observed at a 0% discount, with some reaching higher total sales values. And the next bigger sales are when a 50% discount is applied to the products. 
   
   <img width="869" alt="Screenshot 2025-01-14 at 11 12 58 PM" src="https://github.com/user-attachments/assets/329eed75-204e-4c2a-bb1d-26921b998081" /> 

##
   
7. Discount Vs Total Profit : The image shows that as discounts increase, total profit generally declines, with profits even turning negative at higher discount levels.

   <img width="827" alt="Screenshot 2025-01-14 at 11 13 17 PM" src="https://github.com/user-attachments/assets/14099df3-9e1d-4f37-b927-5932be2d178b" />

##

# Implementation Details

## a) Data Preprocessing

-  The Order Date column was converted into a datetime format for accurate filtering and time-series analysis.
   
-  Derived fields such as Year and Month were added to facilitate year-over-year and month-over-month trend analysis.

## b) Visualization Tools

-  Leveraged Plotpy for creating interactive charts, providing features like hover effects, tooltips, and custom formatting.
   
-  Used Streamlit for the deployment process which also, enabled real-time interactivity for users.

## c) Insights Derived:

-  Sales increased consistently over the years, showcasing growth.

-  Certain regions demonstrated significantly higher sales compared to others, potentially due to larger customer bases or higher-order volumes.

-  Analysis of the top-selling products provides actionable insights into inventory and marketing strategies.

-  Observations revealed that while discounts often boosted sales, they sometimes led to reduced profitability, necessitating careful discount planning.

# Deployment

The project was deployed using Streamlit's sharing platform, allowing public access and ease of demonstration. The app is live at: [Sales Dashboard](https://iwmzpsezammraqyk7tlf2u.streamlit.app/).


