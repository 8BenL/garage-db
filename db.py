import sqlite3

def query_db(sql):
    with sqlite3.connect("cars.sqlite") as conn:
        cur=conn.cursor()
        res=cur.execute(sql)
        try:
            return res.fetchall()
        except:
            return []

def setup_db():
    query_db("CREATE TABLE IF NOT EXISTS cars(name, year, color, number)")
    query_db("INSERT INTO cars VALUES ('toyota', '2012', 'blue', '7656577')")

def save(cars:list):
    for car in cars:
        query_db(f"INSERT INTO cars VALUES ('{car.name}', '{car.year}', '{car.color}', '{car.number}')")


def load():
    return str(query_db("SELECT * FROM cars"))

setup_db()
print(load())