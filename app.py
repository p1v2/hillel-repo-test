from flask import Flask, jsonify, request
from peewee import fn

from db import Student, Mark, Teacher
from deserializators import deserialize_student_data, deserialize_mark_data, deserialize_teacher_data
from serializatiors import serialize_db_student, serialize_db_mark, serialize_db_student_with_marks, \
    serialize_db_teachers, serialize_db_teacher_with_id
from validators import validate_student_data, ValidationError, validate_mark_data, validate_teacher_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World"})


@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify({"message": str(error)})
    response.status_code = 422

    return response


@app.route('/students', methods=["GET", "POST"])
def students_api():
    if request.method == "GET":
        # Get name from query params
        filter_name = request.args.get("name")

        students = Student.select(Student, fn.AVG(Mark.value).alias("avg_mark")).join(Mark).group_by(Student).order_by(
            fn.AVG(Mark.value).desc())
        #students = Student.select()

        if filter_name:
            students = students.where(Student.name.contains(filter_name))

        return jsonify([serialize_db_student(student) for student in students])
    elif request.method == "POST":
        data = deserialize_student_data()

        validate_student_data(data)

        student = Student.create(**data)

        return jsonify(serialize_db_student(student)), 201


@app.route('/students/<int:student_id>', methods=["GET"])
def student_api(student_id):
    if request.method == "GET":
        student = Student.get_or_none(id=student_id)

        if not student:
            return jsonify({"message": "student not found"}), 404

        return jsonify(serialize_db_student_with_marks(student))


@app.route('/marks', methods=["GET", "POST"])
def marks_api():
    if request.method == "POST":
        data = deserialize_mark_data()

        validated_data = validate_mark_data(data)
        # validated_data["student"] = student

        mark = Mark.create(**validated_data)
        # mark.student = student

        return jsonify(serialize_db_mark(mark)), 201
    if request.method == "GET":
        marks = Mark.select(Mark, Student).join(Student).join_from(Mark,Teacher)

        return jsonify([serialize_db_mark(mark) for mark in marks])

@app.route('/teachers', methods=["GET", "POST"])
def teachers_api():
    if request.method == "POST":

        data = deserialize_teacher_data()

        validate_teacher_data(data)
        # validated_data["student"] = student

        teacher = Teacher.create(**data)
        # mark.student = student

        return jsonify(serialize_db_teachers(teacher)), 201
    if request.method == "GET":
        #marks = Mark.select(Mark, Student).join(Student)
        teachers = Teacher.select()

        return jsonify([serialize_db_teachers(teacher) for teacher in teachers])

@app.route('/teachers/<int:teacher_id>', methods=["GET"])
def teacher_api(teacher_id):
    if request.method == "GET":
        teacher = Teacher.get_or_none(id=teacher_id)

        if not teacher:
            return jsonify({"message": "teacher not found"}), 404

        return jsonify(serialize_db_teacher_with_id(teacher))

@app.route('/delteacher', methods=["DELETE"])
def del_teacher_with_data():
    if request.method == "DELETE":
        data = deserialize_teacher_data()

        if not data:
            return jsonify({"error": "Can`t get teacher`s data"}), 400

        teacher_to_delete = Teacher.get_or_none(Teacher.name == data["name"],Teacher.subject == data["subject"])

        if teacher_to_delete:
            teacher_to_delete.delete_instance()
            return jsonify({"message": "Teacher has been deleted"}), 200
        else:
            return jsonify({"error": "The teacher not found"}), 404

@app.route('/delteacher_id/<int:teacher_id>', methods=["DELETE"])
def del_teacher_with_id(teacher_id):
    if request.method == "DELETE":
        teacher_to_delete = Teacher.get_or_none(id=teacher_id)
        if teacher_to_delete:
            teacher_to_delete.delete_instance()
            return jsonify({"message": "Teacher has been deleted"}), 200
        else:
            return jsonify({"error": "The teacher not found"}), 404

@app.route('/updateteacher/<teacher_id>', methods=["PATCH"])
def update_teacher_with_id(teacher_id):
    if request.method == "PATCH":
        data = deserialize_teacher_data()

        if not data:
            return jsonify({"error": "Can't get teacher's data"}), 400

        validate_teacher_data(data)

        teacher_to_update = Teacher.get_or_none(id = teacher_id)

        if teacher_to_update:
            new_name = data.get("name")
            new_subject = data.get("subject")

            if new_name.replace(" ","").isalpha():  # Проверка, что имя состоит только из букв
                teacher_to_update.name = new_name
                teacher_to_update.subject = new_subject
                teacher_to_update.save()
                return jsonify({"message": "Teacher has been updated"}), 200
            else:
                return jsonify({"error": "Name can only contain letters"}), 400
        else:
            return jsonify({"error": "The teacher not found"}), 404



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
