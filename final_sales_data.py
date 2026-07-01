import pandas as pd 


def load_data(): # Loading the data from the csv file and returning a dataset to analyze
    sales = pd.read_csv("sales_data.csv")
    return sales


def create_columns(sales): # Adding a total revenue, cost and profit column to the dataset and then printing the first 5 rows again to see the changes
    sales["Total_Revenue"] = sales["Unit_Price"] * sales["Quantity_Sold"] 
    sales["Total_Cost"] = sales["Unit_Cost"] * sales["Quantity_Sold"]
    sales["Total_Profit"] = sales["Total_Revenue"] - sales["Total_Cost"]
    return sales

sales = load_data()
sales = create_columns(sales)

def data_summary(sales): # Printing the first 5 rows, shape, columns and info of the dataset to get a summary of the data
    print(sales.head())
    print(sales.shape)
    print(sales.columns)
    print(sales.info())


def check_missing_values(sales): # Checking for missing values in the dataset
    print(sales.isnull().sum())
    print(sales.notnull().sum())

def product_analysis(sales): # Analyze the product to answer questions
    # Q: What is the total profit generated?
    total_profit = sales["Total_Profit"].sum()  # The old code before I introduced the total profit column: total_profit = sales["Unit_Price"].sum() - sales["Unit_Cost"].sum() * sales["Quantity_Sold"].sum()
    print(f"""
Total Profit: 
${total_profit:.2f}""")

    # Q: What is the average unit cost, price and profit of products sold?
    average_unit_cost = sales["Total_Cost"].mean() # The old code before I introduced the total cost column: average_unit_cost = sales["Unit_Cost"] * sales["Quantity_Sold"].mean()
    average_unit_price = sales["Total_Revenue"].mean()  # The old code before I introduced the total price column: average_unit_price = sales["Unit_Price"] * sales["Quantity_Sold"].mean()
    average_profit = sales["Total_Profit"].mean() # The old code before I introduced the total profit column: average_profit = average_unit_price - average_unit_cost
    print(f"""
Average Product Cost: 
${average_unit_cost:.2f}""")
    print(f"""
Average Product Price: 
${average_unit_price:.2f}""")
    print(f"""
Average Product Profit: 
${average_profit:.2f}""")

    # Q: How many unique products are there in the dataset?
    unique_products = sales[sales["Quantity_Sold"] == 1].value_counts().sum()
    print(f"""
Unique Products Sold:
{unique_products}""")

    # Q: What is the most expensive product sold?
    most_expensive_product = sales.groupby("Product_ID")["Unit_Price"].max().idxmax()
    highest_product_profit_value = sales.groupby("Product_ID")["Unit_Price"].max().max()
    print(f"""
Most Expensive Product Sold: 
ID {most_expensive_product} for ${highest_product_profit_value:.2f}""")
    
    # Q: What is the cheapest expensive product sold?
    cheapest_product = sales.groupby("Product_ID")["Unit_Price"].min().idxmin()
    highest_product_profit_value = sales.groupby("Product_ID")["Unit_Price"].min().min()
    print(f"""
Cheapest Product Sold: 
ID {cheapest_product} for ${highest_product_profit_value:.2f}""")
        
    # Q: Which product has the highest profit?
    highest_product_profit =  sales.groupby("Product_ID")["Total_Profit"].max().idxmax()
    highest_product_profit_value = sales.groupby("Product_ID")["Total_Profit"].max().max()
    print(f"""
Product with the Highest Profit: 
ID {highest_product_profit} with ${highest_product_profit_value:.2f}""")
    

def product_category_analysis(sales): # Analyze the product category to answer questions
    # Q: Which product category sold the most?
    most_sales = sales["Product_Category"].value_counts().idxmax()
    print(f"""
Most Sold Category: 
{most_sales}""")

    # Q: Which category has the highest total revenue?
    highest_revenue_category = sales.groupby("Product_Category")["Total_Revenue"].sum().idxmax()
    print(f"""
Product Category with Highest Total Revenue: 
{highest_revenue_category}""")

    # Q: What product category has the highest average profit?
    highest_average_category_profit = sales.groupby("Product_Category")["Total_Profit"].mean().idxmax()
    print(f"""
Product Category with Highest Average Profit: 
{highest_average_category_profit}""")


def customer_analysis(sales): # Analyze the customer to answer questions
    # Q: What category of costumer spent the most money; new or returning?
    highest_spending_customer = sales.groupby("Customer_Type")["Total_Profit"].sum().idxmax()
    print(f"""
Customer Category that Spent the Most Money: 
{highest_spending_customer}""")
    
def print_profit_percentage(profit_percentage_per_category):
        print("\nTotal Profit Percentage Contribution by Category:")

        for category, percentage in profit_percentage_per_category.items():
            print(f"{category}: {percentage} %")
        print("")

profit_percentage_per_category = (
            sales.groupby("Product_Category")["Total_Profit"].sum()
            / sales["Total_Profit"].sum()
            * 100
        ).round(2).sort_values(ascending=False)

def sales_analysis_report(sales):
    sales = load_data()
    sales = create_columns(sales)
    print("""
---------------------
SALES ANALYSIS REPORT
---------------------""")
    product_analysis(sales)
    product_category_analysis(sales)
    customer_analysis(sales)
    print_profit_percentage(profit_percentage_per_category)

def main():
    sales_analysis_report(sales)

if __name__ == "__main__":
    main()
