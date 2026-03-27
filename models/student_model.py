import sqlite3

#DATABASE CONNECTIE
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


#STUDENTEN VERWERKING

def add_student(first_name, last_name, birthdate, class_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (first_name, last_name, birthdate, class_id) VALUES (?, ?, ?, ?)",
        (first_name, last_name, birthdate, class_id)
    )
    conn.commit()
    conn.close()


def get_all_students():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT students.*, classes.class_name
        FROM students
        LEFT JOIN classes ON students.class_id = classes.id
        ORDER BY students.id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_student_by_id(student_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT students.*, classes.class_name
        FROM students
        LEFT JOIN classes ON students.class_id = classes.id
        WHERE students.id = ?
    """, (student_id,))
    row = cur.fetchone()
    conn.close()
    return row


def update_student(student_id, first_name, last_name, birthdate, class_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET first_name = ?, last_name = ?, birthdate = ?, class_id = ?
        WHERE id = ?
    """, (first_name, last_name, birthdate, class_id, student_id))
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()



#KLASSEN VERWERKING

def get_all_classes():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM classes ORDER BY class_name")
    rows = cur.fetchall()
    conn.close()
    return rows


def add_class(class_name):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM classes WHERE class_name = ?", (class_name,))
    existing = cur.fetchone()
    if existing:
        conn.close()
        return False

    cur.execute("INSERT INTO classes (class_name) VALUES (?)", (class_name,))
    conn.commit()
    conn.close()
    return True


def get_class_by_id(class_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM classes WHERE id = ?", (class_id,))
    row = cur.fetchone()
    conn.close()
    return row


def update_class(class_id, class_name):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM classes WHERE class_name = ?", (class_name,))
    existing = cur.fetchone()
    if existing:
        conn.close()
        return False

    cur.execute("""
        UPDATE classes
        SET class_name = ?
        WHERE id = ?
    """, (class_name, class_id))

    conn.commit()
    conn.close()
    return True


def get_students_by_class(class_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT students.*, classes.class_name
        FROM students
        LEFT JOIN classes ON students.class_id = classes.id
        WHERE class_id = ?
        ORDER BY students.last_name
    """, (class_id,))
    rows = cur.fetchall()
    conn.close()
    return rows
