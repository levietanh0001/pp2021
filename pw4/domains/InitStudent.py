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