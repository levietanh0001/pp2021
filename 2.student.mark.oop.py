# Creating a class of student with the constructors for SMM Student Mark Management.
class Student:
    def __init__(self, SMM, s_id, name, dob):
        self.__s_id = s_id
        self.__name = name
        self.__dob = dob
        SMM.students_info.append(self)
        SMM.students_id.append(self.__s_id)

    def get_s_id(self):
        return self.__s_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

# Creating a class of Course with the constructors for SMM Student Mark Management.
class Course:
    def __init__(self, SMM, c_id, name):
        self.__c_id = c_id
        self.__name = name
        SMM.courses.append(self)
        SMM.courses_id.append(self.__c_id)

    def get_c_id(self):
        return self.__c_id

    def get_name(self):
        return self.__name

# Creating a class of Marks with the constructors for SMM Student Mark Management.
class Marks:
    def __init__(self, SMM, s_id, c_id, val):
        self.__s_id = s_id
        self.__c_id = c_id
        self.__val = val
        SMM.marks.append(self)

    def get_s_id(self):
        return self.__s_id

    def get_c_id(self):
        return self.__c_id

    def get_value(self):
        return self.__val

class SMM:

    students_id = []
    students_info = []
    courses = []
    courses_id = []
    marks = []

    no_students = None
    no_courses = None

    def input_no_students(self):
        no_students = int(input("-> Enter the number of students: "))
        self.no_students = no_students

    def input_no_courses(self):
        no_courses = int(input("-> Enter the number of courses: "))
        self.no_courses = no_courses

    def input_student_info(self):
        while True:
            s_id = input("-> Enter student ID: ")
            if s_id is None:
                print("***Error: Student ID cannot be empty***")
            else:
                break
        if s_id in self.students_id:
            print("***Error: Student ID existed***")
            exit()
        else:
            while True:
                name = input("-> Enter student name: ")
                if name is None:
                    print("***Error: Student name cannot be empty***")
                else:
                    break
            while True:
                dob = input("-> Enter student date of birth: ")
                if dob is None:
                    print("***Error: Student date of birth cannot be empty***")
                else:
                    break
            print(f"Successfully added student: {name}")
            Student(self, s_id, name, dob)

    def input_course_info(self):
        while True:
            c_id = input("-> Enter course ID: ")
            if c_id is None:
                print("***Error: Course ID cannot be empty***")
            else:
                break
        if c_id in self.courses_id:
            print("***Error: Course ID existed***")
            exit()
        else:
            while True:
                name = input("-> Enter course name: ")
                if name is None:
                    print("***Error: Course name cannot be empty***")
                else:
                    break
            print(f"Successfully added course: {name}")
            Course(self, c_id, name)

    def input_course_mark(self, c_id):
        for student in self.students_info:
            s_id = student.get_s_id()

            value = float(input(f"-> Enter marks for {student.get_name()}: "))
            Marks(self, s_id, c_id, value)

    def input_mark(self):
        while True:
            c_id = input("-> Enter the course ID you want to input mark: ")
            if c_id in self.courses_id:
                if len(self.marks) > 0:
                    Marked = False
                    for mark in self.marks:
                        if mark.get_c_id() == c_id:
                            print("***Error: You have already input marks for this course***")
                            Marked = True
                            break
                    if not Marked:
                        self.input_course_mark(c_id)
                else:
                    self.input_course_mark(c_id)
                break
            elif c_id is None:
                print("***Error: Course ID cannot be empty***")
            else:
                print("***Error: There exists no course with that ID***")
                return -1

    def list_courses(self):
        print("Showing all courses: ")
        for course in self.courses:
            print("\t\t[%s]   %-20s" % (course.get_c_id(), course.get_name()))

    def list_students(self):
        print("Showing all Students in class:")
        for student in self.students_info:
            print("\t\t[%s]    %-20s%s" % (student.get_s_id(), student.get_name(), student.get_dob()))

    def list_course_marks(self, c_id):
        for mark in self.marks:
            if mark.get_c_id() == c_id:
                s_id = mark.get_s_id()
                for student in self.students_info:
                    if student.get_s_id() == s_id:
                        print(f"\t\t[%s]    %-20s%s" % (student.get_s_id(), student.get_name(), mark.get_value()))

    def list_marks(self):
        while True:
            c_id = input("-> Enter the course ID you want to list marks: ")
            if c_id is None:
                print("***Error: Course ID cannot be empty***")
            else:
                break
        if c_id in self.courses_id:
            self.list_course_marks(c_id)
        else:
            print("***Error: There exist no course with that ID***")
            return -1

    # Start the Student Mark Manager
    def start_SMM(self):
        print("Loading Student Mark manager...")
        print("Choose your option: ")
        print("[1] Input number of student and their information")
        print("[2] Input number of courses and their information")
        print("[3] Cancel")
        print()
        choice1 = int(input("Enter the corresponding number: "))
        while True:
            if choice1 == 1:
                self.input_no_students()
                for i in range(self.no_students):
                    print(f"Student #{i + 1}:")
                    self.input_student_info()
                while len(self.courses) == 0:
                    print("[1] Input number of courses and their information")
                    print("[2] Cancel")
                    choice2 = int(
                        input("Select your option by entering the digit: "))
                    if choice2 == 1:
                        self.input_no_courses()
                        for i in range(self.no_courses):
                            print(f"Course #{i + 1}:")
                            self.input_course_info()
                        break
                    elif choice2 == 2:
                        print("Exiting!")
                        exit()
                    else:
                        print("***Error: Invalid choice***")
                break
            elif choice1 == 2:
                self.input_no_courses()
                for i in range(self.no_courses):
                    print(f"Course #{i + 1}:")
                    self.input_course_info()
                while len(self.students_info) == 0:
                    print("\n[1] Input number of students and their information")
                    print("[2] Cancel\n")
                    choice2 = int(
                        input("Select your option by entering the digit: "))
                    if choice2 == 1:
                        self.input_no_students()
                        for i in range(self.no_students):
                            print(f"Student #{i + 1}:")
                            self.input_student_info()
                        break
                    elif choice2 == 2:
                        print("Exiting!")
                        exit()
                    else:
                        print("***Error: Invalid choice***")
                        break
                break
            elif choice1 == 3:
                print("Exiting!")
                exit()
            else:
                print("***Error: Invalid choice***")
                exit()
        while len(self.marks) < len(self.students_info) * len(self.courses):
            print("[1] Input mark for a course")
            print("[2] List students")
            print("[3] List courses")
            print("[4] Cancel")
            choice3 = int(input("Select your option by entering the digit: "))
            if choice3 == 1:
                self.input_mark()
            elif choice3 == 2:
                self.list_students()
            elif choice3 == 3:
                self.list_courses()
            elif choice3 == 4:
                print("Exiting!")
                exit()
            else:
                print("***Error: invalid choice***")
        while True:
            print("[1] List students")
            print("[2] List courses")
            print("[3] Show marks of a course")
            print("[4] Cancel")
            print()
            choice3 = int(input("Select your option by entering the digit: "))
            if choice3 == 1:
                self.list_students()
            elif choice3 == 2:
                self.list_courses()
            elif choice3 == 3:
                self.list_marks()
            elif choice3 == 4:
                print("Exiting!")
                exit()
            else:
                print("***Error: invalid choice***")


if __name__ == '__main__':
    e = SMM()
    e.start_SMM()
