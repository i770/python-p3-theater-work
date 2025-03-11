import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Query the roles table
print("Roles:")
cursor.execute("SELECT * FROM roles;")
roles = cursor.fetchall()
for role in roles:
    print(role)

# Query the auditions table
print("\nAuditions:")
cursor.execute("SELECT * FROM auditions;")
auditions = cursor.fetchall()
for audition in auditions:
    print(audition)

# Close the connection
conn.close()
