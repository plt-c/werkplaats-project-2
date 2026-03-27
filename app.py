from flask import Flask, render_template, request, redirect, url_for
from models.student_model import (
    get_all_students,
    add_student,
    delete_student,
    get_student_by_id,
    update_student,
    get_all_classes,
    add_class,
    get_class_by_id,
    update_class,
    get_students_by_class
)
from datetime import date

app = Flask(__name__)




#HOME PAGE
@app.get("/")
def home():
    return render_template("index.html", title="Home")




#ROUTES VAN STUDENTEN
@app.get("/students")
def students():
    rows = get_all_students()
    today = date.today()

    students_with_age = []
    for s in rows:
        y, m, d = map(int, s["birthdate"].split("-"))
        age = today.year - y - ((today.month, today.day) < (m, d))

        students_with_age.append({
            "id": s["id"],
            "first_name": s["first_name"],
            "last_name": s["last_name"],
            "birthdate": s["birthdate"],
            "age": age,
            "class_name": s["class_name"]
        })

    return render_template("student.html", students=students_with_age, title="Studenten")


@app.get("/students/add")
def add_student_form():
    today = date.today().isoformat()
    classes = get_all_classes()
    return render_template("add_student.html", today=today, classes=classes, title="Student toevoegen")


@app.post("/students/add")
def add_student_submit():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    birthdate = request.form["birthdate"]
    class_id = request.form["class_id"]

    add_student(first_name, last_name, birthdate, class_id)
    return redirect(url_for("students"))


@app.get("/students/delete/<int:student_id>")
def delete_student_route(student_id):
    delete_student(student_id)
    return redirect(url_for("students"))


@app.get("/students/edit/<int:student_id>")
def edit_student_form(student_id):
    student = get_student_by_id(student_id)
    classes = get_all_classes()

    y, m, d = map(int, student["birthdate"].split("-"))
    today = date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))

    return render_template(
        "edit_student.html",
        student=student,
        age=age,
        today=today.isoformat(),
        classes=classes,
        title="Student bewerken"
    )


@app.post("/students/edit/<int:student_id>")
def edit_student_submit(student_id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    birthdate = request.form["birthdate"]
    class_id = request.form["class_id"]

    update_student(student_id, first_name, last_name, birthdate, class_id)
    return redirect(url_for("students"))



#ROUTES VAN KLASSEN


@app.get("/classes")
def classes():
    rows = get_all_classes()
    return render_template("classes.html", classes=rows, title="Klassen")


@app.get("/classes/add")
def add_class_form():
    return render_template("add_class.html", title="Klas toevoegen")


@app.post("/classes/add")
def add_class_submit():
    name = request.form["class_name"].strip().upper()
    full_name = f"POC-{name}"

    success = add_class(full_name)
    if not success:
        return "Deze klas bestaat al!"

    return redirect("/classes")


@app.get("/classes/edit/<int:class_id>")
def edit_class_form(class_id):
    class_item = get_class_by_id(class_id)
    return render_template("edit_classes.html", class_item=class_item, title="Klas bewerken")


@app.post("/classes/edit/<int:class_id>")
def edit_class_submit(class_id):
    name = request.form["class_name"].strip().upper()
    full_name = f"POC-{name}"

    success = update_class(class_id, full_name)
    if not success:
        return "Deze klas bestaat al!"

    return redirect("/classes")


@app.get("/classes/<int:class_id>")
def class_detail(class_id):
    class_item = get_class_by_id(class_id)
    students = get_students_by_class(class_id)

    return render_template(
        "class_detail.html",
        class_item=class_item,
        students=students,
        title=f"Studenten in {class_item['class_name']}"
    )


if __name__ == "__main__":
    app.run(debug=True)
