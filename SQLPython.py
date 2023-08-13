import sqlite3

def main():
    # Connect to a SQLite database (or create one if it doesn't exist)
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Define and execute an SQL SELECT query
    query = "SELECT * FROM customers;"
    cursor.execute(query)

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()
