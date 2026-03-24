
import pandas as pd

# Load Data
df = pd.read_csv("scripts/train.csv")

# ======================================================
# Exploratory Data Analysis (EDA)
# ======================================================

# -----------------------
# Data Preparation
# -----------------------

# Ensure Order Date is datetime (safe conversion)
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")

# Create time features
df["month"] = df["Order Date"].dt.month
df["month_name"] = df["Order Date"].dt.month_name()
df["day_name"] = df["Order Date"].dt.day_name()

# -----------------------
# Regional Performance
# -----------------------

# Total sales by region
region_sales = (
	df.groupby("Region")["Sales"]
	.sum()
	.sort_values(ascending=False)
)

# Number of transactions by region
region_transactions = (
	df.groupby("Region")["Order ID"]
	.nunique()
	.sort_values(ascending=False)
)

# Average sale value by region
region_avg_sale = (
	df.groupby("Region")["Sales"]
	.mean()
	.sort_values(ascending=False)
)

print("Total sales by region:")
print(region_sales)

print("\nTransactions by region:")
print(region_transactions)

print("\nAverage sale value by region:")
print(region_avg_sale)

# Regional summary including Average Order Value (AOV)
region_summary = df.groupby("Region").agg(
	total_sales=("Sales", "sum"),
	num_transactions=("Order ID", "nunique")
)

region_summary["avg_order_value"] = (
	region_summary["total_sales"] / region_summary["num_transactions"]
)

region_summary = region_summary.sort_values(
	by="total_sales", ascending=False
)

print("\nRegional summary (including AOV):")
print(region_summary)

# -----------------------
# Category Performance
# -----------------------

category_summary = (
	df.groupby("Category")
	.agg(
    	total_sales=("Sales", "sum"),
    	num_transactions=("Order ID", "nunique"),
    	avg_sale=("Sales", "mean")
	)
	.sort_values(by="total_sales", ascending=False)
)

print("\nCategory performance:")
print(category_summary)

# -----------------------
# Time-Based Analysis
# -----------------------

# Monthly sales trend
monthly_sales = (
	df.groupby(["month", "month_name"])["Sales"]
	.sum()
	.reset_index()
	.sort_values("month")
)

print("\nMonthly sales:")
print(monthly_sales)

# Sales by day of week
day_sales = (
	df.groupby("day_name")["Sales"]
	.sum()
	.sort_values(ascending=False)
)

print("\nSales by day of week:")
print(day_sales)

# -----------------------
# Product Performance
# -----------------------

top_products = (
	df.groupby("Product Name")["Sales"]
	.sum()
	.sort_values(ascending=False)
	.head(10)
)

print("\nTop 10 products by sales:")
print(top_products)

# -----------------------
# Key EDA Insights
# -----------------------

print("\n--- KEY EDA INSIGHTS ---")
print(f"Top region by total sales: {region_sales.idxmax()}")
print(f"Region with most transactions: {region_transactions.idxmax()}")
print(f"Region with highest average sale: {region_avg_sale.idxmax()}")

print(f"Top category by sales: {category_summary.index[0]}")
print(f"Top product by sales: {top_products.index[0]}")

print(
	"Highest sales month:",
	monthly_sales.loc[monthly_sales["Sales"].idxmax(), "month_name"]
)

print("Best performing day:", day_sales.idxmax())

