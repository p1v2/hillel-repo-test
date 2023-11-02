from flask import request


def deserialize_student_data():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    return {
        "name": name,
        "age": age
    }


def deserialize_mark_data():
    data = request.get_json()

    student_id = data.get("student_id")
    value = data.get("value")

    return {
        "student_id": student_id,
        "value": value
   }