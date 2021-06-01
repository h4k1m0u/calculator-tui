#!/usr/bin/env python
import curses
import curses.panel
import time


def make_panel(content, nlines, ncols, y, x):
    """
    Important to return panel otherwise will be garbage collected
    """
    win = curses.newwin(nlines, ncols, y, x)
    win.box()
    win.addstr(0, 0, content)
    panel = curses.panel.new_panel(win)

    return panel


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
    key = ''
    while key != ord('q'):
        # TODO: print a menu using panels
        # panels: windows with depth - update virtual panels stack
        panel1 = make_panel('Panel1', 10, 10, 0, 0)
        panel2 = make_panel('Panel2', 10, 10, 5, 5)
        curses.panel.update_panels()
        stdscr.refresh()
        
        time.sleep(1)

        panel1.top()
        curses.panel.update_panels()

        # stdscr.box()

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
        stdscr.addstr(
            y_statusbar, len(statusbar), ' ' * (n_cols - len(statusbar) - 1))

        # wait for keypress
        key = stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)
