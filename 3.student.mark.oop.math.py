import curses
import math
import numpy as np

screen = curses.initscr()

def PrintError(error):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    screen.addstr("\nError: " + error, curses.color_pair(1) | curses.A_BOLD)
    screen.refresh()
    curses.napms(1000)
    screen.clear()
    screen.refresh()

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

    def setGPA(self, gpa):
        self.gpa = gpa

    def getGPA(self):
        return self.gpa

class InitCourse:
    def __init__(self, StudentMarkManagementSystem, course_id, name, credit):
        self.courseID = course_id
        self.stdName = name
        self.credit = credit
        StudentMarkManagementSystem.courses_list.append(self)
        StudentMarkManagementSystem.courses_id_list.append(self.courseID)

    def getCourseID(self):
        return self.courseID

    def getName(self):
        return self.stdName

    def getCredit(self):
        return  self.credit

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
    courses_id_list = []
    marks_list = []

    num_of_students = None
    num_of_courses = None

    def getNumOfStudents(self):
        while True:
            screen.addstr("\nEnter number of students: ")
            screen.refresh()
            num_of_students = int(screen.getstr().decode())
            if num_of_students < 0:
                PrintError("\nNumber of students cannot be negative")
            else:
                break
        self.num_of_students = num_of_students

    def getNumOfCourses(self):
        while True:
            screen.addstr("\nEnter number of courses: ")
            screen.refresh()
            num_of_courses = int(screen.getstr().decode())
            if num_of_courses < 0:
                PrintError("\nNumber of courses cannot be negative")
            else:
                break
        self.num_of_courses = num_of_courses

    def getStudentInfo(self):
        while True:
            screen.addstr("\nEnter student ID: ")
            screen.refresh()
            student_id = screen.getstr().decode()
            if student_id is None:
                PrintError("Student ID cannot be null!")
            else:
                break
        if student_id in self.students_id_list:
            PrintError("Student ID already exists!")
            exit()
        else:
            while True:
                screen.addstr("Enter student name: ")
                screen.refresh()
                name = screen.getstr().decode()
                if name is None:
                    PrintError("Student name cannot be null!")
                else:
                    break
            while True:
                screen.addstr("Enter student dob/ date of birth: ")
                screen.refresh()
                dob = screen.getstr().decode()
                if dob is None:
                    PrintError("Student dob/ date of birth cannot be null!")
                else:
                    break


            screen.addstr(f"Added student {name}!")
            screen.refresh()
            curses.napms(500)
            InitStudent(self, student_id, name, dob)

    def getCourseInfo(self):
        while True:
            screen.addstr("\nEnter course ID: ")
            screen.refresh()
            course_id = screen.getstr().decode()
            if course_id is None:
                PrintError("Course ID cannot be null!")
            else:
                break
        if course_id in self.courses_id_list:
            PrintError("Course ID already exists!")
            exit()
        else:
            while True:
                screen.addstr("Enter course name: ")
                screen.refresh()
                name = screen.getstr().decode()
                if name is None:
                    PrintError("Course name cannot be null!")
                else:
                    break
            while True:
                screen.addstr("Enter course credits: ")
                screen.refresh()
                credit = int(screen.getstr().decode())
                if credit < 0:
                    PrintError("Course credit can not be negative!")
                elif credit is None:
                    PrintError("Course credit cannot be null!")
                else:
                    break

            screen.addstr(f"Added course {name}!")
            screen.refresh()
            curses.napms(500)

            InitCourse(self, course_id, name, credit)

    def getCourseMark(self, course_id):
        for student in self.students_info_list:
            student_id = student.getStudentID()
            studentName = student.getName()
            screen.addstr(f"Enter marks for {studentName}: ")
            screen.refresh()
            value = float(screen.getstr().decode())
            value = math.floor(value * 10) / 10.0
            InitMark(self, student_id, course_id, value)

    def getMark(self):
        while True:
            screen.addstr("Enter the course ID for which you want to input marks: ")
            screen.refresh()
            course_id = screen.getstr().decode()
            screen.clear()
            screen.refresh()
            if course_id in self.courses_id_list:
                if len(self.marks_list) > 0:
                    Marked = False
                    for mark in self.marks_list:
                        if mark.getCourseID() == course_id:
                            PrintError("You have already input marks for this course!")
                            Marked = True
                            break
                    if not Marked:
                        self.getCourseMark(course_id)
                else:
                    self.getCourseMark(course_id)
                break
            elif course_id is None:
                PrintError("Course ID cannot be null!")
            else:
                PrintError("No course with such ID!")
                return -1

    def printCourses(self):
        screen.addstr("Printing all courses: ")
        screen.refresh()
        for course in self.courses_list:
            screen.addstr("%s %s" % (course.getCourseID(), course.getName()))
            screen.refresh()

    def printStudents(self):
        screen.addstr("Printing all Students in class:")
        screen.refresh()
        for student in self.students_info_list:
            screen.addstr("%s %s %s" % (student.getStudentID(), student.getName(), student.getDOB()))
            screen.refresh()

    def printCourseMarks(self, course_id):
        for mark in self.marks_list:
            if mark.getCourseID() == course_id:
                student_id = mark.getStudentID()
                for student in self.students_info_list:
                    if student.getStudentID() == student_id:
                        screen.addstr(f"%s %s %s" % (student.getStudentID(), student.getName(), mark.getStudentMark()))
                        screen.refresh()

    def printMarks(self):
        while True:
            screen.addstr("- Enter the course ID for which you want to list marks: ")
            screen.refresh()
            course_id = screen.getstr().decode()
            if course_id is None:
                PrintError("Course ID cannot be null")
            else:
                break
        if course_id in self.courses_id_list:

            self.printCourseMarks(course_id)
        else:
            PrintError("There exist no course with that ID!")
            return -1

    def computeStudentGPA(self, sid):
        marks_arr = np.array([])
        course_credits = np.array([])
        for mark in self.marks_list:
            if mark.getStudentID() == sid:
                for course in self.courses_list:
                    if course.getCourseID() == mark.getCourseID():
                        marks_arr = np.append(marks_arr, mark.getStudentMark())
                        course_credits = np.append(course_credits, course.getCredit())
        gpa = np.dot(marks_arr, course_credits) / np.sum(course_credits)
        rounded_gpa = math.floor(gpa * 10) / 10.0

        for student in self.students_info_list:
            if student.getStudentID() == sid:
                student.setGPA(rounded_gpa)

    def computeGPA(self):
        while True:
            screen.addstr("Enter student ID to compute the student GPA: ")
            screen.refresh()
            sid = screen.getstr().decode()
            if len(sid) == 0 or sid is None:
                PrintError("Student ID cannot be null!")
            elif sid not in self.students_id_list:
                PrintError("Student ID does not exist!")
            else:
                break
        for student in self.students_info_list:
            if student.getStudentID() == sid:
                self.computeStudentGPA(sid)
                screen.addstr("Student %s has GPA = %.1f" % (student.getName(), student.getGPA()))
                screen.refresh()
                break

    def printSortedList(self):

        new_student_list = []
        for student in self.students_info_list:
            self.computeStudentGPA(student.getStudentID())
            new_student = (student.getStudentID(), student.getName(), student.getGPA())
            new_student_list.append(new_student)

        dtype = [('sid', 'S10'), ('name', 'S30'), ('gpa', float)]
        numpy_student_list = np.array(new_student_list, dtype=dtype)
        sorted_student_list = np.sort(numpy_student_list, order='gpa')[::-1]

        new_sorted_student_list = []
        for student in sorted_student_list:
            decoded_student = (student[0].decode(), student[1].decode(), student[2])
            new_sorted_student_list.append(decoded_student)
        for student in new_sorted_student_list:
            screen.addstr("ID = %s, %s, GPA = %s\n" % (student[0], student[1], student[2]))
            screen.refresh()

    def startSMMS(self):
        curses.start_color()
        num_rows, num_cols = screen.getmaxyx()

        def printMid(message):
            mid_row = int(num_rows / 2)
            mid_col = int(num_cols / 3)
            screen.addstr(mid_row, mid_col, message)
            screen.refresh()

        screen.refresh()
        printMid("Loading Student Mark Management System")
        for i in range(3):
            screen.addstr(" > ")
            screen.refresh()
            curses.napms(300)
        screen.clear()
        screen.refresh()
        printMid("Initilaizing STUDENT MARK MANAGEMENT SYSTEM")
        for i in range(3):
            screen.addstr(" . ")
            screen.refresh()
            curses.napms(300)
        screen.clear()
        screen.refresh()

        screen.addstr("\n1 = Enter students' details")
        screen.addstr("\n2 = Enter courses' details")
        screen.addstr("\n3 = Exit")
        screen.addstr("\nEnter your choice: ")
        screen.refresh()
        myChoice = int(screen.getstr().decode())
        while True:
            if myChoice == 1:
                screen.clear()
                screen.refresh()
                self.getNumOfStudents()
                screen.clear()
                screen.refresh()
                for i in range(self.num_of_students):
                    screen.addstr(f"Student #{i + 1}:\n")
                    screen.refresh()
                    self.getStudentInfo()
                    screen.clear()
                    screen.refresh()
                while len(self.courses_list) == 0:
                    screen.addstr("\n1 =  Enter courses' details")
                    screen.addstr("\n2 = Exit")
                    screen.refresh()
                    screen.addstr("\nEnter your choice: ")
                    screen.refresh()
                    myChoice2 = int(screen.getstr().decode())
                    if myChoice2 == 1:
                        screen.clear()
                        screen.refresh()
                        self.getNumOfCourses()
                        screen.clear()
                        screen.refresh()
                        for i in range(self.num_of_courses):
                            screen.addstr(f"Course #{i + 1}:")
                            screen.refresh()
                            self.getCourseInfo()
                            screen.clear()
                            screen.refresh()
                        break
                    elif myChoice2 == 2:
                        screen.clear()
                        curses.endwin()
                        exit()
                    else:
                        PrintError("Invalid choice!")
                break
            elif myChoice == 2:
                screen.clear()
                screen.refresh()
                self.getNumOfCourses()
                screen.clear()
                screen.refresh()
                for i in range(self.num_of_courses):
                    screen.addstr(f"Course #{i + 1}:")
                    screen.refresh()
                    self.getCourseInfo()
                    screen.clear()
                    screen.refresh()
                while len(self.students_info_list) == 0:
                    screen.addstr("1 = Enter students' details")
                    screen.addstr("\n2 = Exit\n")
                    screen.refresh()
                    screen.addstr("Enter your choice: ")
                    screen.refresh()
                    myChoice2 = int(screen.getstr().decode())
                    if myChoice2 == 1:
                        screen.clear()
                        screen.refresh()
                        self.getNumOfStudents()
                        screen.clear()
                        screen.refresh()
                        for i in range(self.num_of_students):
                            screen.addstr(f"Student #{i + 1}:")
                            screen.refresh()
                            self.getStudentInfo()
                            screen.clear()
                            screen.refresh()
                        break
                    elif myChoice2 == 2:
                        screen.clear()
                        curses.endwin()
                        exit()
                    else:
                        PrintError("Invalid choice!")
                        break
                break
            elif myChoice == 3:
                screen.clear()
                curses.endwin()
                exit()
            else:
                PrintError("Invalid choice!")
                curses.endwin()
                exit()
        while len(self.marks_list) < len(self.students_info_list) * len(self.courses_list):
            screen.clear()
            screen.refresh()
            screen.addstr("1 = Enter mark for a course")
            screen.addstr("\n2 = Print students")
            screen.addstr("\n3 = Print courses")
            screen.addstr("\n4 = Exit\n")
            screen.addstr("\nEnter your choice: ")
            screen.refresh()
            myChoice3 = int(screen.getstr().decode())
            screen.clear()
            screen.refresh()
            if myChoice3 == 1:
                self.getMark()
            elif myChoice3 == 2:

                self.printStudents()
                curses.napms(self.num_of_students * 1000)

            elif myChoice3 == 3:

                self.printCourses()
                curses.napms(self.num_of_courses * 1000)

            elif myChoice3 == 4:
                screen.clear()
                curses.endwin()
                exit()
            else:
                PrintError("Invalid choice!")
        while True:
            screen.clear()
            screen.refresh()
            screen.addstr("1 = Print all students")
            screen.addstr("\n2 = Print all courses")
            screen.addstr("\n3 = Print marks of a course")
            screen.addstr("\n4 = Compute GPA for a student")
            screen.addstr("\n5 = Print a sorted student list by GPA in descending order")
            screen.addstr("\n6 = Exit")

            screen.addstr("\nEnter your choice: ")
            screen.refresh()
            myChoice4 = int(screen.getstr().decode())
            screen.clear()
            screen.refresh()
            if myChoice4 == 1:

                self.printStudents()
                curses.napms(self.num_of_students * 1500)

            elif myChoice4 == 2:

                self.printCourses()
                curses.napms(self.num_of_courses * 1500)

            elif myChoice4 == 3:
                self.printMarks()
                curses.napms(self.num_of_students * 1500)

            elif myChoice4 == 4:
                self.computeGPA()
                curses.napms(1000)

            elif myChoice4 == 5:
                self.printSortedList()
                curses.napms(self.num_of_students * 1500)

            elif myChoice4 == 6:
                screen.clear()
                printMid("Closing application!")
                curses.endwin()
                exit()
            else:
                PrintError("Invalid choice!")

    # main
if __name__ == '__main__':
    screen = curses.initscr()
    systemObj = StudentMarkManagementSystem()
    systemObj.startSMMS()