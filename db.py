import logging
from datetime import datetime

from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DateTimeField

logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = SqliteDatabase('sqlite3.db')

class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    name = CharField()
    age = IntegerField()

class Teacher(BaseModel):
    name = CharField()
    subject = CharField()

class Mark(BaseModel):
    student = ForeignKeyField(Student, backref='marks')
    teacher = ForeignKeyField(Teacher, backref='subjects')  # Link to the Teacher model using the appropriate field
    value = IntegerField()
    timestamp = DateTimeField(default=datetime.now)

"""import os

# Replace 'your_database.db' with your actual database file path
db_file = 'sqlite3.db'

# Close the database connection if it's open
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"The database file '{db_file}' has been deleted.")
else:
    print(f"The database file '{db_file}' does not exist.")"""



if __name__ == "__main__":
    db.connect()
    db.create_tables([Student, Mark, Teacher])
    db.close()
    #Mark.delete().execute()
    #Student.delete().execute()
    #Teacher.delete().execute()