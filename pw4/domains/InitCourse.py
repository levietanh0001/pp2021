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
        return self.credit