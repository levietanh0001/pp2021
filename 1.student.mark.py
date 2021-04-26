students_id = []
students_info = []
courses = []
courses_id = []
marks = []

def n_students():
    while True:
        no_students = int(input("-> Enter the total number of students: "))
        if (no_students < 0):
            print("***Error: number of students cannot be negative***")
        else:
            break
    return no_students

def n_courses():
    while True:
        no_courses = int(input("-> Enter total number of courses: "))
        if no_courses < 0:
            print("***Error: Number of courses cannot be negative***")
        else:
            break
    return no_courses


# Create a dictionary for storing student info
def student_dict(stu_id, name, dob):
    this_student = {
        "id": stu_id,
        "name": name,
        "dob": dob
    }
    students_info.append(this_student)
    students_id.append(stu_id)

# Create a dictionary for storing course info
def course(c_id, name):
    this_course = {
        "id": c_id,
        "name": name
    }
    courses.append(this_course)
    courses_id.append(c_id)


# Create a dictionary holding a mark entity's information and put it into list marks[]
# A mark entity will have a specified student ID, course ID and its value
def mark(stu_id, c_id, value):
    this_mark = {
        "sid": stu_id,
        "cid": c_id,
        "value": value
    }
    marks.append(this_mark)

def input_student_info():
    while True:
        sid = input("-> Enter student ID: ")
        if len(sid) == 0 or sid is None:
            print("***Error: Student ID cannot be empty***")
        else:
            break
    if sid in students_id:
        print("***Error: Student ID already exists***")
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
        student_dict(sid, name, dob)

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
    for s in students_info:
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
    for s in students_info:
        print("\t\t[%s]    %-20s%s" % (s['id'], s['name'], s['dob']))

    print()


def list_course_marks(cid):
    for m in marks:
        if m['cid'] == cid:
            sid = m['sid']
            for s in students_info:
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
    print("Loading Student Mark manager...")
    print("Choose your option:")
    print("[1] Input number of students and their information")
    print("[2] Input number of courses and their detail")
    print("[3] Cancel")
    print()
    choice1 = int(input("Enter the corresponding number: "))
    while True:
        if choice1 == 1:
            no_students = n_students()
            for i in range(no_students):
                print(f"Student #{i + 1}:")
                input_student_info()
            while len(courses) == 0:
                print("[1] Input number of courses and their information")
                print("[2] Cancel")
                choice2 = int(
                    input("Select your option by entering the digit: "))
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
        elif choice1 == 2:
            no_courses = n_courses()
            for i in range(no_courses):
                print(f"Course #{i + 1}:")
                input_course_info()
            while len(students_info) == 0:
                print("[1] Input number of students and their information: ")
                print("[2] Cancel")
                choice2 = int(
                    input("Select your option by entering the digit: "))
                if choice2 == 1:
                    no_students = n_students()
                    for i in range(no_students):
                        print(f"Student #{i + 1}:")
                        input_student_info()
                    break
                elif choice2 == 2:
                    print("Exiting!")
                    exit()
                else:
                    print("***Error: Invalid choice***")
                    break
            break
        elif choice1 == 3:
            print("Exiting!")
            exit()
        else:
            print("***Error: Invalid choice***")
            exit()
    while len(marks) < len(students_info) * len(courses):
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
