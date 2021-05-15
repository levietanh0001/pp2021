import math
import curses
import numpy as np


class Output:
    def __init__(self, screen):
        self.screen = screen

    def PrintError(self, error):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        screen.addstr("\nError: " + error, curses.color_pair(1) | curses.A_BOLD)
        screen.refresh()
        curses.napms(1000)
        screen.clear()
        screen.refresh()

    def printCourses(self, StudentMarkManagementSystem):
        self.screen.addstr("Printing all courses: ")
        self.screen.refresh()
        for course in StudentMarkManagementSystem.courses_list:
            self.screen.addstr("ID = %s, %s, %s" % (course.getCourseID(), course.getName(), course.getCredit()))
            self.screen.refresh()

    def printStudents(self, StudentMarkManagementSystem):
        self.screen.addstr("Printing all Students in class:")
        self.screen.refresh()
        for student in StudentMarkManagementSystem.students_info_list:
            self.screen.addstr("%s %s %s" % (student.getStudentID(), student.getName(), student.getDOB()))
            self.screen.refresh()

    def printCourseMarks(self, StudentMarkManagementSystem,course_id):
        for mark in StudentMarkManagementSystem.marks_list:
            if mark.getCourseID() == course_id:
                student_id = mark.getStudentID()
                for student in StudentMarkManagementSystem.students_info_list:
                    if student.getStudentID() == student_id:
                        self.screen.addstr(f"%s %s %s" % (student.getStudentID(), student.getName(), mark.getStudentMark()))
                        self.screen.refresh()

    def printMarks(self, StudentMarkManagementSystem):
        while True:
            self.screen.addstr("- Enter the course ID for which you want to list marks: ")
            self.screen.refresh()
            course_id = self.screen.getstr().decode()
            if course_id is None:
                PrintError("Course ID cannot be null")
            else:
                break
        if course_id in StudentMarkManagementSystem.courses_id_list:

            self.printCourseMarks(StudentMarkManagementSystem,course_id)
        else:
            PrintError("There exist no course with that ID!")
            return -1

    def computeStudentGPA(self, StudentMarkManagementSystem ,sid):
        marks_arr = np.array([])
        course_credits = np.array([])
        for mark in StudentMarkManagementSystem.marks_list:
            if mark.getStudentID() == sid:
                for course in StudentMarkManagementSystem.courses_list:
                    if course.getCourseID() == mark.getCourseID():
                        marks_arr = np.append(marks_arr, mark.getStudentMark())
                        course_credits = np.append(course_credits, course.getCredit())
        gpa = np.dot(marks_arr, course_credits) / np.sum(course_credits)
        rounded_gpa = math.floor(gpa * 10) / 10.0

        for student in StudentMarkManagementSystem.students_info_list:
            if student.getStudentID() == sid:
                student.setGPA(rounded_gpa)

    def computeGPA(self, StudentMarkManagementSystem):
        while True:
            self.screen.addstr("Enter student ID to compute the student GPA: ")
            self.screen.refresh()
            sid = self.screen.getstr().decode()
            if len(sid) == 0 or sid is None:
                PrintError("Student ID cannot be null!")
            elif sid not in StudentMarkManagementSystem.students_id_list:
                PrintError("Student ID does not exist!")
            else:
                break
        for student in StudentMarkManagementSystem.students_info_list:
            if student.getStudentID() == sid:
                self.computeStudentGPA(sid)
                self.screen.addstr("Student %s has GPA = %.1f" % (student.getName(), student.getGPA()))
                self.screen.refresh()
                break

    def printSortedList(self, StudentMarkManagementSystem):

        new_student_list = []
        for student in StudentMarkManagementSystem.students_info_list:
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
            self.screen.addstr("ID = %s, %s, GPA = %s\n" % (student[0], student[1], student[2]))
            self.screen.refresh()
