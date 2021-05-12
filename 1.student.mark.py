    # arrays containing info
students_id_list = []
students_info_list = []
courses = []
courses_id = []
marks = []

def NumOfStds():
    while True:
        num_of_students = int(input("Total number of students: "))
        if (num_of_students < 0):
            print("Negative number of students is not valid!")
        else:
            break
    return num_of_students

    # dictionary for student info
def CreateStudentDict(student_id, name, dob):
    aboutStudent = {
        "id": student_id,
        "name": name,
        "dob": dob
    }
    students_info_list.append(aboutStudent)
    students_id_list.append(student_id)

def NumOfCourses():
    while True:
        num_of_courses = int(input("Total number of courses: "))
        if num_of_courses < 0:
            print("Negative number of courses is not valid")
        else:
            break
    return num_of_courses

    # create a dictionary for course info
def CreateCourseDict(course_id, name):
    aboutCourse = {
        "id": course_id,
        "name": name
    }
    courses.append(aboutCourse)
    courses_id.append(course_id)

    # create a dictionary for marks
def CreateMarkDict(student_id, course_id, value):
    aboutMark = {
        "sid": student_id,
        "cid": course_id,
        "value": value
    }
    marks.append(aboutMark)

def StudentInfoQuery():
    while True:
        sid = input("-> Enter student ID: ")
        if len(sid) == 0 or sid is None:
            print("Negative student ID is not allowed!")
        else:
            break
    if sid in students_id_list:
        print("Student ID already exists")
        exit()
    else:
        while True:
            name = input("-> Enter student name: ")
            if len(name) == 0 or name is None:
                print("***Error: Student name cannot be empty***")
            else:
                break
        while True:
            dob = input("-> Enter student date of birth: ")
            if len(dob) == 0 or dob is None:
                print("***Error: Student date of birth cannot be empty***")
            else:
                break
        print(f"Student successfully added: {name}")
        CreateStudentDict(sid, name, dob)

def input_course_info():
    while True:
        cid = input("-> Enter course ID: ")
        if len(cid) == 0 or cid is None:
            print("***Error: Course ID cannot be empty***")
        else:
            break
    if cid in courses_id:
        print("***Error: Course ID already exists***")
        exit()
    else:
        while True:
            name = input("-> Enter course name: ")
            if len(name) == 0 or name is None:
                print("***Error: Course name cannot be empty***")
            else:
                break
        print(f"Successfully added course: {name}")
        course(cid, name)

def input_course_marks(cid):
    for s in students_info_list:
        sid = s['id']
        while True:
            value = float(input(f"-> Enter marks for {s['name']}: "))
            if value < 0:
                print("***Error: Marks must be non-negative***")
            else:
                break
        mark(sid, cid, value)


def input_marks():
    while True:
        cid = input("-> Enter Course ID for which you want to input marks: ")
        if cid in courses_id:
            if len(marks) > 0:
                marked = False
                for m in marks:
                    if m['cid'] == cid:
                        print("***Error: You have already input marks for this course***")
                        marked = True
                        break
                if not marked:
                    input_course_marks(cid)
            else:
                input_course_marks(cid)
            break
        elif len(cid) == 0 or cid is None:
            print("***Error: Course ID cannot be empty***")
        else:
            print("***Error: No course found for the input ID***")
            return -1


def list_courses():
    print("List of all Courses:")
    for c in courses:
        print("\t\t[%s]   %-20s" % (c['id'], c['name']))

    print()


def list_students():
    print("All Students in class:")
    for s in students_info_list:
        print("\t\t[%s]    %-20s%s" % (s['id'], s['name'], s['dob']))

    print()


def list_course_marks(cid):
    for m in marks:
        if m['cid'] == cid:
            sid = m['sid']
            for s in students_info_list:
                if s['id'] == sid:
                    print(f"\t\t[%s]    %-20s%s" % (s['id'], s['name'], m['value']))


# Ask the user for the course ID whose mark should be listed, then invoke the list_course_marks() function
def list_marks():
    while True:
        cid = input("-> Enter the course ID for which you want to see marks: ")
        if len(cid) == 0 or cid is None:
            print("***Error: Course ID cannot be empty***")
        else:
            break
    if cid in courses_id:
        list_course_marks(cid)
    else:
        print("***Error: No course exists for the input ID***")
        return -1


def main():
    print("1 = Input students' details")
    print("2 = Input courses' details")
    print("3 = Exit")
    print()
    myChoice = int(input("Enter your choice: "))
    while True:
        if myChoice == 1:
            num_of_stds = NumOfStds()
            for i in range(num_of_stds):
                print(f"-Student {i + 1}-")
                StudentInfoQuery()
            while len(courses) == 0:
                print("[1] Input courses' details")
                print("[2] Cancel")
                choice2 = int(input("Select your option by entering the digit: "))
                if choice2 == 1:
                    no_courses = n_courses()
                    for i in range(no_courses):
                        print(f"Course #{i + 1}:")
                        input_course_info()
                    break
                elif choice2 == 2:
                    print("Exiting!")
                    exit()
                else:
                    print("***Error: Invalid choice***")
            break
        elif myChoice == 2:
            no_courses = n_courses()
            for i in range(no_courses):
                print(f"Course #{i + 1}:")
                input_course_info()
            while len(students_info_list) == 0:
                print("[1] Input number of students and their information: ")
                print("[2] Cancel")
                choice2 = int(
                    input("Select your option by entering the digit: "))
                if choice2 == 1:
                    num_of_stds = NumOfStds()
                    for i in range(num_of_stds):
                        print(f"Student #{i + 1}:")
                        StudentInfoQuery()
                    break
                elif choice2 == 2:
                    print("Exiting!")
                    exit()
                else:
                    print("***Error: Invalid choice***")
                    break
            break
        elif myChoice == 3:
            print("Exiting!")
            exit()
        else:
            print("***Error: Invalid choice***")
            exit()
    while len(marks) < len(students_info_list) * len(courses):
        print("[1] Input mark for a course")
        print("[2] List students")
        print("[3] List courses")
        print("[4] Cancel")
        print()
        choice3 = int(input("Select your option by entering the digit: "))
        if choice3 == 1:
            input_marks()
        elif choice3 == 2:
            list_students()
        elif choice3 == 3:
            list_courses()
        elif choice3 == 4:
            print("Exiting!")
            exit()
        else:
            print("***Error: invalid choice***")
    while True:
        print("[1] List students")
        print("[2] List courses")
        print("[3] Show marks of a course")
        print("[4] Cancel")
        choice3 = int(input("Enter the corresponding number: "))
        if choice3 == 1:
            list_students()
        elif choice3 == 2:
            list_courses()
        elif choice3 == 3:
            list_marks()
        elif choice3 == 4:
            print("Exiting!")
            exit()
        else:
            print("***Error: invalid choice***")


main()
