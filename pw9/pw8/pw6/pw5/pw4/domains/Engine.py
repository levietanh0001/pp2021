import input
import output
import curses


class Engine:
    # List students to store student objects
    students = []
    # List students_id to store students id, so that we can fetch id more easily afterwards
    students_id = []
    # List courses to store course objects
    courses = []
    # List courses_id to store courses id
    courses_id = []
    # List marks to store mark objects that are the marks of courses and students
    marks = []

    number_of_students = None
    number_of_courses = None

    def __init__(self, scr):
        self.__screen = scr
        self.__input = input.Input(scr)
        self.__output = output.Output(scr)

    # Define a method to print error
    def print_error(self, error):
        self.__screen.addstr("\nError: " + error + ".", curses.color_pair(1) |
                      curses.A_BOLD | curses.A_UNDERLINE | curses.A_BLINK)
        self.__screen.refresh()
        curses.napms(3000)
        self.__screen.clear()
        self.__screen.refresh()

    # A method to start the program
    def start_engine(self):

        # print("Initializing engine...\n")
        # print("--- Student Manager ---\n")

        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        num_rows, num_cols = self.__screen.getmaxyx()

        # Make a function to print a line in the center of screen
        def print_center(message):
            # Calculate center row
            middle_row = int(num_rows / 2)

            # Calculate center column, and then adjust starting position based
            # on the length of the message
            half_length_of_message = int(len(message) / 2)
            middle_column = int(num_cols / 2)
            x_position = middle_column - half_length_of_message

            # Draw the text
            if message == "--- Student Manager ---":
                self.__screen.addstr(middle_row, x_position, message, curses.A_BOLD)
                self.__screen.refresh()
            else:
                self.__screen.addstr(middle_row, x_position, message)
                self.__screen.refresh()

        curses.curs_set(0)
        self.__screen.refresh()
        print_center("Loading Student Mark Manager")
        curses.napms(500)
        for i in range(3):
            self.__screen.addstr(".")
            self.__screen.refresh()
            curses.napms(500)
        self.__screen.clear()
        self.__screen.refresh()
        curses.napms(500)
        print_center("--- Select from the MENU ---")
        self.__screen.refresh()
        curses.napms(2000)
        self.__screen.clear()
        self.__screen.refresh()

        # print("\n[1] Input number of student and students information")
        # print("[2] Input number of courses and courses information")
        # print("[3] Cancel\n")

        curses.curs_set(1)
        self.__screen.addstr("[1] Input number of student and students information")
        self.__screen.addstr("\n[2] Input number of courses and courses information")
        self.__screen.addstr("\n[3] Cancel\n")

        # choice1 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
        self.__screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
        self.__screen.refresh()
        choice1 = int(self.__screen.getstr().decode())
        while True:
            if choice1 == 1:
                self.__screen.clear()
                self.__screen.refresh()
                self.__input.input_number_of_students(self)
                self.__screen.clear()
                self.__screen.refresh()
                for i in range(self.number_of_students):
                    # print(f"Student #{i + 1}:")
                    self.__screen.addstr(f"Student #{i + 1}:\n")
                    self.__screen.refresh()
                    self.__input.input_student_information(self)
                    self.__screen.clear()
                    self.__screen.refresh()
                while len(self.courses) == 0:
                    self.__screen.addstr("[1] Input number of courses and courses information")
                    self.__screen.addstr("\n[2] Cancel\n")
                    self.__screen.refresh()
                    # choice2 = int(
                    #     input("Select the functionality you want to proceed (by input the corresponding number): "))
                    self.__screen.addstr(
                        "Select the functionality you want to proceed (by input the corresponding number): ")
                    self.__screen.refresh()
                    choice2 = int(self.__screen.getstr().decode())
                    if choice2 == 1:
                        self.__screen.clear()
                        self.__screen.refresh()
                        self.__input.input_number_of_courses(self)
                        self.__screen.clear()
                        self.__screen.refresh()
                        for i in range(self.number_of_courses):
                            # print(f"Course #{i + 1}:")
                            self.__screen.addstr(f"Course #{i + 1}:\n")
                            self.__screen.refresh()
                            self.__input.input_course_information(self)
                            self.__screen.clear()
                            self.__screen.refresh()
                        break
                    elif choice2 == 2:
                        # print("Good bye!")
                        self.__screen.clear()
                        curses.curs_set(0)
                        print_center("Good bye!")
                        curses.napms(1000)
                        curses.curs_set(1)
                        curses.endwin()
                        exit()
                    else:
                        # print("Error: Invalid choice.")
                        self.print_error("Invalid choice")
                break
            elif choice1 == 2:
                self.__screen.clear()
                self.__screen.refresh()
                self.__input.input_number_of_courses(self)
                self.__screen.clear()
                self.__screen.refresh()
                for i in range(self.number_of_courses):
                    # print(f"Course #{i + 1}:")
                    self.__screen.addstr(f"Course #{i + 1}:\n")
                    self.__screen.refresh()
                    self.__input.input_course_information(self)
                    self.__screen.clear()
                    self.__screen.refresh()
                while len(self.students) == 0:
                    self.__screen.addstr("[1] Input number of students and students information")
                    self.__screen.addstr("\n[2] Cancel\n")
                    self.__screen.refresh()
                    # choice2 = int(
                    #     input("Select the functionality you want to proceed (by input the corresponding number): "))
                    self.__screen.addstr(
                        "Select the functionality you want to proceed (by input the corresponding number): ")
                    self.__screen.refresh()
                    choice2 = int(self.__screen.getstr().decode())
                    if choice2 == 1:
                        self.__screen.clear()
                        self.__screen.refresh()
                        self.__input.input_number_of_students(self)
                        self.__screen.clear()
                        self.__screen.refresh()
                        for i in range(self.number_of_students):
                            # print(f"Student #{i + 1}:")
                            self.__screen.addstr(f"Student #{i + 1}:\n")
                            self.__screen.refresh()
                            self.__input.input_student_information(self)
                            self.__screen.clear()
                            self.__screen.refresh()
                        break
                    elif choice2 == 2:
                        # print("Good bye!")
                        self.__screen.clear()
                        curses.curs_set(0)
                        print_center("Good bye!")
                        curses.napms(1000)
                        curses.curs_set(1)
                        curses.endwin()
                        exit()
                    else:
                        # print("Error: Invalid choice.")
                        self.print_error("Invalid choice")
                        break
                break
            elif choice1 == 3:
                # print("Good bye!")
                self.__screen.clear()
                curses.curs_set(0)
                print_center("Good bye!")
                curses.napms(1000)
                curses.curs_set(1)
                curses.endwin()
                exit()
            else:
                # print("Error: Invalid choice.\n")
                self.print_error("Invalid choice")
                curses.endwin()
                exit()
        while len(self.marks) < len(self.students) * len(self.courses):
            self.__screen.clear()
            self.__screen.refresh()
            self.__screen.addstr("[1] Input mark for a course")
            self.__screen.addstr("\n[2] List students")
            self.__screen.addstr("\n[3] List courses")
            self.__screen.addstr("\n[4] Cancel\n")
            # choice3 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
            self.__screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
            self.__screen.refresh()
            choice3 = int(self.__screen.getstr().decode())
            self.__screen.clear()
            self.__screen.refresh()
            if choice3 == 1:
                self.__input.input_mark(self)
            elif choice3 == 2:
                curses.curs_set(0)
                self.__output.list_students(self)
                curses.napms(self.number_of_students * 1000)
                curses.curs_set(1)
            elif choice3 == 3:
                curses.curs_set(0)
                self.__output.list_courses(self)
                curses.napms(self.number_of_courses * 1000)
                curses.curs_set(1)
            elif choice3 == 4:
                # print("Good bye!")
                self.__screen.clear()
                curses.curs_set(0)
                print_center("Good bye!")
                curses.napms(1000)
                curses.curs_set(1)
                curses.endwin()
                exit()
            else:
                # print("Error: invalid choice.")
                self.print_error("Invalid choice")
        while True:
            self.__screen.clear()
            self.__screen.refresh()
            self.__screen.addstr("[1] List students")
            self.__screen.addstr("\n[2] List courses")
            self.__screen.addstr("\n[3] Show marks of a course")
            self.__screen.addstr("\n[4] Calculate GPA for a student")
            self.__screen.addstr("\n[5] Print a sorted student list by GPA descending")
            self.__screen.addstr("\n[6] Cancel\n")
            # choice4 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
            self.__screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
            self.__screen.refresh()
            choice4 = int(self.__screen.getstr().decode())
            self.__screen.clear()
            self.__screen.refresh()
            if choice4 == 1:
                curses.curs_set(0)
                self.__output.list_students(self)
                curses.napms(self.number_of_students * 1000)
                curses.curs_set(1)
            elif choice4 == 2:
                curses.curs_set(0)
                self.__output.list_courses(self)
                curses.napms(self.number_of_courses * 1000)
                curses.curs_set(1)
            elif choice4 == 3:
                self.__output.list_marks(self)
                curses.napms(self.number_of_students * 1000)
                curses.curs_set(1)
            elif choice4 == 4:
                self.__output.calculate_gpa(self)
                curses.napms(1000)
                curses.curs_set(1)
            elif choice4 == 5:
                curses.curs_set(0)
                self.__output.print_sorted_list(self)
                curses.napms(self.number_of_students * 1000)
                curses.curs_set(1)
            elif choice4 == 6:
                # print("Good bye!")
                self.__screen.clear()
                curses.curs_set(0)
                print_center("Good bye!")
                curses.napms(1000)
                curses.curs_set(1)
                curses.endwin()
                exit()
            else:
                # print("Error: invalid choice.")
                self.print_error("Invalid choice")
