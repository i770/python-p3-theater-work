import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Insert sample data into roles table
cursor.execute("INSERT INTO roles (character_name) VALUES ('Lead Actor');")
cursor.execute("INSERT INTO roles (character_name) VALUES ('Supporting Actor');")

# Insert sample data into auditions table
cursor.execute("INSERT INTO auditions (actor, location, phone, hired, role_id) VALUES ('John Doe', 'Theater A', 1234567890, 1, 1);")
cursor.execute("INSERT INTO auditions (actor, location, phone, hired, role_id) VALUES ('Jane Smith', 'Theater B', 9876543210, 0, 2);")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Sample data inserted successfully.")
