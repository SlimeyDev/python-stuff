import sqlite3

conn = sqlite3.connect("test_database.db")

c = conn.cursor()

c.execute("""CREATE TABLE test_table (
    test1 text,
    test2 text,
    test3 text
)""")

conn.commit()

conn.close()