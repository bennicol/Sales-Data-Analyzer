import pandas as pd 


def load_data(): # Loading the data from the csv file and returning a dataset to analyze
    sales = pd.read_csv("sales_data.csv")
    return sales


def create_columns(sales): # Adding a total revenue, cost and profit column to the dataset and then printing the first 5 rows again to see the changes
    sales["Total_Revenue"] = sales["Unit_Price"] * sales["Quantity_Sold"] 
    sales["Total_Cost"] = sales["Unit_Cost"] * sales["Quantity_Sold"]
    sales["Total_Profit"] = sales["Total_Revenue"] - sales["Total_Cost"]
    return sales


def data_summary(sales): # Printing the first 5 rows, shape, columns and info of the dataset to get a summary of the data
    print(sales.head())
    print(sales.shape)
    print(sales.columns)
    print(sales.info())


def check_missing_values(sales): # Checking for missing values in the dataset
    print(sales.isnull().sum())
    print(sales.notnull().sum())


def product_category_analysis(sales): # Analyze the product category to answer questions
    # Q: Which product category sold the most?
    most_sales = sales["Product_Category"].value_counts().max()
    print(f"The product category that sold the most is: {most_sales}")

    # Q: Which category has the highest total revenue?
    highest_revenue_category = sales.groupby("Product_Category")["Total_Revenue"].sum().max()
    print(f"The product category with the highest total revenue is: {highest_revenue_category}")
    
    # Q: What product category has the highest average profit?
    highest_average_category_profit = sales.groupby("Product_Category")["Total_Profit"].mean().idxmax()
    print(f"The product category with the highest average profit is: {highest_average_category_profit}")

    # Q: What profit percentage does each product category contribute to the total profit?
    profit_percentage_per_category = sales.groupby("Product_Category")["Total_Profit"].sum() / sales["Total_Profit"].sum() * 100
    profit_percentage_per_category = profit_percentage_per_category.astype(str) + ' %'
    print(f"""The profit percentage contribution from each category is:
    {profit_percentage_per_category}""")
    

def product_analysis(sales): # Analyze the product to answer questions
    # Q: What is the total profit generated?
    total_profit = sales["Total_Profit"].sum()  # The old code before I introduced the total profit column: total_profit = sales["Unit_Price"].sum() - sales["Unit_Cost"].sum() * sales["Quantity_Sold"].sum()
    print(f"The total profit generated is: ${total_profit:.2f}")

    # Q: What is the average unit cost, price and profit of products sold?
    average_unit_cost = sales["Total_Cost"].mean() # The old code before I introduced the total cost column: average_unit_cost = sales["Unit_Cost"] * sales["Quantity_Sold"].mean()
    average_unit_price = sales["Total_Revenue"].mean()  # The old code before I introduced the total price column: average_unit_price = sales["Unit_Price"] * sales["Quantity_Sold"].mean()
    average_profit = sales["Total_Profit"].mean() # The old code before I introduced the total profit column: average_profit = average_unit_price - average_unit_cost
    print(f"The average unit cost is: ${average_unit_cost:.2f}")
    print(f"The average unit price is: ${average_unit_price:.2f}")
    print(f"The average profit is: ${average_profit:.2f}")

    # Q: How many unique products are there in the dataset?
    unique_products = sales[sales["Quantity_Sold"] == 1].value_counts().sum()
    print(f"There are {unique_products} unique products that have been sold.")

    # Q: What is the most expensive product sold?
    most_expensive_product = sales.loc[sales["Unit_Price"].idxmax()]
    print(f"""The most expensive product sold is: 
    {most_expensive_product}""")
    
    # Q: What is the cheapest expensive product sold?
    cheapest_product = sales.loc[sales["Unit_Price"].idxmin()]
    print(f"""The cheapest product sold is: 
    {cheapest_product}""")
        
    # Q: Which product has the highest profit?
    highest_product_profit =  sales.groupby("Product_ID")["Total_Profit"].max().idxmax()
    print(f"The product with the highest profit is: ID {highest_product_profit}")


def customer_analysis(sales): # Analyze the customer to answer questions
    # Q: What category of costumer spent the most money; new or returning?
    highest_spending_customer = sales.groupby("Customer_Type")["Total_Profit"].sum().idxmax()
    print(f"The customer category that spent the most money is: {highest_spending_customer}")


def main():
    sales = load_data()
    sales = create_columns(sales)
    data_summary(sales)
    check_missing_values(sales)
    product_analysis(sales)
    product_category_analysis(sales)
    customer_analysis(sales)


if __name__ == "__main__":
    main()
