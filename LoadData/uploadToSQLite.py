import sqlite3
import pandas as pd
import os

def create_sqlite_db(db_name):
    folder_name = f"../data/"
    db_path = folder_name + db_name
    print(db_path)

    # Connect (this creates the file in the 'data' folder)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    conn.commit()
    conn.close()

def replace_table_with_df(df, db_path, table_name):
    """
    df : The DataFrame containing the data.
    db_path : Path to the SQLite database file
    table_name : Name of the table to create or update.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"Table '{table_name}' successfully written to '{db_path}' ({len(df)} rows).")
    except Exception as e:
        print(f"Error writing table '{table_name}' to database: {e}")
    return None


def append_df_to_table(df, db_path, table_name):
    """
        df : The DataFrame containing the data.
        db_path : Path to the SQLite database file
        table_name : Name of the table to create or update.
        """
    try:
        with sqlite3.connect(db_path) as conn:
            df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"Table '{table_name}' successfully written to '{db_path}' ({len(df)} rows).")
    except Exception as e:
        print(f"Error writing table '{table_name}' to database: {e}")
    return None


def merge_table(table_name, new_data):

    return None