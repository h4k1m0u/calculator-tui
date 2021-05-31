#!/usr/bin/env python
import curses

def main(stdscr: 'curses._CursesWindow'):
    """
    Called by curses.wrapper() & restores terminal state at end of execution
    Explicit type hint for `stdscr` for autocomplete

    @param stdscr  Main screen (Window) to print onto
    """
    # initialize & define terminal colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # hide cursor
    curses.curs_set(0)

    # main loop
    c = ''
    while c != ord('q'):
        # terminal dimensions
        n_rows, n_cols = stdscr.getmaxyx()

        # print message at center of screen
        message = 'Hello to this app'
        x_message, y_message = n_cols // 2 - len(message) // 2, n_rows // 2
        stdscr.attron(curses.A_BOLD | curses.color_pair(1))
        stdscr.addstr(y_message, x_message, message)

        # print status bar
        statusbar = " Press 'q' to exit"
        y_statusbar = n_rows - 1
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(y_statusbar, 0, statusbar)
        stdscr.addstr(y_statusbar, len(statusbar), ' ' * (n_cols - len(statusbar) - 1))

        # TODO: print a menu

        # wait for keypress
        c = stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)
