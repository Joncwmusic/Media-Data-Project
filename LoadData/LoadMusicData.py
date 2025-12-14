# Given artists find all relevant artist data

# Need Followers, Popularity, Album Releases, Genres, Album Img URLS, and artist ID

#### Vibe coded slop to be refined
import sqlite3
import pandas as pd

# Sample dataframe
data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}
df = pd.DataFrame(data)

# SQLite database file
db_file = "local_db.sqlite"
table_name = "people"

# Connect to SQLite (creates file if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table if it doesn't exist
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
"""
cursor.execute(create_table_query)
conn.commit()

# Insert or replace rows from dataframe
for _, row in df.iterrows():
    cursor.execute(f"""
    INSERT OR REPLACE INTO {table_name} (id, name, age)
    VALUES (?, ?, ?)
    """, (row['id'], row['name'], row['age']))

conn.commit()
conn.close()
print(f"Data inserted/merged into {table_name} successfully.")
