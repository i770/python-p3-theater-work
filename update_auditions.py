import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Update the auditions table
cursor.execute("UPDATE auditions SET actor = 'Jacob' WHERE actor = 'John Doe';")
cursor.execute("UPDATE auditions SET actor = 'Judah' WHERE actor = 'Jane Smith';")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Audition records updated successfully.")
