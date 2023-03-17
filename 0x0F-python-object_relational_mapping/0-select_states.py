#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.

import MySQLdb
import sys

if __name__ == '__main__':
    # Get the mysql username, password and database name
    # from command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost", port=3306, user=mysql_user,
            passwd=mysql_password, db=db_name)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute a SELECT query to get all the states from the database
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
