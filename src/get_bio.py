from database.db_connection import execute_query

def get_bio():
    update = input("\nSelect a hero:\n")
    query = f"SELECT name from heroes WHERE id = {update}"
    query3 = f"SELECT biography from heroes WHERE id = {update}"
    name = execute_query(query).fetchone()
    update_query = execute_query(query3).fetchone()
    print(f"\n\nHERO: {name[0]}\n\nBIO: {update_query[0]}\n")