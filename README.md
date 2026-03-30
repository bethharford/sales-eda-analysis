# sales-eda-analysis
Exploratory data analysis of sales data
Project Overview
This project explores a retail sales dataset to analyse regional performance, category trends, time‑based patterns, and top‑selling products.
The aim is to demonstrate a complete exploratory data analysis (EDA) workflow using Python, with a strong focus on business‑relevant metrics and clear, interpretable insights.
The analysis mirrors real‑world retail and business analytics use cases, including revenue concentration, customer purchasing behaviour, and seasonality.

Objectives
The primary objectives of this analysis were to:
Compare sales performance across geographic regions
Measure transaction volume versus revenue contribution
Analyse category‑level revenue drivers
Identify temporal trends by month and day of week
Highlight top‑performing products
Translate raw transactional data into actionable insights

Dataset
Type: Retail transaction data
Granularity: Individual sales transactions
Key fields:
Order ID
Order Date
Region
Category
Product Name
Sales
The dataset represents individual purchase events, allowing analysis at regional, category, product, and temporal levels.

Analysis Workflow
1️⃣ Regional Performance
Regional sales performance was assessed using:
Total sales revenue
Number of unique transactions
Average sale value
Average Order Value (AOV), calculated as:
AOV = total_sales / number_of_transactions

This distinction helps identify regions driven by:
High transaction volume versus
Higher‑value orders per transaction

2️⃣ Category Performance
Each product category was evaluated based on:
Total sales
Number of transactions
Average sale value
This highlights which categories are the largest contributors to revenue and whether performance is driven by volume or order size.

3️⃣ Time‑Based Analysis
Temporal patterns were explored by analysing:
Monthly sales trends to identify seasonality
Day‑of‑week performance to understand purchasing behaviour across the week
Order dates were converted to datetime format to ensure accurate grouping and chronological ordering.

4️⃣ Product Performance
Products were ranked by total sales to identify the top 10 revenue‑generating products, showing:
Revenue concentration
Key products driving overall performance

Key Insights
One region consistently leads in total sales, indicating strong overall market presence
Another region records the highest transaction count, suggesting high customer activity even where average sale values are lower
A small number of product categories contribute a disproportionate share of total revenue
Clear seasonal patterns are present, with one month showing peak sales performance
Sales vary meaningfully by day of the week, revealing opportunities for promotions and operational optimisation
Revenue is partially concentrated among a small number of top‑performing products

Tools & Technologies
Python
Pandas for data manipulation and aggregation
Datetime utilities for temporal analysis
Jupyter Notebook / Python scripts for reproducible workflows
(Optional extension: Power BI or other BI tools for visualisation.)

Project Structure
retail-sales-performance-analysis/
│
├── data/
│   └── raw_dataset.csv
│
├── scripts/
│   └── analysis.py
│
├── notebooks/
│   └── eda.ipynb
│
├── outputs/
│
└── README.md


Limitations
The analysis is descriptive and does not infer causality
Customer demographic information is not available
Promotional, pricing, or discount data is not included
Results depend on the accuracy and completeness of the dataset

Possible Extensions
Customer segmentation analysis
Sales forecasting and trend modelling
Category growth analysis over time
Promotion impact modelling
SQL‑based data modelling and dashboards

Author Notes
This project forms part of a structured data analytics portfolio aimed at demonstrating:
End‑to‑end exploratory analysis
Business‑focused metric selection
Clear communication of findings
Reproducible analytical workflows
The emphasis is on clarity, decision relevance, and analytical judgement rather than unnecessary technical complexity.


