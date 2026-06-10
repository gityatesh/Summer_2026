from sql.database import DatabaseConnector

def generate_database_reports():
    print("Connecting to PostgreSQL Analytics Engine...\n")
    db = DatabaseConnector()

    # 1. Execute Customer Spending Query
    print("=== CUSTOMER LEADERBOARD ===")
    spending_query = """
        SELECT c.customer_name, SUM(t.amount) AS total_spent
        FROM customers c
        JOIN transactions t ON c.customer_id = t.customer_id
        GROUP BY c.customer_name
        ORDER BY total_spent DESC;
    """
    spending_data = db.execute_read_query(spending_query)
    
    # RealDictCursor allows us to access SQL columns like a dictionary
    if spending_data:
        for row in spending_data:
            print(f"Customer: {row['customer_name']} | Total Spent: ${row['total_spent']}")
    else:
        print("No data found.")

    # 2. Execute Category Sales Query
    print("\n=== CATEGORY SALES ===")
    category_query = """
        SELECT category, SUM(amount) AS total_sales
        FROM transactions
        GROUP BY category
        ORDER BY total_sales DESC;
    """
    category_data = db.execute_read_query(category_query)
    
    if category_data:
        for row in category_data:
            print(f"Category: {row['category']} | Total Revenue: ${row['total_sales']}")
    else:
        print("No data found.")

if __name__ == "__main__":
    generate_database_reports()