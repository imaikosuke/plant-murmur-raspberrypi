import psycopg2
from get_conn import get_connection_uri

conn_string = get_connection_uri()

conn = psycopg2.connect(conn_string) 
print("Connection established")
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS conditions (
        id SERIAL PRIMARY KEY,
        moisture INT NOT NULL,
        timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
''')
print("create conditions table")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS photos (
        photo_id SERIAL PRIMARY KEY,
        photo_url VARCHAR(255) NOT NULL,
        timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
''')
print("create photos table")

# Clean up
conn.commit()
cursor.close()
conn.close()

print("Tables created successfully.")
