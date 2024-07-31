import mysql.connector
from mysql.connector import Error

# Define the transfer parameters
account_from = 1
account_to = 2
transfer_amount = 100.00

try:
    # Establish a connection to the database
    with mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
    ) as connection:

        # Create a cursor object
        with connection.cursor() as cursor:

            try:
                # Start a transaction
                connection.start_transaction()

                # Check balance of Account A
                cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_from,))
                account_from_balance = cursor.fetchone()[0]

                if account_from_balance < transfer_amount:
                    raise ValueError("Insufficient funds in Account A")

                # Class: both operations or no operations

                # Debit Account A
                cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s",
                               (transfer_amount, account_from))

                # Credit Account B
                cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s",
                               (transfer_amount, account_to))

                # Commit the transaction
                connection.commit()
                print("Transaction committed successfully")

            except (mysql.connector.Error, Exception) as err:
                # Rollback in case of any error
                print(f"Error: {err}")
                connection.rollback()

except Error as err:
    # Handle errors related to connecting to the database
    print(f"Connection error: {err}")

# No need for explicit close statements, as context managers handle that automatically