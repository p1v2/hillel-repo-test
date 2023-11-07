from db import Student, Mark, Teacher


def serialize_db_student(student: Student):
    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
    }


def serialize_db_mark(mark: Mark):
    return {
        "id": mark.id,
        "value": mark.value,
        "timestamp": mark.timestamp,
    }


def serialize_db_teacher(teacher: Teacher):
    return {
        "id": teacher.id,
        "name": teacher.name,
        "subject": teacher.subject,
        "timestamp": teacher.start_of_work
    }


def serialize_db_teacher_with_marks(teacher: Teacher):
    return {
        **serialize_db_teacher(teacher),
        "marks": [serialize_db_mark(mark) for mark in teacher.marks]
    }


def serialize_db_student_with_marks(student: Student):
    return {
        **serialize_db_student(student),
        "marks": [serialize_db_mark(mark) for mark in student.marks]
    }


def serialize_db_mark_with_student(mark: Mark):
    return {
        **serialize_db_mark(mark),
        "student": serialize_db_student(mark.student)
    }
