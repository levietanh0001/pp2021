class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def get_student_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def set_student_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def __eq__(self, other):
        return self.id == other.id

    def get_key(self):
        return self.get_student_id()

    def displayStudentInformation(self):
        print("Student Id: %d, Student name: %s, Student dob: %s" % (self.id, self.name, self.dob))


class Course:
    def __init__(self, courseId, courseName, noOfCredit):
        self.courseId = courseId
        self.courseName = courseName
        self.noOfCredit = noOfCredit

    def get_course_id(self):
        return self.courseId

    def get_course_name(self):
        return self.courseName

    def get_course_credit(self):
        return self.noOfCredit

    def set_course_name(self, courseName):
        self.courseName = courseName

    def set_course_id(self, courseId):
        self.courseId = courseId

    def set_course_credit(self, noOfCredit):
        self.noOfCredit = noOfCredit

    def __eq__(self, other):
        return self.courseId == other.courseId

    def get_key(self):
        return self.get_course_id()

    def displayCourseInformation(self):
        print(
            "CourseId: {}, Course name: {}, Course credit: {}".format(self.courseId, self.courseName, self.noOfCredit))


class Mark:
    def __init__(self, studentId, courseId, grade):
        self.studentId = studentId
        self.courseId = courseId
        self.grade = grade

    def get_student_id(self):
        return self.studentId

    def get_course_id(self):
        return self.courseId

    def get_grade(self):
        return self.grade

    def set_student_id(self, studentId):
        self.studentId = studentId

    def set_course_id(self, courseId):
        self.courseId = courseId

    def set_grade(self, grade):
        self.grade = grade

    def __eq__(self, other):
        return self.get_student_id() == other.get_student_id() and self.get_course_id() == other.get_course_id()

    def displayStudentMark(self, studentName):
        print("Student Id: {}, Student Name: {}, Student Mark: {} ".format(self.studentId, studentName, self.grade))