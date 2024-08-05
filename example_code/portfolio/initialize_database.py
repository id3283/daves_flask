import mysql


def initialize_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
        )
        cursor = connection.cursor()
        # Perform database initialization tasks
        cursor.execute("CREATE TABLE IF NOT EXISTS example (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL)")
        connection.commit()
        cursor.close()
        connection.close()
        print("Database initialized successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")