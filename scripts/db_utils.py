import pymysql

def get_connection(config):
    return pymysql.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

def get_table_schema(cursor, table_name):
    query = f"DESCRIBE {table_name}"
    cursor.execute(query)
    return cursor.fetchall()

def get_row_count(cursor, table_name):
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    return cursor.fetchone()[0]

def get_sample_rows(cursor, table_name, limit=10):
    query = f"SELECT * FROM {table_name} LIMIT {limit}"
    cursor.execute(query)
    return cursor.fetchall()
