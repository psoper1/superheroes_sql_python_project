from database.db_connection import execute_query

def get_names():
    query = "SELECT id, name FROM heroes ORDER BY id Asc"
    names = execute_query(query).fetchall()
    for count, x in names:
        print(f"ID|{count} - {x}")