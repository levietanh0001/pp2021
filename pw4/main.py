from domains.StudentMarkManagementSystem import StudentMarkManagementSystem
import curses

screen = curses.initscr()
systemObj = StudentMarkManagementSystem(screen)
systemObj.startSMMS()