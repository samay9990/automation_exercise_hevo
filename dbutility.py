from datetime import datetime

import mysql.connector
from mysql.connector import connection


def create_table(connection):
    cursor = connection.cursor()
    try:
        # Define the table creation query
        create_table_query = "CREATE TABLE IF NOT EXISTS Automate_Test (id INT PRIMARY KEY, test_name VARCHAR(255), last_modified TIMESTAMP)"

        # Execute the query
        cursor.execute(create_table_query)
        print("Table created successfully")
    except mysql.connector.Error as error:
        print("Error creating table: {}".format(error))
    finally:
        cursor.close()


# def insert_record(connection, id, test_name):
#     try:
#         cursor = connection.cursor()
#         insert_query = "INSERT INTO Automate_Test (id, test_name, last_modified) VALUES (%s, %s, %s)"
#
#         # Get the current timestamp
#         current_timestamp = datetime.now()
#
#         record_to_insert = (id, test_name, current_timestamp)  # Using current_timestamp for last_modified
#
#         cursor.execute(insert_query, record_to_insert)
#         connection.commit()
#         print("Record inserted successfully")
#     except mysql.connector.Error as error:
#         print("Failed to insert record:", error)


# Insert a record
# insert_record(connection, "1", 'FIRST')

def main():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host="mysql-database-1.cx08aukg2czn.eu-north-1.rds.amazonaws.com",
            user="admin",
            password="Chocolatecake123*",
            database="automation"
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create the table
            create_table(connection)

    except mysql.connector.Error as error:
        print("Error connecting to MySQL: {}".format(error))
    finally:
        # Close the connection
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed")


if __name__ == "__main__":
    main()

# def execute_query(connection, query):
#     cursor = connection.cursor()
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#
#
# # Example query
# query = "SELECT * FROM automation.Automate_test"

# Execute the query
# execute_query(connection, query)

connection.close()
