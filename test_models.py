import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create tables if they don't exist (for testing purposes)
cursor.execute('''
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY,
    character_name TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS auditions (
    id INTEGER PRIMARY KEY,
    actor TEXT NOT NULL,
    location TEXT NOT NULL,
    phone INTEGER,
    hired BOOLEAN,
    role_id INTEGER,
    FOREIGN KEY(role_id) REFERENCES roles(id)
);
''')

# Test creating a role
cursor.execute("INSERT INTO roles (character_name) VALUES ('Test Role');")
conn.commit()

# Test querying the role
cursor.execute("SELECT * FROM roles;")
roles = cursor.fetchall()
print("Roles in the database:", roles)  # Confirm roles retrieval

# Test creating an audition
cursor.execute("INSERT INTO auditions (actor, location, phone, hired, role_id) VALUES ('Test Actor', 'Test Location', 1234567890, 1, 1);")

# Test creating an audition
cursor.execute("INSERT INTO auditions (actor, location, phone, hired, role_id) VALUES ('Test Actor', 'Test Location', 1234567890, 1, 1);")
conn.commit()

# Test querying the audition
cursor.execute("SELECT * FROM auditions;")
auditions = cursor.fetchall()
print("Auditions in the database:", auditions)  # Confirm auditions retrieval

# Close the connection
conn.close()
