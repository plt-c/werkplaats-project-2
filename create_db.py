#DATABASE STRUCTUUR

from models.student_model import get_db

conn = get_db()
cur = conn.cursor()

#STUDENTEN TABEL

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birthdate TEXT NOT NULL,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES classes(id)
)
""")

#KLASSEN TABEL
cur.execute("""
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT UNIQUE NOT NULL
)
""")

conn.commit()
conn.close()

print("Database aangemaakt!")

