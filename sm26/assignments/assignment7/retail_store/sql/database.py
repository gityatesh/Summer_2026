import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseConnector:
    def __init__(self):
        # In a real app, these would be hidden in a .env file.
        # For this local Docker test, we can hardcode them.
        self.host = "localhost"
        self.port = "5432"
        self.database = "retail_db"
        self.user = "postgres"
        self.password = "Yatesh1234?"

    def get_connection(self):
        """Creates and returns a connection to the database."""
        try:
            return psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except Exception as e:
            print(f"Failed to connect to database: {e}")
            return None

    def execute_read_query(self, query: str):
        """Executes a SELECT query and returns the rows as a list of dictionaries."""
        conn = self.get_connection()
        if not conn:
            return []

        try:
            # RealDictCursor makes the rows look like JSON objects instead of raw tuples
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            return []
        finally:
            cursor.close()
            conn.close()