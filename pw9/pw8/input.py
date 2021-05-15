import math
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class Input:
    def __init__(self, scr):
        self.__screen = scr

    # Define a method to print error
    def print_error(self, error):
        self.__screen.addstr("\nError: " + error + ".", curses.color_pair(1) |
                      curses.A_BOLD | curses.A_UNDERLINE | curses.A_BLINK)
        self.__screen.refresh()
        curses.napms(3000)
        self.__screen.clear()
        self.__screen.refresh()

    # Function to ask user to input number of student.
    # Print error and force the user to re-input if wrong data is given.
    def input_number_of_students(self, engine):
        while True:
            # number_of_students = int(input("- Enter number of students: "))
            self.__screen.addstr("-> Enter number of students: ")
            self.__screen.refresh()
            number_of_students = int(self.__screen.getstr().decode())
            if number_of_students < 0:
                # print("Error: number of students must be non-negative")
                self.print_error("number of students must be non-negative")
            else:
                break
        engine.number_of_students = number_of_students

    # Function to ask user to input number of courses.
    # Print error and force the user to re-input if wrong data is given.
    def input_number_of_courses(self, engine):
        while True:
            # number_of_courses = int(input("- Enter number of courses: "))
            self.__screen.addstr("-> Enter number of courses: ")
            self.__screen.refresh()
            number_of_courses = int(self.__screen.getstr().decode())
            if number_of_courses < 0:
                # print("Error: number of courses must be non-negative")
                self.print_error("number of courses must be non-negative")
            else:
                break
        engine.number_of_courses = number_of_courses

    # Function to input a student object information. Force the user to re-input if wrong data is given
    def input_student_information(self, engine):
        while True:
            # sid = input("- Enter student ID: ")
            self.__screen.addstr("-> Enter student ID: ")
            self.__screen.refresh()
            sid = self.__screen.getstr().decode()
            if len(sid) == 0 or sid is None:
                # print("Error: Student ID cannot be empty")
                self.print_error("Student ID cannot be empty")
            else:
                break
        if sid in engine.students_id:
            # print("Error: Student ID existed")
            self.print_error("Student ID already exists")
            curses.endwin()
            exit()
        else:
            while True:
                # name = input("- Enter student name: ")
                self.__screen.addstr("-> Enter student name: ")
                self.__screen.refresh()
                name = self.__screen.getstr().decode()
                if len(name) == 0 or name is None:
                    # print("Error: Student name cannot be empty")
                    self.print_error("Student name cannot be empty")
                else:
                    break
            while True:
                # dob = input("- Enter student date of birth: ")
                self.__screen.addstr("-> Enter student date of birth: ")
                self.__screen.refresh()
                dob = self.__screen.getstr().decode()
                if len(dob) == 0 or dob is None:
                    # print("Error: Student date of birth cannot be empty")
                    self.print_error("Student date of birth cannot be empty")
                else:
                    break
            curses.curs_set(0)
            self.__screen.addstr(f"\n Successfully Added student: {name}")
            self.__screen.refresh()
            curses.napms(1000)
            curses.curs_set(1)
            Student(engine, sid, name, dob)

    # Function to input a course object information. Force the user to re-input if wrong data is given
    def input_course_information(self, engine):
        while True:
            # cid = input("- Enter course ID: ")
            self.__screen.addstr("-> Enter course ID: ")
            self.__screen.refresh()
            cid = self.__screen.getstr().decode()
            if len(cid) == 0 or cid is None:
                # print("Error: Course ID cannot be empty")
                self.print_error("Course ID cannot be empty")
            else:
                break
        if cid in engine.courses_id:
            # print("Error: Course ID existed")
            self.print_error("Course ID existed")
            curses.endwin()
            exit()
        else:
            while True:
                # name = input("- Enter course name: ")
                self.__screen.addstr("-> Enter course name: ")
                self.__screen.refresh()
                name = self.__screen.getstr().decode()
                if len(name) == 0 or name is None:
                    # print("Error: Course name cannot be empty")
                    self.print_error("Course name cannot be empty")
                else:
                    break
            while True:
                # credit = int(input("- Enter course credits: "))
                self.__screen.addstr("-> Enter course credits: ")
                self.__screen.refresh()
                credit = int(self.__screen.getstr().decode())
                if credit < 0:
                    # print("Error: Course credit must be non-negative")
                    self.print_error("Course credit must be non-negative")
                elif credit is None:
                    # print("Error: Course credit cannot be empty")
                    self.print_error("Course credit cannot be empty")
                else:
                    break
            curses.curs_set(0)
            self.__screen.addstr(f"\nSuccessfully Added course: {name}")
            self.__screen.refresh()
            curses.napms(1000)
            curses.curs_set(1)
            Course(engine, cid, name, credit)

    # Function to input a mark object information. Force the user to re-input if wrong data is given
    def input_course_mark(self, engine, cid):
        for student in engine.students:
            sid = student.get_sid()
            while True:
                # value = float(input(f"- Enter mark for {student.get_name()}: "))
                self.__screen.addstr(f"-> Enter mark for {student.get_name()}: ")
                self.__screen.refresh()
                value = float(self.__screen.getstr().decode())
                value = math.floor(value * 10) / 10.0
                if value < 0:
                    # print("Error: Mark must be non-negative")
                    self.print_error("Mark must be non-negative")
                else:
                    break
            Mark(engine, sid, cid, value)

    # Ask the user for the course ID whose mark should be input, then invoke the input_course_mark() function
    def input_mark(self, engine):
        while True:
            # cid = input("- Enter the course ID you want to input mark: ")
            self.__screen.addstr("-> Enter the course ID you want to input mark: ")
            self.__screen.refresh()
            cid = self.__screen.getstr().decode()
            self.__screen.clear()
            self.__screen.refresh()
            if cid in engine.courses_id:
                if len(engine.marks) > 0:
                    existed = False
                    for mark in engine.marks:
                        if mark.get_cid() == cid:
                            # print("Error: You've already input mark for this course.")
                            self.print_error("You have already input mark for this course")
                            existed = True
                            break
                    if not existed:
                        self.input_course_mark(engine, cid)
                else:
                    self.input_course_mark(engine, cid)
                break
            elif len(cid) == 0 or cid is None:
                # print("Error: Course ID cannot be empty.")
                self.print_error("Course ID cannot be empty")
            else:
                # print("Error: There exist no course with that ID.")
                self.print_error("There exist no course with that ID")
                return -1
