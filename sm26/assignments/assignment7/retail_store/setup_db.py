from sql.database import DatabaseConnector

def initialize_database():
    print("Connecting to PostgreSQL Container...")
    db = DatabaseConnector()
    conn = db.get_connection()
    
    if not conn:
        print("Failed to connect. Is Docker running?")
        return

    cursor = conn.cursor()

    try:
        # Read and execute the table creation script
        with open('sql/create_tables.sql', 'r') as file:
            print("Creating tables...")
            cursor.execute(file.read())
            
        # Read and execute the data insertion script
        with open('sql/insert_data.sql', 'r') as file:
            print("Inserting data...")
            cursor.execute(file.read())
            
        # MUST commit the changes, or the database will roll them back
        conn.commit()
        print("Database successfully initialized and populated!")
        
    except Exception as e:
        print(f"A database error occurred: {e}")
        conn.rollback()
        
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    initialize_database()