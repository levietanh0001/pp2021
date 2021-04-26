import curses


def print_menu(stdscr, selected_row_idx):
    menu = ['AddStudent', 'AddCourse', 'AddMark', 'ShowStudent', 'ShowCourse', 'ShowMark', 'StudentAverageGpa',
            'SortDescendingOrder', 'Decompress File', 'Exit']
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = int(w // 2 - len(row) // 2)
        y = int(h // 2 - len(menu) // 2 + idx)
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()
