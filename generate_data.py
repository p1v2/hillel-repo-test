from peewee import fn
from random import randint

from db import Student, Mark, Teacher

for _ in range(1000):
    # Get random student
    student = Student.select().order_by(fn.Random()).get()

    # Get random teacher
    teacher = Teacher.select().order_by(fn.Random()).get()

    # Generate mark
    Mark.create(student=student, teacher=teacher, value=randint(60, 100))
