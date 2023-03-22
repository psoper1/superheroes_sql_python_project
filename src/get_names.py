from database.db_connection import execute_query

def get_names():
    query = "SELECT name FROM heroes ORDER BY id Asc"
    names = execute_query(query).fetchall()
    for count, x in enumerate(names):
        print(f"{count + 1}: {x[0]}")