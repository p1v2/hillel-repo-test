from db import Student, Teacher


class ValidationError(Exception):
    pass


def validate_student_data(data):
    name = data.get("name")
    age = data.get("age")

    if not (name and age):
        raise ValidationError("name and age are required")

    if not isinstance(age, int):
        raise ValidationError("age must be integer")
    if not isinstance(name, str):
        raise ValidationError("name must be string")

    if age < 0:
        raise ValidationError("age must be positive")
    if name == "":
        raise ValidationError("name must not be empty")


def validate_mark_data(data):
    student_id = data.get("student_id")
    value = data.get("value")

    student = Student.get_or_none(id=student_id)

    if not student:
        raise ValidationError("student with such id does not exist")

    if not (student_id and value):
        raise ValidationError("student_id and value are required")

    if not isinstance(student_id, int):
        raise ValidationError("student_id must be integer")
    if not isinstance(value, int):
        raise ValidationError("value must be integer")

    if value < 0:
        raise ValidationError("value must be positive")

    data["student"] = student
    return data

def validate_teacher_data(data):
    t_name = data.get("name")
    t_subject = data.get("subject")

    if not (t_name and t_subject):
        raise ValidationError("name and subject are required")

    if not isinstance(t_name, str):
        raise ValidationError("name must be string")
    if not isinstance(t_subject, str):
        raise ValidationError("subject must be string")

    if len(t_name) < 3:
        raise ValidationError("too short name")
    if t_subject == "":
        raise ValidationError("subject must not be empty")

