import pandas as pd 

sales = pd.read_csv("sales_data.csv")

print(sales.head())

# Adding a total revenue, cost and profit column to the dataset and then printing the first 5 rows again to see the changes
sales["Total_Revenue"] = sales["Unit_Price"] * sales["Quantity_Sold"]
sales["Total_Cost"] = sales["Unit_Cost"] * sales["Quantity_Sold"]
sales["Total_Profit"] = sales["Total_Revenue"] - sales["Total_Cost"]

print(sales.head())
print(sales.shape)
print(sales.columns)

# Question 1: Which product category sold the most?
most_sales = sales["Product_Category"].value_counts().idxmax()
print(f"The product category that sold the most is: {most_sales}")

# Question 2: What is the total profit generated?
# The old code before I introduced the total profit column: total_profit = sales["Unit_Price"].sum() - sales["Unit_Cost"].sum() * sales["Quantity_Sold"].sum()
total_profit = sales["Total_Profit"].sum()
print(f"The total profit generated is: ${total_profit:.2f}")

# Question 3: What is the average unit cost, price and profit of products sold?
# The old code before I introduced the total cost column: average_unit_cost = sales["Unit_Cost"].mean()
average_unit_cost = sales["Total_Cost"].mean()
# The old code before I introduced the total price column: average_unit_price = sales["Unit_Price"].mean()
average_unit_price = sales["Total_Revenue"].mean()
# The old code before I introduced the total profit column: average_profit = average_unit_price - average_unit_cost
average_profit = sales["Total_Profit"].mean()
print(f"The average unit cost is: ${average_unit_cost:.2f}")
print(f"The average unit price is: ${average_unit_price:.2f}")
print(f"The average profit is: ${average_profit:.2f}")

# Question 4: How many unique products are there in the dataset?
unique_products = sales[sales["Quantity_Sold"] == 1].shape[0]
print(f"There are {unique_products} unique products that have been sold.")

# Question 5: What is the most expensive product sold?
most_expensive_product = sales.loc[sales["Unit_Price"].idxmax()]
print(f"""The most expensive product sold is: 
{most_expensive_product}""")

# Question 6: What is the cheapest expensive product sold?
cheapest_product = sales.loc[sales["Unit_Price"].idxmin()]
print(f"""The cheapest product sold is: 
{cheapest_product}""")

# Question 7: Which category has the highest total revenue?
highest_revenue_category = sales.groupby("Product_Category")["Total_Revenue"].sum().idxmax()
print(f"The product category with the highest total revenue is: {highest_revenue_category}")

# Question 8: Which product has the highest profit?
highest_product_profit = sales.loc[sales["Total_Profit"].idxmax(), "Product_ID"]
print(f"The product with the highest profit is: ID {highest_product_profit}")

# Question 9: What category of costumer spent the most money; new or returning?
highest_spending_customer = sales.groupby("Customer_Type")["Total_Profit"].sum().idxmax()
print(f"The customer category that spent the most money is: {highest_spending_customer}")

# Question 10: What product category has the highest average profit?
highest_average_category_profit = sales.groupby("Product_Category")["Total_Profit"].mean().idxmax()
print(f"The product category with the highest average profit is: {highest_average_category_profit}")

# Question 11: What profit percentage does each product category contribute to the total profit?
profit_percentage_per_category = sales.groupby("Product_Category")["Total_Profit"].sum() / total_profit * 100 
profit_percentage_per_category = profit_percentage_per_category.astype(str) + ' %'
print(f"""The profit percentage contribution from each category is:
{profit_percentage_per_category}""")