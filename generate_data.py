from peewee import fn
from random import randint
from db import Student, Mark, Teacher

students_data = [
    {"name": "Serega", "age": 19},
    {"name": "Danil", "age": 22},
    {"name": "Alex", "age": 30},
]


for student_data in students_data:
    Student.create(**student_data)

teachers_data = [
    {"name": "Teacherone", "subject": "Math"},
    {"name": "Teachertwo", "subject": "History"},
    {"name": "Teacherthree", "subject": "Physics"},
]


for teacher_data in teachers_data:
    Teacher.create(**teacher_data)

# Get all students and teachers
students = Student.select()
teachers = Teacher.select()

for _ in students:
    student = Student.select().order_by(fn.Random()).get()

    teacher = Teacher.select().order_by(fn.Random()).get()

    Mark.create(student=student,teacher=teacher, value=randint(60, 100))
