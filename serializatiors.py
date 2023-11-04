from db import Student, Mark, Teacher


def serialize_db_student(student: Student):
    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
    }


def serialize_db_mark(mark):
    return {
        "id_of_mark": mark.id,
        "name_of_student":mark.student.name,
        "value": mark.value,
        "teacher": mark.teacher.name,
        "subject":mark.teacher.subject,
        "timestamp": mark.timestamp,
    }
def serialize_db_teachers(teacher):
    return {
        "id_teacher": teacher.id,
        "name": teacher.name,
        "subject": teacher.subject
    }

def serialize_db_teacher_with_id(teacher):
    return {
        "teacher": [serialize_db_teachers(teacher)]
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
