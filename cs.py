class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0
        self.courses_attached = []
        students_list.append(self.__dict__)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades += [grade]
            lecturer.average_score = round(sum(lecturer.grades) / len(lecturer.grades), 2)
    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average_score < other.average_score

    def __str__(self):
        return f'Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции: {self.average_score} \nКурсы в процессе изучения:{self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
                sum_hw = 0
                counter = 0
                for key, value in student.grades.items():
                    sum_hw += sum(value) / len(value)
                    counter += 1
                student.average_score = round(sum_hw / counter, 2)

    def __str__(self):
        return f'Имя:{self.name} \nФамилия:{self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = []
        self.courses_attached = []
        self.average_score = 0
        super().__init__(name, surname)
        lecturers_list.append(self.__dict__)

    def __str__(self):
        return f'Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции: {self.average_score}'


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_score < other.average_score

students_list = []
lecturers_list = []

def average_grade_hw(students, courses):
    sum_gh = 0
    counter = 0
    for student in students:
        for key, value in student['grades'].items():
            if courses in key:
                sum_gh += sum(value) / len(value)
                counter += 1
    return round(sum_gh / counter, 2)

def average_grade_lecture(lecturers, courses):
    sum_gl = 0
    counter = 0
    for lector in lecturers:
        if courses in lector["courses_attached"]:
           sum_gl += sum(lector["grades"]) / len(lector["grades"])
           counter += 1
    return round(sum_gl / counter, 2)

rachel = Student('Rachel', 'Green', 'r')
rachel.courses_in_progress += ['Fashion']
rachel.courses_in_progress += ['Cooking']

monica = Student('Monica', 'Geller', 'r')
monica.courses_in_progress += ['Cooking']
monica.finished_courses += ['Fashion']

ross = Lecturer('Ross', 'Geller')
ross.courses_attached += ['Cooking']

chandler = Lecturer('Chandler', 'Bing')
chandler.courses_attached += ['Fashion']

joey = Reviewer('Joey', 'Tribianni')
joey.courses_attached += ['Fashion']

foebe = Reviewer('Foebe', 'Buffe')
foebe.courses_attached += ['Cooking']


joey.rate_hw(rachel, 'Fashion', 7)
joey.rate_hw(rachel, 'Fashion', 5)
joey.rate_hw(rachel, 'Fashion', 3)
joey.rate_hw(monica, 'Fashion', 5)

foebe.rate_hw(rachel, 'Cooking', 9)
foebe.rate_hw(rachel, 'Cooking', 6)
foebe.rate_hw(rachel, 'Cooking', 5)
foebe.rate_hw(monica, 'Cooking', 2)
foebe.rate_hw(monica, 'Cooking', 6)
foebe.rate_hw(monica, 'Cooking', 3)

rachel.rate_lect(ross, 'Cooking', 4)
rachel.rate_lect(ross, 'Cooking', 5)
rachel.rate_lect(ross, 'Cooking', 8)
monica.rate_lect(ross, 'Cooking', 3)
monica.rate_lect(ross, 'Cooking', 1)
monica.rate_lect(ross, 'Cooking', 2)

rachel.rate_lect(chandler, 'Fashion', 3)
rachel.rate_lect(chandler, 'Fashion', 7)
rachel.rate_lect(chandler, 'Fashion', 6)

monica.rate_lect(chandler, 'Fashion', 7)

print(f'')
print(rachel)
print(f'')
print(monica)
print(f'')
print(chandler)
print(f'')
print(ross)
print(f'')
print(joey)
print(f'')
print(foebe)

print(f'')
print("Средний балл за домашние задания по курсу:", average_grade_hw(students_list, 'Cooking'))
print("Средний балл за лекции по курсу:", average_grade_lecture(lecturers_list, 'Fashion'))

print(f'')
print(ross < chandler)
print(f'')
print(monica > rachel)


