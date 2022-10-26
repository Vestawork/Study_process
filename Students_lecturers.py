class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}




    def rate_lec(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.finished_courses or course in self.courses_in_progress:
            if course in lecture.rates_lecture.keys():
                lecture.rates_lecture[course] += [grade]
            else:
                lecture.rates_lecture.update({course:[grade]})
                #lecture.rates_lecture[course] = grade

        else:
            return 'Ошибка'

    def av_gr (self):
        AG = 0
        if len(self.grades.values()) != 0:
            sum = 0
            i = 0
            for el in self.grades.values():
                for ell in el:
                    sum += ell
                    i += 1
            AG = sum/i
        return AG


    def __str__(self):

        def not_zero(a):
            if a == 0:
                a = 1
            return (a)

        return (f'Имя:{self.name}\nФамилия:{self.surname}\n'+
                f'Средняя оценка за домашние задания: {sum(self.grades.values())/not_zero(len(self.grades.values()))}\n' +
                f'Курсы в процессе изучения: {self.courses_in_progress}\n' +
                f'Завершенные курсы: {self.finished_courses}') #+''.join(f'{element for element in self.finished_courses}'))

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return

        return self.av_gr() < other.av_gr()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return

        return self.av_gr() > other.av_gr()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.rates_lecture = {}

    def av_gr(self):
        AG = 0

    def av_gr(self):
        AG = 0
        if len(self.rates_lecture.values()) != 0:
            sum = 0
            i = 0
            for el in self.rates_lecture.values():
                for ell in el:
                    sum += ell
                    i += 1
            AG = sum / i
        return AG





    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.av_gr() < other.av_gr()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.av_gr() > other.av_gr()

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n' +
                f'{sum(rates)/len(self.rates_lecture[grade]) for rates in self.rates_lecture}')




class Reviewer(Mentor):
    # def __init__(self, name, surname):
    #     super().__init__(name, surname)

    def __str__(self):
        return(f'Имя: {self.name}\nФамилия: {self.surname}')



    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def av_hw_rate (students, course):
    sum_grades = 0
    sum_st = 0
    for id, st in enumerate(students):
        if isinstance(st, Student):
            for cour, gr in st.grades.items():
                if cour == course:
                    for grade in gr:
                        sum_grades += grade

        sum_st = id+1
        AG = sum_grades/sum_st
    return AG

def av_lec_rate (lecturers, course):
    sum_grades = 0
    sum_lec = 0
    for id, lec in enumerate(lecturers):
        if isinstance(lec, Lecturer):
            for cour, rate in lec.grades.items():
                if cour == course:
                    for grade in rate:
                        sum_grades += grade

        sum_lec = id+1
        AG = sum_grades/sum_lec
    return AG






# Создать по 2 экземпляра каждого класса и наполнить значениями

some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['C++']
some_student.courses_in_progress += ['Cooking']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Cooking']

some_reviewer = Reviewer('Someer', 'Buddyer')
some_reviewer.rate_hw (some_student, 'Python', 10)
some_reviewer.rate_hw (some_student, 'Cooking', 8)

some_student1 = Student('Vasya', 'Fokin', 'male')
some_student1.courses_in_progress += ['C++']
some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['Cooking']

some_lecturer1 = Lecturer('Sanya', 'Budkin')
some_lecturer1.courses_attached += ['C++']

some_reviewer1 = Reviewer('Samir', 'Buddylaev')
some_reviewer1.rate_hw (some_student1, 'C++', 10)
some_reviewer1.rate_hw (some_student1, 'Cooking', 6)

some_student.rate_lec(some_lecturer, 'Python', 10)
some_student1.rate_lec(some_lecturer1, 'C++', 10)
some_student.rate_lec(some_lecturer, 'Cooking', 1)
some_student1.rate_lec(some_lecturer, 'Cooking', 3)
some_student.rate_lec(some_lecturer1, 'C++', 8)

#вызываем созданные методы:
print(some_reviewer)
print(some_lecturer)
print(some_student)
print (some_student1)

print(some_student.grades)

#сравниваем лекторов и студентов по средней оценке

print (some_student > some_lecturer)
print (some_lecturer > some_student)

if some_student < some_student1:
    print (f'{some_student.name} {some_student.surname} хуже учится, чем {some_student1.name} {some_student1.surname}')


print (some_student > some_student1)

print (some_lecturer>some_lecturer1)
print (some_lecturer<some_lecturer1)
s = input ('Введите название курса для расчета средней оценки студентов')
print (str(f'Средняя оцнка по {s} {av_hw_rate([some_student, some_student1], s)}'))

av_lec_rate

s1 = input ('Введите название курса для расчета средней оценки лекторов')
print (str(f'Средняя оцнка по {s1} {av_lec_rate([some_lecturer, some_lecturer1], s1)}'))
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)



