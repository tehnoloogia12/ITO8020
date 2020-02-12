import sqlite3

print("ha")
conn = sqlite3.connect('proov.sql')
cur=conn.cursor()
cur.execute("select * from inimesed where sugu='n'");

print(cur.fetchall())