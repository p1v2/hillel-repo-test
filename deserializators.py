from flask import request


def deserialize_student_data():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    return {
        "name": name,
        "age": age
    }


def deserialize_teacher_data():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    subject = data.get("subject")

    return {
        "name": name,
        "age": age,
        "subject": subject
    }


def deserialize_mark_data():
    data = request.get_json()

    teacher_id = data.get("teacher_id")
    student_id = data.get("student_id")
    value = data.get("value")

    return {
        "teacher_id": teacher_id,
        "student_id": student_id,
        "value": value
   }


