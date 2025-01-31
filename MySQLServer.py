import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (Modify user and password accordingly)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this if needed
            password='Meek@2023'  # Change this if needed
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: Unable to connect to the database. {e}")
    
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
