import mysql.connector
from mysql.connector import Error

from constants import DatabaseConfig


def query_without_context_manager(query):
    connection = None
    cursor = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
        )

        if connection.is_connected():
            print("Connected to MySQL server")

            # Create a cursor object using the cursor() method
            cursor = connection.cursor()

            # Execute the SQL query
            cursor.execute(query)

            # Fetch all the rows from the executed query
            result = cursor.fetchall()

            # Print the result
            for row in result:
                print(row)

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def query_with_context_manager(query):
    try:
        # Establish the connection using a context manager
        with mysql.connector.connect(
                host=DatabaseConfig.HOST,
                user=DatabaseConfig.USER,
                password=DatabaseConfig.PASSWORD,
                database=DatabaseConfig.DATABASE
        ) as connection:
            if connection.is_connected():
                print("Connected to MySQL server")

                # Create a cursor object using a context manager
                with connection.cursor() as cursor:
                    # Execute the SQL query
                    cursor.execute(query)

                    # Fetch all the rows from the executed query
                    result = cursor.fetchall()

                    # Print the result
                    for row in result:
                        print(row)

    except Error as e:
        print("Error while connecting to MySQL", e)


# Define your SQL query
sql_query = "SELECT * FROM users"

# Execute the query
query_with_context_manager(sql_query)
