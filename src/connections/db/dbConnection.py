import mysql.connector
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Replace these values with your own database information
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("dataBase")

# Establish a connection to the MySQL server


def insertMetaData(rawJSON):

    parsed_data = json.loads(rawJSON)
    connection = mysql.connector.connect(host=host,user=user,password=password,database=database)
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Replace 'your_table' with the actual table name
    table_name = "metadata"

    # Example data to insert
    data_to_insert = {
        "id": parsed_data["id"],
        "cpu": parsed_data["cpu"],
        "memory": parsed_data["memory"],
        "net": parsed_data["net"],
        "temp": parsed_data["temp"],
        "inserDT": parsed_data["inserDT"],
    }

    # Build the SQL INSERT statement
    insert_query = f"INSERT INTO {table_name} ({', '.join(data_to_insert.keys())}) VALUES ({', '.join(['%s']*len(data_to_insert))})"

    # Execute the query with the data
    cursor.execute(insert_query, tuple(data_to_insert.values()))

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()