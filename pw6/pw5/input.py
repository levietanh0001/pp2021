import math

def add_students(stdscr):
    stdscr.addstr(2, 0, "id")
    studentId = int(stdscr.getstr(3, 0).decode())
    stdscr.addstr(4, 0, "name")
    studentName = stdscr.getstr(5, 0).decode()
    stdscr.addstr(6, 0, 'dob')
    dob = stdscr.getstr(7, 0).decode()
    stdscr.addstr(9, 0, str(studentId))
    return studentId, studentName, dob


def add_courses(stdscr):
    stdscr.addstr(2, 0, "id")
    courseId = int(stdscr.getstr(3, 0).decode())
    stdscr.addstr(4, 0, "name")
    courseName = stdscr.getstr(5, 0).decode()
    stdscr.addstr(6, 0, 'noOfCredit')
    noOfCredit = int(stdscr.getstr(7, 0).decode())
    return courseId, courseName, noOfCredit


def add_marks(stdscr):
    stdscr.addstr(2, 0, "studentId")
    studentId = stdscr.getstr(3, 0).decode()
    stdscr.addstr(4, 0, "courseId")
    courseId = stdscr.getstr(5, 0).decode()
    stdscr.addstr(6, 0, 'mark')
    mark = float(stdscr.getstr(7, 0).decode())
    mark = math.floor(mark)
    return studentId, courseId, mark


def add_student_id(stdscr):
    stdscr.addstr(2, 0, "studentId")
    studentId = int(stdscr.getstr(3, 0).decode())
    return studentId
