
import math
import numpy as np
import curses

# Method to display error
def print_error(error):
    screen.addstr("*** Error: " + error + " ***", curses.color_pair(2) |
                  curses.A_BOLD | curses.A_UNDERLINE | curses.A_BLINK)
    screen.refresh()
    curses.napms(2000)
    screen.clear()
    screen.refresh()

# Creating a class of student with the constructors for SMM Student Mark Management.
class Student:
    def __init__(self, SMM, s_id, name, dob, gpa=0):
        self.__s_id = s_id
        self.__name = name
        self.__dob = dob
        self.__gpa = gpa
        SMM.students_info.append(self)
        SMM.students_id.append(self.__s_id)

    def get_s_id(self):
        return self.__s_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    # Creating getter and setter for GPA

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

# Creating a class of Course with the constructors for SMM Student Mark Management.
class Course:
    def __init__(self, SMM, c_id, name, credit):
        self.__c_id = c_id
        self.__name = name
        self.__credit = credit
        SMM.courses.append(self)
        SMM.courses_id.append(self.__c_id)

    def get_c_id(self):
        return self.__c_id

    def get_name(self):
        return self.__name

    def get_credit(self):
        return self.__credit

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
        while True:
            screen.addstr("\n-> Enter number of students: ")
            screen.refresh()
            no_students = int(screen.getstr().decode())
            if no_students < 0:
                print_error("number of students cannot be negative")
            else:
                break
        self.no_students = no_students

    def input_no_courses(self):
        while True:
            screen.addstr("\n-> Enter number of courses: ")
            screen.refresh()
            no_courses = int(screen.getstr().decode())
            if no_courses < 0:
                print_error("number of courses cannot be negative")
            else:
                break
        self.no_courses = no_courses

    def input_student_info(self):
        while True:
            screen.addstr("\n-> Enter student ID: ")
            screen.refresh()
            s_id = screen.getstr().decode()
            if s_id is None:
                print_error("Student ID cannot be empty")
            else:
                break
        if s_id in self.students_id:
            print_error("Student ID already exists")
            exit()
        else:
            while True:
                screen.addstr("-> Enter student name: ")
                screen.refresh()
                name = screen.getstr().decode()
                if name is None:
                    print_error("Student name cannot be empty")
                else:
                    break
            while True:
                screen.addstr("-> Enter student date of birth: ")
                screen.refresh()
                dob = screen.getstr().decode()
                if dob is None:
                    print_error("Student date of birth cannot be empty")
                else:
                    break

            curses.curs_set(0)
            screen.addstr(f"Successfully added student: {name}")
            screen.refresh()
            curses.napms(1000)
            curses.curs_set(1)
            Student(self, s_id, name, dob)

    def input_course_info(self):
        while True:
            screen.addstr("\n-> Enter course ID: ")
            screen.refresh()
            c_id = screen.getstr().decode()
            if c_id is None:
                print_error("Course ID cannot be empty")
            else:
                break
        if c_id in self.courses_id:
            print_error("Course ID already exists")
            exit()
        else:
            while True:
                screen.addstr("-> Enter course name: ")
                screen.refresh()
                name = screen.getstr().decode()
                if name is None:
                    print_error("Course name cannot be empty")
                else:
                    break
            while True:
                screen.addstr("-> Enter course credits: ")
                screen.refresh()
                credit = int(screen.getstr().decode())
                if credit < 0:
                    print_error("Course credit must be positive")
                elif credit is None:
                    print_error("Course credit cannot be None")
                else:
                    break
            curses.curs_set(0)
            screen.addstr(f"Successfully added course: {name}")
            screen.refresh()
            curses.napms(1000)
            curses.curs_set(1)
            Course(self, c_id, name, credit)

    def input_course_mark(self, c_id):
        for student in self.students_info:
            s_id = student.get_s_id()

            screen.addstr(f"-> Enter marks for {student.get_name()}: ")
            screen.refresh()
            value = float(screen.getstr().decode())
            value = math.floor(value * 10) / 10.0

            Marks(self, s_id, c_id, value)

    def input_mark(self):
        while True:
            screen.addstr("-> Enter the course ID for which you want to input marks: ")
            screen.refresh()
            c_id = screen.getstr().decode()
            screen.clear()
            screen.refresh()
            if c_id in self.courses_id:
                if len(self.marks) > 0:
                    Marked = False
                    for mark in self.marks:
                        if mark.get_c_id() == c_id:
                            print_error("You have already input marks for this course")
                            Marked = True
                            break
                    if not Marked:
                        self.input_course_mark(c_id)
                else:
                    self.input_course_mark(c_id)
                break
            elif c_id is None:
                print_error("Course ID cannot be empty")
            else:
                print_error("There exists no course with that ID")
                return -1

    def list_courses(self):

        screen.addstr("Showing all courses: ")
        screen.refresh()
        for course in self.courses:
            screen.addstr("\t\t[%s]   %-20s" % (course.get_c_id(), course.get_name()))
            screen.refresh()

    def list_students(self):
        screen.addstr("Showing all Students in class:")
        screen.refresh()
        for student in self.students_info:
            screen.addstr("\t\t[%s]    %-20s%s" % (student.get_s_id(), student.get_name(), student.get_dob()))
            screen.refresh()

    def list_course_marks(self, c_id):
        for mark in self.marks:
            if mark.get_c_id() == c_id:
                s_id = mark.get_s_id()
                for student in self.students_info:
                    if student.get_s_id() == s_id:
                        screen.addstr(f"\t\t[%s]    %-20s%s" % (student.get_s_id(), student.get_name(), mark.get_value()))
                        screen.refresh()

    def list_marks(self):
        while True:
            screen.addstr("- Enter the course ID for which you want to list marks: ")
            screen.refresh()
            c_id = screen.getstr().decode()
            if c_id is None:
                print_error("Course ID cannot be empty")
            else:
                break
        if c_id in self.courses_id:
            curses.curs_set(0)
            self.list_course_marks(c_id)
        else:
            print_error("There exist no course with that ID")
            return -1

    def calculate_student_gpa(self, sid):
        mark_values = np.array([])
        course_credits = np.array([])
        for mark in self.marks:
            if mark.get_sid() == sid:
                for course in self.courses:
                    if course.get_cid() == mark.get_cid():
                        mark_values = np.append(mark_values, mark.get_value())
                        course_credits = np.append(course_credits, course.get_credit())
        gpa = np.dot(mark_values, course_credits) / np.sum(course_credits)
        rounded_gpa = math.floor(gpa * 10) / 10.0
        # Add the value of attribute gpa for the student with ID specified
        for student in self.students:
            if student.get_sid() == sid:
                student.set_gpa(rounded_gpa)

    # Ask the user for the student ID whose GPA should be calculated, then invoke the calculate_student_gpa() function
    def calculate_gpa(self):
        while True:
            screen.addstr("-> Enter student ID to calculate the student GPA: ")
            screen.refresh()
            sid = screen.getstr().decode()
            if len(sid) == 0 or sid is None:
                # print("Error: Student ID cannot be empty")
                print_error("Student ID cannot be empty")
            elif sid not in self.students_id:
                # print("Error: Student does not exist")
                print_error("Student ID does not exist")
            else:
                break
        for student in self.students:
            if student.get_sid() == sid:
                self.calculate_student_gpa(sid)
                curses.curs_set(0)
                screen.addstr("\n\t\t%s's GPA:    %-20.1f" % (student.get_name(), student.get_gpa()))
                screen.refresh()
                break

    # A function to print a sorted student list by GPA descending
    def print_sorted_list(self):
        # Automatically calculate GPA for all students before printing a sorted list
        new_student_list = []
        for student in self.students:
            self.calculate_student_gpa(student.get_sid())
            new_student = (student.get_sid(), student.get_name(), student.get_gpa())
            new_student_list.append(new_student)
        # Make a copy of the student list using type numpy.array (Attributes type str will be converted to type bytes)
        dtype = [('sid', 'S10'), ('name', 'S30'), ('gpa', float)]
        np_student_list = np.array(new_student_list, dtype=dtype)
        # Sort the student list in ascending order and then reverse it
        sorted_student_list = np.sort(np_student_list, order='gpa')[::-1]
        # Make a copy of the sorted student list with attributes type bytes converted back to type str
        new_sorted_student_list = []
        for student in sorted_student_list:
            decoded_student = (student[0].decode(), student[1].decode(), student[2])
            new_sorted_student_list.append(decoded_student)
        # Print the final sorted student list
        for student in new_sorted_student_list:
            screen.addstr("\t\t[%s]    %-20sGPA: %s\n" % (student[0], student[1], student[2]))
            screen.refresh()

    # Start the Student Mark Manager
    def start_SMM(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        num_rows, num_cols = screen.getmaxyx()

        # Make a function to print a line in the center of screen
        def print_center(message):
            # Calculate center row
            middle_row = int(num_rows / 2)

            # Calculate center column, and then adjust starting position based
            # on the length of the message
            half_length_of_message = int(len(message) / 2)
            middle_column = int(num_cols / 2)
            x_position = middle_column - half_length_of_message

            # Draw the text
            if message == "--- Choose an option from the MENU ---":
                screen.addstr(middle_row, x_position, message, curses.A_BOLD)
                screen.refresh()
            else:
                screen.addstr(middle_row, x_position, message)
                screen.refresh()

        curses.curs_set(0)
        screen.refresh()
        print_center("Loading Student Mark manager")
        curses.napms(500)
        for i in range(3):
            screen.addstr(".")
            screen.refresh()
            curses.napms(500)
        screen.clear()
        screen.refresh()
        curses.napms(500)
        print_center("--- Choose an option from the MENU ---")
        screen.refresh()
        curses.napms(2000)
        screen.clear()
        screen.refresh()

        curses.curs_set(1)
        screen.addstr("\n[1] Input number of student and their information\n")
        screen.addstr("[2] Input number of courses and their information\n")
        screen.addstr("[3] Cancel\n")
        screen.addstr("Enter the corresponding number: ")
        screen.refresh()
        choice1 = int(screen.getstr().decode())
        while True:
            if choice1 == 1:
                screen.clear()
                screen.refresh()
                self.input_no_students()
                screen.clear()
                screen.refresh()
                for i in range(self.no_students):
                    screen.addstr(f"Student #{i + 1}:\n")
                    screen.refresh()
                    self.input_student_info()
                    screen.clear()
                    screen.refresh()
                while len(self.courses) == 0:
                    screen.addstr("[1] Input number of courses and courses information")
                    screen.addstr("\n[2] Cancel\n")
                    screen.refresh()
                    screen.addstr("Enter the corresponding number: ")
                    screen.refresh()
                    choice2 = int(screen.getstr().decode())
                    if choice2 == 1:
                        screen.clear()
                        screen.refresh()
                        self.input_no_courses()
                        screen.clear()
                        screen.refresh()
                        for i in range(self.no_courses):
                            screen.addstr(f"Course #{i + 1}:")
                            screen.refresh()
                            self.input_course_info()
                            screen.clear()
                            screen.refresh()
                        break
                    elif choice2 == 2:
                        screen.clear()
                        curses.curs_set(0)
                        print_center("Exiting!")
                        curses.napms(1000)
                        curses.curs_set(1)
                        curses.endwin()
                        exit()
                    else:
                        print_error("Invalid choice")
                break
            elif choice1 == 2:
                screen.clear()
                screen.refresh()
                self.input_no_courses()
                screen.clear()
                screen.refresh()
                for i in range(self.no_courses):
                    screen.addstr(f"Course #{i + 1}:")
                    screen.refresh()
                    self.input_course_info()
                    screen.clear()
                    screen.refresh()
                while len(self.students_info) == 0:
                    screen.addstr("[1] Input number of students and their information")
                    screen.addstr("\n[2] Cancel\n")
                    screen.refresh()
                    screen.addstr("Enter the corresponding number: ")
                    screen.refresh()
                    choice2 = int(screen.getstr().decode())
                    if choice2 == 1:
                        screen.clear()
                        screen.refresh()
                        self.input_no_students()
                        screen.clear()
                        screen.refresh()
                        for i in range(self.no_students):
                            screen.addstr(f"Student #{i + 1}:")
                            screen.refresh()
                            self.input_student_info()
                            screen.clear()
                            screen.refresh()
                        break
                    elif choice2 == 2:
                        screen.clear()
                        curses.curs_set(0)
                        print_center("Exiting!")
                        curses.napms(1000)
                        curses.curs_set(1)
                        curses.endwin()
                        exit()
                    else:
                        print_error("Invalid choice")
                        break
                break
            elif choice1 == 3:
                screen.clear()
                curses.curs_set(0)
                print_center("Exiting!")
                curses.napms(1000)
                curses.curs_set(1)
                curses.endwin()
                exit()
            else:
                print_error("Invalid choice")
                curses.endwin()
                exit()
        while len(self.marks) < len(self.students_info) * len(self.courses):
            screen.clear()
            screen.refresh()
            screen.addstr("[1] Input mark for a course")
            screen.addstr("\n[2] List students")
            screen.addstr("\n[3] List courses")
            screen.addstr("\n[4] Cancel\n")
            screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
            screen.refresh()
            choice3 = int(screen.getstr().decode())
            screen.clear()
            screen.refresh()
            if choice3 == 1:
                self.input_mark()
            elif choice3 == 2:
                curses.curs_set(0)
                self.list_students()
                curses.napms(self.no_students * 1000)
                curses.curs_set(1)
            elif choice3 == 3:
                curses.curs_set(0)
                self.list_courses()
                curses.napms(self.no_courses * 1000)
                curses.curs_set(1)
            elif choice3 == 4:
                screen.clear()
                curses.curs_set(0)
                print_center("Exiting!")
                curses.napms(1000)
                curses.curs_set(1)
                curses.endwin()
                exit()
            else:
                print_error("Invalid choice")
        while True:
            screen.clear()
            screen.refresh()
            screen.addstr("[1] List all students")
            screen.addstr("\n[2] List all courses")
            screen.addstr("\n[3] Show marks of a course")
            screen.addstr("\n[4] Calculate GPA for a student")
            screen.addstr("\n[5] Print a sorted student list by GPA in descending order")
            screen.addstr("\n[6] Cancel\n")

            screen.addstr("Enter the corresponding number")
            screen.refresh()
            choice4 = int(screen.getstr().decode())
            screen.clear()
            screen.refresh()
            if choice4 == 1:
                curses.curs_set(0)
                self.list_students()
                curses.napms(self.no_students * 1000)
                curses.curs_set(1)
            elif choice4 == 2:
                curses.curs_set(0)
                self.list_courses()
                curses.napms(self.no_courses * 1000)
                curses.curs_set(1)
            elif choice4 == 3:
                self.list_marks()
                curses.napms(self.no_students * 1000)
                curses.curs_set(1)
            elif choice4 == 4:
                self.calculate_gpa()
                curses.napms(1000)
                curses.curs_set(1)
            elif choice4 == 5:
                curses.curs_set(0)
                self.print_sorted_list()
                curses.napms(self.no_students * 1000)
                curses.curs_set(1)
            elif choice4 == 6:
                screen.clear()
                curses.curs_set(0)
                print_center("Exiting!")
                curses.napms(1000)
                curses.curs_set(1)
                curses.endwin()
                exit()
            else:
                print_error("Invalid choice")


if __name__ == '__main__':
    screen = curses.initscr()
    e = SMM()
    e.start_SMM()
