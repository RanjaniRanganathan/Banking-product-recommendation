# Banking Product Recommendation System
A SQL-Python project recommending banking products based on customer requirements.

## Overview
This project demonstrates a banking product recommendation system using Oracle SQL and Python. It analyzes customer data and provides product recommendations based on customer requirements and risk tolerance.

## Features
- Analyze customer and product data from an Oracle database.
- Generate product recommendations using Python logic.
- Visualize insights with bar charts.
- Export recommendations to an Excel file.

## Technologies Used
- **Oracle SQL**
- **Python**: cx_Oracle, pandas, matplotlib

## How to Run
1. **Set up the Oracle SQL Database**:
   - Execute the SQL scripts in the `sql/` folder:
     - `create_tables.sql`: Creates the necessary tables.
     - `insert_data.sql`: Inserts sample data into the tables.

2. **Run the Python Script**:
   - Install Python dependencies:
     ```bash
     pip install cx_Oracle pandas matplotlib
     ```
   - Run the Python script:
     ```bash
     python python/banking_recommendation.py
     ```

3. **View Outputs**:
   - Visualizations (e.g., bar charts) will be saved in the `visualizations/` folder.

## Outputs
- **Bar Chart**: Visualizes customer distribution by risk tolerance.
Example insights:
  - "80% of customers prefer low-risk products like Fixed Deposits."
  - "Mutual Funds provide the highest return (15%) among all products."


