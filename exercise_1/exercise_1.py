def exercise_1(inputs): # DO NOT CHANGE THIS LINE
    """
    This functions receives the input in the parameter 'inputs'. 
    Change the code, so that the output is sqaure of the given input.
    
    p, q, r = inputs
    
    p => ['t101', 't102', 't103']
    q => ['s101', 's102', 's103']
    r => {
        'l101':['t101': ['s101', 's102']], 
        'l102': ['s101', 's102', 's103']]
    }
    
    output = [Person, Teacher, Student, Lecture]
    """
    
    from abc import ABC

class Person(ABC):
    def addname(self, name):
        self.name = name
        pass

class Student(Person):
    lectures_enrolled = []
    def addlec(self,lectures_enrolled):
        if (len(self.lectures_enrolled) >= 3):
            print("lecture is at max")
        else:
            self.lectures_enrolled.append(lectures_enrolled)
    def add(self, name, student_id, lectures_enrolled):
        self.student_id = student_id
        self.lectures_enrolled.append(lectures_enrolled)
        super().addname(name)

class Teacher(Person):
    def add(self, name, teacher_id, lecture_taught):
        self.teacher_id = teacher_id
        self.lecture_taught = lecture_taught
        super().addname(name)

class Lecture:
    lecturer_list=[]
    students_list=[]
    def assign_teacher(self, Teacher):
        self.lecturer_list.append(Teacher)
    def assign_students(self, Student):
        self.students_list.append(Student)
    def get_teacher(self):
        for lecturer in lecturer_list:
            print(lecturer.name)
            print(lecturer.teacher_id)
    def get_students(self):
        for students in students_list:
            print(students.name)
            print(students.student_id)
    
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
