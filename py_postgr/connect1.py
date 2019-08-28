# https://stackabuse.com/working-with-postgresql-in-python/
import psycopg2

con = psycopg2.connect(database="xmkvsriw", user="xmkvsriw", password="0HlF-y1j5NUUszyn-2PqhgfJ-SJPPyWL", 
                       host="elmer.db.elephantsql.com", port="5432")

print("Database opened successfully")

cur = con.cursor()
cur.execute("SELECT id, nome, modelo, ano, fabricante from carros")
rows = cur.fetchall()

for row in rows:
    print("id =", row[0])
    print("Nome =", row[1])
    print("Modelo =", row[2])
    print("Ano =", row[3])
    print("Fabricante =", row[4], "\n")

print("Operation done successfully")
con.close()