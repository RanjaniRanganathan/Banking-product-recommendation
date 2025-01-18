import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Connect to Oracle Database
# -------------------------------

conn = cx_Oracle.connect("system", "system", "localhost:1521/xe")
cursor = conn.cursor()
print("Database connection established!")

# -------------------------------
# Step 2: Fetch Data from Tables
# -------------------------------

# Fetch CUSTOMERS data
cursor.execute("SELECT * FROM CUSTOMERS")
column_customers = [col[0] for col in cursor.description]  
customers_data = pd.DataFrame(cursor.fetchall(), columns=column_customers)
print("\nCUSTOMERS DataFrame:")
print(customers_data)

# Fetch INVESTMENT_PRODUCTS data
cursor.execute("SELECT * FROM INVESTMENT_PRODUCTS")
column_products = [col[0] for col in cursor.description]
product_data = pd.DataFrame(cursor.fetchall(), columns=column_products)
print("\nINVESTMENT_PRODUCTS DataFrame:")
print(product_data)

# Fetch INVESTMENT_RECOMMENDATIONS data
cursor.execute("SELECT * FROM INVESTMENT_RECOMMENDATIONS")
column_recommendations = [col[0] for col in cursor.description]
recommendations_data = pd.DataFrame(cursor.fetchall(), columns=column_recommendations)
print("\nINVESTMENT_RECOMMENDATIONS DataFrame:")
print(recommendations_data)

# -------------------------------
# Step 3: High-Return Products
# -------------------------------

# Query to get products with a return rate greater than 10%
query_high_return = "SELECT PRODUCT_NAME, RETURN_RATE FROM INVESTMENT_PRODUCTS WHERE RETURN_RATE > 10"
cursor.execute(query_high_return)
high_return_products = cursor.fetchall()

print("\nHigh-Return Products:")
for product in high_return_products:
    print(product)

# -------------------------------
# Step 4: Summarize Risk Tolerance
# -------------------------------

# Count customers by risk tolerance
query_risk_tolerance = "SELECT RISK_TOLERANCE, COUNT(*) FROM CUSTOMERS GROUP BY RISK_TOLERANCE"
cursor.execute(query_risk_tolerance)
risk_data = {row[0]: row[1] for row in cursor.fetchall()}  # Convert query result to dictionary

print("\nCustomer Count by Risk Tolerance:")
for key, value in risk_data.items():
    print(f"{key} Risk: {value} Customers")

# -------------------------------
# Step 5: Add Recommendations Logic
# -------------------------------

# Define recommendation logic
def recommend_products(risk_tolerance):
    if risk_tolerance == 'Low':
        return 'Fixed Deposit'
    elif risk_tolerance == 'High':
        return 'Mutual Funds'
    else:
        return 'ULIP'

customers_data['Recommended_Product'] = customers_data['RISK_TOLERANCE'].apply(recommend_products)
print("\nUpdated CUSTOMERS DataFrame with Recommendations:")
print(customers_data[['CUSTOMER_NAME', 'RISK_TOLERANCE', 'Recommended_Product']])

# -------------------------------
# Step 6: Visualization
# -------------------------------

# Bar Chart: Risk Tolerance Distribution
plt.bar(risk_data.keys(), risk_data.values(), color=['green', 'orange', 'red'])
plt.title('Customer Risk Tolerance Distribution')
plt.xlabel('Risk Tolerance')
plt.ylabel('Number of Customers')
plt.savefig("risk_tolerance_distribution.png")  # Save the chart
plt.show()


# -------------------------------
# Step 8: Add User Interaction
# -------------------------------

# Allow user to fetch recommendation for a specific customer
customer_id = int(input("Enter Customer ID to fetch recommendations: "))
customer_info = customers_data[customers_data['CUSTOMER_ID'] == customer_id]

if not customer_info.empty:
    print(f"Customer Name: {customer_info['CUSTOMER_NAME'].values[0]}")
    print(f"Recommended Product: {customer_info['Recommended_Product'].values[0]}")
else:
    print("Customer not found.")

# -------------------------------
# Step 9: Close Database Connection
# -------------------------------
cursor.close()
conn.close()
print("Database connection closed.")
