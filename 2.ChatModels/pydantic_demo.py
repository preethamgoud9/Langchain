from pydantic import BaseModel

class Student(BaseModel):

    name:str = "preetham"


new_student = {}

student = Student(**new_student)
print(student)