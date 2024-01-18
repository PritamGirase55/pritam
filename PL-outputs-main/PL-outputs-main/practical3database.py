import sqlite3

# Connect to SQLite database (or create if not exists)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS cricket_equipment (
        id INTEGER PRIMARY KEY,
        product_name TEXT,
        price REAL
    )
'''
cursor.execute(create_table_query)

# Insert data into the table
insert_data_query = "INSERT INTO cricket_equipment (product_name, price) VALUES (?, ?)"
data_to_insert = [('Cricket Bat', 49.99), ('Cricket Ball', 9.99), ('Cricket Helmet', 29.99)]

cursor.executemany(insert_data_query, data_to_insert)

# Commit the changes
conn.commit()

# Print the records in the table
select_query = "SELECT * FROM cricket_equipment"
cursor.execute(select_query)

print("Records in the cricket_equipment table:")
for row in cursor.fetchall():
    print(row)

# Update a record
update_query = "UPDATE cricket_equipment SET price = ? WHERE product_name = ?"
update_data = (39.99, 'Cricket Bat')
cursor.execute(update_query, update_data)
conn.commit()

# Print the updated records
cursor.execute(select_query)
print("\nRecords after updating the price:")
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
