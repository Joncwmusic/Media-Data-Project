import sqlite3

def create_database(table_name, cols={}):
    """Creates an SQLite database file with a 'users' table."""
    # Connect to the database file. It will be created if it doesn't exist.
    try:
        conn = sqlite3.connect(table_name)
        cursor = conn.cursor() # Create a cursor object to execute SQL commands
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name}
                
            )
        ''')

        cursor.execute("INSERT INTO {table_name} (name, age) VALUES ('Alice', 30)")
        cursor.execute("INSERT INTO {table_name} (name, age) VALUES ('Bob', 25)")

        # Commit (save) the changes to the database file
        conn.commit()

        print("Database 'my_database.db' and table 'users' created successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
    return None


def create_table(table_name, new_data):
    return None


def append_table(table_name, new_data):
    return None


def merge_table(table_name, new_data):
    return None
