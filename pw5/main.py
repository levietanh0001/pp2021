from domains import *
from input import *
from output import print_menu
import curses
import time
import math
import zipfile
import os


def main(stdscr):
    menu = ['AddStudent', 'AddCourse', 'AddMark', 'ShowStudent', 'ShowCourse', 'ShowMark', 'StudentAverageGpa',
            'SortDescendingOrder','Exit']

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0

    print_menu(stdscr, current_row_idx)
    if os.path.isfile('students.dat'):
        zip_file = zipfile.ZipFile('students.dat', 'r')
        zip_file.extractall()

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 0:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            studentId, studentName, dob = add_students(stdscr)
            student = Student(studentId, studentName, dob)
            a_file = open("student.txt", "r")

            lines = a_file.readlines()
            a_file.close()
            new_file = open("student.txt", "w")
            m = 0
            for line in lines:
                if (line.strip("\n").split("--")[0] != str(student.get_student_id())):
                    m = 1
                    new_file.write(line)
            if (m == 1):
                new_file.write(f"{student.get_student_id()}--{student.get_name()}--{student.get_dob()} \n")

            new_file.close()

            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 1:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            m = 0
            courseId, courseName, noOfCredit = add_courses(stdscr)
            course = Course(courseId, courseName, noOfCredit)

            a_file = open("course.txt", "r")

            lines = a_file.readlines()
            a_file.close()
            new_file = open("course.txt", "w")
            m = 0
            for line in lines:
                if (line.strip("\n").split("--")[0] != str(course.get_course_id())):
                    m = 1
                    new_file.write(line)
            if (m == 1):
                new_file.write(f"{course.get_course_id()}--{course.get_course_name()}--{course.get_course_credit()} \n")

            new_file.close()

            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 2:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            m = 0
            studentId, courseId, mark = add_marks(stdscr)
            grade = Mark(studentId, courseId, mark)
            a_file = open("course.txt", "r")

            lines = a_file.readlines()
            a_file.close()
            new_file = open("course.txt", "w")
            m = 0
            for line in lines:
                if str(line.split("--")[0]) == str(grade.get_student_id()) and line.split("--")[1] == str(
                        grade.get_course_id()):
                    m = 1
                    new_file.write(line)
            if (m == 1):
                new_file.write(f"{grade.get_student_id()}--{grade.get_course_id()}--{grade.get_grade()} \n")

            new_file.close()
            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 3:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            studentId = add_student_id(stdscr)
            with open("student.txt", "r") as sf:
                for line in sf.readlines():
                    if str(line.split("--")[0]) == str(studentId):
                        x = line.split("--")
                        stdscr.addstr(6, 0,
                                      "StudentId: " + str(x[0]) + " Student name: " + x[1] + " Dob: " + x[2])
                        break
                    else:
                        continue
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 4:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            stdscr.addstr(2, 0, "courseId")
            courseId = int(stdscr.getstr(3, 0).decode())
            with open("course.txt", "r") as sf:
                for line in sf.readlines():
                    if str(line.split("--")[0]) == str(courseId) in line:
                        x = line.split("--")
                        stdscr.addstr(6, 0,
                                      "CourseId: " + str(x[0]) + " Course name: " + str(x[1]) + " Credit: " + str(x[2]))
                        break
                    else:
                        continue
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 5:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            stdscr.addstr(2, 0, "courseName")
            courseName = stdscr.getstr(3, 0).decode()
            courseId = 0
            x = 0
            y = 5
            num = 0
            with open("course.txt", "r") as sf:
                for line in sf.readlines():
                    if line.split("--")[1] == courseName:
                        courseId = line.split("--")[0]
            with open("mark.txt", "r") as sf:
                for line in sf.readlines():
                    if line.split("--")[1] == str(courseId):
                        stdscr.addstr(y + num, x,
                                      "Student Id: " + str(line.split("--")[0]) + ' Student grade: ' + str(
                                          line.split("--")[2]))
                        num += 2

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 6:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            studentId = add_student_id(stdscr)
            stdscr.addstr(5, 0, "student average marks: ")
            totalMark = 0
            courseNum = 0
            with open("mark.txt", "r") as sf:
                for line in sf.readlines():
                    if line.split("--")[0] == str(studentId):
                        totalMark += float(line.split("--")[2])
                        courseNum += 1
            averageMark = totalMark / courseNum
            stdscr.addstr(7, 0, str(averageMark))
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 7:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'Hello World')
            averageGpa = []
            students = []
            with open("student.txt", "r") as sf:
                for line in sf.readlines():
                    students.append(str(line.split("--")[0]))
            with open("mark.txt", "r") as f:
                for i in range(len(students)):
                    print(students[i])
                    totalMark = 0
                    courseNum = 0

                    with open("mark.txt", "r") as sf:
                        for line in sf.readlines():
                            if line.split("--")[0] == str(students[i]):
                                totalMark += float(line.split("--")[2])
                                courseNum += 1

                    averageMark = totalMark / courseNum
                    averageGpa.append([students[i], averageMark])

            averageGpa.sort(key=lambda x: x[1], reverse=True)
            y = 2
            x = 0
            for i in range(len(averageGpa)):
                stdscr.addstr(y + i * 2, x, "StudentId: " + str(averageGpa[i][0]) + " Student AverageGpa: " +
                              str(averageGpa[i][1]))

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 8:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(0, 0, 'We will decompress file into .dat')
            file_list = ['student.txt', 'course.txt', 'mark.txt']
            with zipfile.ZipFile('students.dat', 'w') as new_zip:
                for file_name in file_list:
                    new_zip.write(file_name)

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 9:
            break

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
