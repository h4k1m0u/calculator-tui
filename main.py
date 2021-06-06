#!/usr/bin/env python
"""
Render a terminal UI with menu & status bar
"""
import curses
import curses.panel

from menu import Menu
from panel import make_panel


def main(stdscr: 'curses._CursesWindow'):
    """
    Called by curses.wrapper() & restores terminal state at end of execution
    Explicit type hint for `stdscr` for autocomplete

    @param stdscr Main screen (Window) to print onto
    """
    # initialize & define terminal colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # hide cursor
    curses.curs_set(0)

    # main loop
    items = ['Run game', 'Options', 'Quit game']
    menu = Menu(stdscr, items)

    key = ''
    while True:
        # render menu
        menu.draw()

        # panels: windows with depth (no linters) - update virtual panels stack
        panel1 = make_panel('Panel1', 10, 10, 20, 20)  # noqa: F841,E501 #pylint: disable=unused-variable
        panel2 = make_panel('Panel2', 10, 10, 25, 25)  # noqa: F841,E501 #pylint: disable=unused-variable
        curses.panel.update_panels()

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

        # menu navigation with arrow keys presses
        if key == curses.KEY_UP:
            menu.move(step=-1)
        elif key == curses.KEY_DOWN:
            menu.move(step=1)
        elif key == ord('q'):
            break


if __name__ == '__main__':
    curses.wrapper(main)
