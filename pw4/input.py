import math
import curses
from domains.InitStudent import *
from domains.InitCourse import *
from domains.InitMark import *


class Input:
    def __init__(self, screen):
        self.screen = screen

    # Define a method to print error
    def PrintError(self, error):
        self.screen.addstr("\nError: " + error + ".", curses.color_pair(1) |
                      curses.A_BOLD | curses.A_UNDERLINE | curses.A_BLINK)
        self.screen.refresh()
        curses.napms(3000)
        self.screen.clear()
        self.screen.refresh()

    def PrintError(self, error):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        self.screen.addstr("\nError: " + error, curses.color_pair(1) | curses.A_BOLD)
        self.screen.refresh()
        curses.napms(1000)
        self.screen.clear()
        self.screen.refresh()

    def getNumOfStudents(self, StudentMarkManagementSystem):
        while True:
            self.screen.addstr("\nEnter number of students: ")
            self.screen.refresh()
            num_of_students = int(self.screen.getstr().decode())
            if num_of_students < 0:
                PrintError("\nNumber of students cannot be negative")
            else:
                break
        StudentMarkManagementSystem.num_of_students = num_of_students

    def getNumOfCourses(self, StudentMarkManagementSystem):
        while True:
            self.screen.addstr("\nEnter number of courses: ")
            self.screen.refresh()
            num_of_courses = int(self.screen.getstr().decode())
            if num_of_courses < 0:
                PrintError("\nNumber of courses cannot be negative")
            else:
                break
        StudentMarkManagementSystem.num_of_courses = num_of_courses

    def getStudentInfo(self, StudentMarkManagementSystem):
        while True:
            self.screen.addstr("\nEnter student ID: ")
            self.screen.refresh()
            student_id = self.screen.getstr().decode()
            if student_id is None:
                PrintError("Student ID cannot be null!")
            else:
                break
        if student_id in StudentMarkManagementSystem.students_id_list:
            PrintError("Student ID already exists!")
            exit()
        else:
            while True:
                self.screen.addstr("Enter student name: ")
                self.screen.refresh()
                name = self.screen.getstr().decode()
                if name is None:
                    PrintError("Student name cannot be null!")
                else:
                    break
            while True:
                self.screen.addstr("Enter student dob/ date of birth: ")
                self.screen.refresh()
                dob = self.screen.getstr().decode()
                if dob is None:
                    PrintError("Student dob/ date of birth cannot be null!")
                else:
                    break

            self.screen.addstr(f"Added student {name}!")
            self.screen.refresh()
            curses.napms(500)
            InitStudent(StudentMarkManagementSystem, student_id, name, dob)

    def getCourseInfo(self, StudentMarkManagementSystem):
        while True:
            self.screen.addstr("\nEnter course ID: ")
            self.screen.refresh()
            course_id = self.screen.getstr().decode()
            if course_id is None:
                PrintError("Course ID cannot be null!")
            else:
                break
        if course_id in StudentMarkManagementSystem.courses_id_list:
            PrintError("Course ID already exists!")
            exit()
        else:
            while True:
                self.screen.addstr("Enter course name: ")
                self.screen.refresh()
                name = self.screen.getstr().decode()
                if name is None:
                    PrintError("Course name cannot be null!")
                else:
                    break
            while True:
                self.screen.addstr("Enter course credits: ")
                self.screen.refresh()
                credit = int(self.screen.getstr().decode())
                if credit < 0:
                    PrintError("Course credit can not be negative!")
                elif credit is None:
                    PrintError("Course credit cannot be null!")
                else:
                    break

            self.screen.addstr(f"Added course {name}!")
            self.screen.refresh()
            curses.napms(500)

            InitCourse(StudentMarkManagementSystem, course_id, name, credit)

    def getCourseMark(self, StudentMarkManagementSystem, course_id):
        for student in StudentMarkManagementSystem.students_info_list:
            student_id = student.getStudentID()
            studentName = student.getName()
            self.screen.addstr(f"Enter marks for {studentName}: ")
            self.screen.refresh()
            value = float(self.screen.getstr().decode())
            value = math.floor(value * 10) / 10.0
            InitMark(StudentMarkManagementSystem, student_id, course_id, value)

    def getMark(self, StudentMarkManagementSystem):
        while True:
            self.screen.addstr("Enter the course ID for which you want to input marks: ")
            self.screen.refresh()
            course_id = self.screen.getstr().decode()
            self.screen.clear()
            self.screen.refresh()
            if course_id in StudentMarkManagementSystem.courses_id_list:
                if len(StudentMarkManagementSystem.marks_list) > 0:
                    Marked = False
                    for mark in StudentMarkManagementSystem.marks_list:
                        if mark.getCourseID() == course_id:
                            PrintError("You have already input marks for this course!")
                            Marked = True
                            break
                    if not Marked:
                        self.getCourseMark(StudentMarkManagementSystem, course_id)
                else:
                    self.getCourseMark(StudentMarkManagementSystem, course_id)
                break
            elif course_id is None:
                PrintError("Course ID cannot be null!")
            else:
                PrintError("No course with such ID!")
                return -1