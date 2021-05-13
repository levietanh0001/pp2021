# Creating a class of student with the constructors for StudentMarkManagementSystem Student Mark Management.

class InitStudent:
    def __init__(self, StudentMarkManagementSystem, student_id, name, date_of_birth):
        self.stdID = student_id
        self.stdName = name
        self.dob = date_of_birth
        StudentMarkManagementSystem.students_info_list.append(self)
        StudentMarkManagementSystem.students_id_list.append(self.stdID)

    def getStudentID(self):
        return self.stdID

    def getName(self):
        return self.stdName

    def getDOB(self):
        return self.dob

# Creating a class of Course with the constructors for StudentMarkManagementSystem Student Mark Management.
class InitCourse:
    def __init__(self, StudentMarkManagementSystem, course_id, name):
        self.courseID = course_id
        self.stdName = name
        StudentMarkManagementSystem.courses.append(self)
        StudentMarkManagementSystem.courses_id.append(self.courseID)

    def getCourseID(self):
        return self.courseID

    def getName(self):
        return self.stdName

# Creating a class of Marks with the constructors for StudentMarkManagementSystem Student Mark Management.
class InitMark:
    def __init__(self, StudentMarkManagementSystem, student_id, course_id, student_mark):
        self.stdID = student_id
        self.courseID = course_id
        self.stdMark = student_mark
        StudentMarkManagementSystem.marks_list.append(self)

    def getStudentID(self):
        return self.stdID

    def getCourseID(self):
        return self.courseID

    def getStudentMark(self):
        return self.stdMark

class StudentMarkManagementSystem:

    students_id_list = []
    students_info_list = []
    courses_list = []
    courses_id = []
    marks_list = []

    num_of_students = None
    num_of_courses = None

    def getStudents(self):
        num_of_students = int(input("Enter the number of students: "))
        self.num_of_students = num_of_students

    def getCourses(self):
        num_of_courses = int(input("Enter the number of courses: "))
        self.num_of_courses = num_of_courses

    def getStudentInfo(self):
        while True:
            student_id = input("Enter student ID: ")
            if student_id is None:
                print("Student ID cannot be empty")
            else:
                break
        if student_id in self.students_id_list:
            print("Student ID already exists")
            exit()
        else:
            while True:
                name = input("Enter student name: ")
                if name is None:
                    print("Student name cannot be empty")
                else:
                    break
            while True:
                date_of_birth = input("Enter student date of birth: ")
                if date_of_birth is None:
                    print("Student date of birth cannot be empty")
                else:
                    break
            print(f"Added student {name}!")
            InitStudent(self, student_id, name, date_of_birth)

    def getCourseInfo(self):
        while True:
            course_id = input("Enter course ID: ")
            if course_id is None:
                print("Course ID cannot be empty")
            else:
                break
        if course_id in self.courses_id:
            print("Course ID already exists")
            exit()
        else:
            while True:
                name = input("Enter course name: ")
                if name is None:
                    print("Course name cannot be empty")
                else:
                    break
            print(f"Successfully added course: {name}")
            InitCourse(self, course_id, name)

    def getCourseMarks(self, course_id):
        for student in self.students_info_list:
            student_id = student.getStudentID()

            value = float(input(f"Enter marks for {student.getName()}: "))
            InitMark(self, student_id, course_id, value)

    def getMark(self):
        while True:
            course_id = input("Enter the course ID you want to input mark: ")
            if course_id in self.courses_id:
                if len(self.marks_list) > 0:
                    Marked = False
                    for mark in self.marks_list:
                        if mark.getCourseID() == course_id:
                            print("You have already input marks for this course")
                            Marked = True
                            break
                    if not Marked:
                        self.getCourseMarks(course_id)
                else:
                    self.getCourseMarks(course_id)
                break
            elif course_id is None:
                print("Course ID cannot be empty")
            else:
                print("No course with that ID")
                return -1

    def printCourses(self):
        print("Printing all courses: ")
        for course in self.courses_list:
            print("%s %s " % (course.getCourseID(), course.getName()))

    def printStudents(self):
        print("Printing all Students in class:")
        for student in self.students_info_list:
            print("%s %s %s" % (student.getStudentID(), student.getName(), student.getDOB()))

    def printCourseMarks(self, course_id):
        for mark in self.marks_list:
            if mark.getCourseID() == course_id:
                student_id = mark.getStudentID()
                for student in self.students_info_list:
                    if student.getStudentID() == student_id:
                        print(f"%s %s %s" % (student.getStudentID(), student.getName(), mark.getStudentMark()))

    def printMarks(self):
        while True:
            course_id = input("Enter the course ID you want to print marks: ")
            if course_id is None:
                print("Course ID cannot be empty")
            else:
                break
        if course_id in self.courses_id:
            self.printCourseMarks(course_id)
        else:
            print("No course with that ID")
            return -1

    # Start the Student Mark Manager
    def StartSMMS(self):
        print("Your choice: ")
        print("1 = Input number of student and their information")
        print("2 = Input number of courses and their information")
        print("3 = Exit")
        print()
        myChoice = int(input("Enter the corresponding number: "))
        while True:
            if myChoice == 1:
                self.getStudents()
                for i in range(self.num_of_students):
                    print(f"Student #{i + 1}:")
                    self.getStudentInfo()
                while len(self.courses_list) == 0:
                    print("1 = Input number of courses and their information")
                    print("2 = Exit")
                    myChoice2 = int(
                        input("Enter your choice: "))
                    if myChoice2 == 1:
                        self.getCourses()
                        for i in range(self.num_of_courses):
                            print(f"Course #{i + 1}:")
                            self.getCourseInfo()
                        break
                    elif myChoice2 == 2:
                        exit()
                    else:
                        print("Invalid choice")
                break
            elif myChoice == 2:
                self.getCourses()
                for i in range(self.num_of_courses):
                    print(f"Course #{i + 1}:")
                    self.getCourseInfo()
                while len(self.students_info_list) == 0:
                    print("\n1 = Input number of students and their information")
                    print("2 = Exit\n")
                    myChoice2 = int(
                        input("Enter your choice: "))
                    if myChoice2 == 1:
                        self.getStudents()
                        for i in range(self.num_of_students):
                            print(f"Student #{i + 1}:")
                            self.getStudentInfo()
                        break
                    elif myChoice2 == 2:

                        exit()
                    else:
                        print("Invalid choice")
                        break
                break
            elif myChoice == 3:
                exit()
            else:
                print("Invalid choice")
                exit()
        while len(self.marks_list) < len(self.students_info_list) * len(self.courses):
            print("1 = Input mark for a course")
            print("2 = Print students")
            print("3 = Print courses")
            print("4 = Exit")
            myChoice3 = int(input("Enter your choice: "))
            if myChoice3 == 1:
                self.getMark()
            elif myChoice3 == 2:
                self.printStudents()
            elif myChoice3 == 3:
                self.printCourses()
            elif myChoice3 == 4:
                exit()
            else:
                print("Invalid choice!")
        while True:
            print("1 = Print students")
            print("2 = Print courses")
            print("3 = Print marks of a course")
            print("4 = Exit")
            print()
            myChoice3 = int(input("Enter your choice: "))
            if myChoice3 == 1:
                self.printStudents()
            elif myChoice3 == 2:
                self.printCourses()
            elif myChoice3 == 3:
                self.printMarks()
            elif myChoice3 == 4:
                exit()
            else:
                print("Invalid choice!")

systemObj = StudentMarkManagementSystem()
systemObj.StartSMMS()
