import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseConnector:
    def __int__(self):
        self.host = 'localhost'
        self.port = '5432'
