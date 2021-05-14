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