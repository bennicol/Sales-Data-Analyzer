import pandas as pd 

sales = pd.read_csv("sales_data.csv")

print(sales.head())
print(sales.shape)
print(sales.columns)
print(sales["Product_Category"])

# Question 1: Which product category sold the most?
most_sales = sales["Product_Category"].value_counts().idxmax()
print(f"The product category that sold the most is: {most_sales}")

# Question 2: What is the total profit generated?
total_profit = sales["Unit_Price"].sum() - sales["Unit_Cost"].sum()
print(f"The total profit generated is: ${total_profit:.2f}")

# Question 3: What is the average unit cost, price and profitof products sold?
average_unit_cost = sales["Unit_Cost"].mean()
average_unit_price = sales["Unit_Price"].mean()
average_profit = average_unit_price - average_unit_cost
print(f"The average unit cost is: ${average_unit_cost:.2f}")
print(f"The average unit price is: ${average_unit_price:.2f}")
print(f"The average profit is: ${average_profit:.2f}")